#!/usr/bin/env python3
# cmsoft:managed step7-import - Prepare Workspace of CMsoft Import for Step7 updates this file; delete this line to keep your own version
r"""
Open a Step7 project through the local Step7 CLI bridge and import all programs.

Examples:
    python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --pretty
    python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --overwrite-all --pretty
    python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --libnodave-only --log-level error --pretty

Status and Step7 Output log lines are written to stderr. The final machine-readable
result is written to stdout as JSON. Press Ctrl+C to interrupt the script.
"""

import argparse
import http.client
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser(
                description="Open a Step7 project through the local Step7 CLI bridge and import all programs into the workspace.",
                formatter_class=argparse.RawDescriptionHelpFormatter,
                epilog=r"""
Examples:
    python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --pretty
    python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --overwrite-all --pretty
    python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --libnodave-only --log-level error --pretty
""".strip(),
    )
    parser.add_argument("project", help="Path to the Step7 .s7p/.s7l project file")
    parser.add_argument(
        "--workspace",
        default=str(SCRIPT_DIR.parent),
        help="Workspace folder containing .step7/cli.json; defaults to the workspace this script is in (the parent of Tools/)",
    )
    parser.add_argument("--timeout", type=int, default=0, help="CLI request timeout in milliseconds; 0 disables it")
    parser.add_argument("--overwrite-all", action="store_true", help="Write the Step7 version of every block, also over workspace changes")
    parser.add_argument(
        "--libnodave-only",
        action="store_true",
        help="Do not open SIMATIC Manager before import. By default the script requires SIMATIC Manager open to succeed.",
    )
    parser.add_argument("--log-limit", type=int, default=80, help="Number of recent Step7 Output log lines to show; 0 disables log display")
    parser.add_argument(
        "--log-level",
        choices=["info", "warn", "error", "section", "all"],
        default="all",
        help="Filter displayed Step7 Output log lines by level",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the final JSON result")
    args = parser.parse_args()

    project_path = Path(args.project).expanduser().resolve()
    workspace_path = Path(args.workspace).expanduser().resolve()
    state: dict[str, Any] = {}

    try:
        status(f"Workspace: {workspace_path}")
        status(f"Project: {project_path}")
        validate_paths(project_path, workspace_path)
        status("Reading Step7 CLI bridge state")
        state = ensure_cli_state(workspace_path)
        status(f"Connected to Step7 CLI bridge at {state['host']}:{state['port']}")

        status("Opening Step7 project" + (" through libnodave only" if args.libnodave_only else " through SIMATIC Manager"))
        open_result = call_step7_bridge(
            state,
            "open_project",
            {
                "filePath": str(project_path),
                "openInSimaticManager": not args.libnodave_only,
                "requireSimaticManager": not args.libnodave_only,
            },
            args.timeout,
        )
        ensure_success("open_project", open_result)
        status("Project opened")

        status("Importing all programs into workspace. Press Ctrl+C to stop waiting for the operation.")
        import_result = call_step7_bridge(
            state,
            "import_project",
            {"overwriteAll": args.overwrite_all},
            args.timeout,
        )
        ensure_success("import_project", import_result)
        status("Import completed")
        show_output_logs(state, args.log_limit, args.log_level, args.timeout)

        return emit(
            {
                "success": True,
                "projectPath": str(project_path),
                "workspace": str(workspace_path),
                "steps": [
                    {"command": "open_project", "result": open_result},
                    {"command": "import_project", "result": import_result},
                ],
            },
            args.pretty,
            0,
        )
    except KeyboardInterrupt:
        status("Interrupted by user")
        show_output_logs(state, args.log_limit, args.log_level, args.timeout)
        return emit(
            {
                "success": False,
                "interrupted": True,
                "error": "Interrupted by user",
                "projectPath": str(project_path),
                "workspace": str(workspace_path),
            },
            args.pretty,
            130,
        )
    except Exception as error:
        status(f"Failed: {error}")
        show_output_logs(state, args.log_limit, args.log_level, args.timeout)
        return emit(
            {
                "success": False,
                "error": str(error),
                "projectPath": str(project_path),
                "workspace": str(workspace_path),
            },
            args.pretty,
            1,
        )


def status(message: str) -> None:
    print(f"[step7-import] {message}", file=sys.stderr, flush=True)


def validate_paths(project_path: Path, workspace_path: Path) -> None:
    if not project_path.exists():
        raise FileNotFoundError(f"Step7 project file not found: {project_path}")
    if project_path.suffix.lower() not in {".s7p", ".s7l"}:
        raise ValueError(f"Expected a .s7p or .s7l Step7 project file, got: {project_path}")
    if not workspace_path.exists():
        raise FileNotFoundError(f"Workspace folder not found: {workspace_path}")


def ensure_cli_state(workspace_path: Path) -> dict[str, Any]:
    state_path = workspace_path / ".step7" / "cli.json"
    if state_path.exists():
        return read_cli_state(state_path)
    raise FileNotFoundError(
        f"Step7 CLI state not found: {state_path}. Open this workspace in VS Code with CMsoft Import for Step7 active "
        "and switch the CLI bridge on (row CLI Bridge of the Connection view, or the setting step7Import.cli.enabled)."
    )


def read_cli_state(state_path: Path) -> dict[str, Any]:
    with state_path.open("r", encoding="utf-8") as state_file:
        state = json.load(state_file)
    for key in ("host", "port", "token"):
        if not state.get(key):
            raise ValueError(f"Invalid Step7 CLI state file {state_path}: missing {key}")
    return state


def call_step7_bridge(
    state: dict[str, Any],
    command: str,
    payload: dict[str, Any],
    timeout_ms: int,
) -> dict[str, Any]:
    body = json.dumps({"command": command, "args": payload}).encode("utf-8")
    connection = http.client.HTTPConnection(
        str(state["host"]),
        int(state["port"]),
        timeout=timeout_ms / 1000 if timeout_ms > 0 else None,
    )
    try:
        connection.request(
            "POST",
            "/api",
            body=body,
            headers={
                "authorization": f"Bearer {state['token']}",
                "content-type": "application/json; charset=utf-8",
            },
        )
        response = connection.getresponse()
        text = response.read().decode("utf-8")
        try:
            result = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Step7 bridge returned invalid JSON for {command}: {text}") from exc
        if response.status >= 400:
            raise RuntimeError(result.get("error") or f"Step7 bridge request failed with HTTP {response.status}")
        return result
    finally:
        connection.close()


def show_output_logs(state: dict[str, Any], limit: int, level: str, timeout_ms: int) -> None:
    if not state or limit <= 0:
        return
    try:
        result = call_step7_bridge(
            state,
            "get_logs",
            {"limit": limit, "level": level},
            timeout_ms,
        )
        if result.get("success") is False:
            status(f"Could not read Step7 Output logs: {result.get('error', result)}")
            return
        lines = ((result.get("data") or {}).get("lines") or [])
        if not lines:
            status("Step7 Output log has no matching entries")
            return
        print("\n--- Step7 Output log ---", file=sys.stderr)
        for line in lines:
            print(line, file=sys.stderr)
        print("--- End Step7 Output log ---\n", file=sys.stderr)
    except Exception as error:
        status(f"Could not read Step7 Output logs: {error}")


def ensure_success(command: str, result: dict[str, Any]) -> None:
    if result.get("success") is False:
        raise RuntimeError(f"{command} failed: {result.get('error', result)}")


def emit(payload: dict[str, Any], pretty: bool, exit_code: int) -> int:
    print(json.dumps(payload, indent=2 if pretty else None))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())