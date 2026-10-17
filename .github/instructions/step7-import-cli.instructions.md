---
applyTo: "Tools/**"
description: "CMsoft Import for Step7 - the CLI bridge for scripts and agents"
---
<!-- cmsoft:managed step7-import - Prepare Workspace of CMsoft Import for Step7 updates this file; delete this line to keep your own version -->
# Step7 CLI Instructions

This workspace can be controlled by the CMsoft Import for Step7 VS Code extension through a local CLI bridge. Use it when an AI agent or external script needs to prepare the workspace, open a Step7 project, import blocks, export changes, or read diagnostics without clicking in the VS Code UI.

## Requirements

1. Open this workspace in VS Code with the CMsoft Import for Step7 extension active (the CLI bridge needs a PRO license).
2. Make sure the extension setting `step7Import.cli.enabled` is `true`.
3. Wait until `.step7/cli.json` exists in the workspace root.
4. Keep `.step7/cli.json` private. It contains a per-session token for the local bridge and must not be committed - `.step7/` belongs in `.gitignore`.

The bridge listens only on `127.0.0.1`. The port is selected dynamically by the operating system and is written to `.step7/cli.json`.

## State File

`.step7/cli.json` contains only the connection data needed by scripts:

```json
{
  "version": 1,
  "host": "127.0.0.1",
  "port": 58469,
  "token": "..."
}
```

If VS Code or the extension is restarted, the port and token can change. Re-read `.step7/cli.json` before each automation run.

## Python Import Helper

`Tools/step7_cli_example.py` (copied by **Step7: Prepare Workspace**) opens a project and imports all programs. It talks directly to the local bridge, so it needs neither Node.js nor the Node CLI client, and it is a starting point for project-specific scripts in `Tools/`.

Example:

```powershell
python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --pretty
```

By default, the helper requires SIMATIC Manager to open the project successfully before importing. Use `--libnodave-only` only when the import should intentionally skip SIMATIC Manager.

Useful options:

```powershell
python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --overwrite-all --pretty
python .\Tools\step7_cli_example.py "E:\Projects\PLC\Demo.s7p" --workspace . --libnodave-only --log-level error --pretty
```

Status and Step7 Output log lines go to stderr; the final result is JSON on stdout.

## Generic CLI Client

Nothing has to be installed to call the bridge - PowerShell is enough:

```powershell
$s = Get-Content .step7\cli.json | ConvertFrom-Json
$h = @{ Authorization = "Bearer $($s.token)" }
Invoke-RestMethod -Method Post -Uri "http://$($s.host):$($s.port)/api" -Headers $h -ContentType 'application/json' `
                  -Body '{"command":"list_programs","args":{}}'
```

The extension also includes a generic CLI client, `scripts\step7-cli.js` in the installed extension's folder (by default `%USERPROFILE%\.vscode\extensions\mariuszczyrnek.step7-import-<version>\`). It runs on the runtime built into VS Code, so no Node.js is needed: section 12.4 of the user manual (**Step7: Open User Manual**) defines a `step7` PowerShell function for it. Use `step7` only when that function exists in the user's PowerShell; otherwise call the bridge as above.

```powershell
step7 prepare_workspace --workspace . --pretty
step7 open_project --workspace . --filePath "E:\Projects\PLC\Demo.s7p" --openInSimaticManager true --requireSimaticManager true --pretty
step7 import_project --workspace . --pretty
step7 export_to_simatic --workspace . --json '{"program":0,"modifiedOnly":true}'
```

Every command prints JSON - `{ "success": true, "data": ..., "message": ... }` or `{ "success": false, "error": ... }` - and the client exits with code `2` when `success` is `false`. An import succeeds only when every block was imported: for a block that does not exist or cannot be read it answers `success: false`, with the reason in `error` and what it did import in `data`. Pass structured arguments with `--json '{...}'`, `--json @payload.json` or `--stdin`.

## Available Commands

Use these command names with the generic CLI. Names with the `step7_` prefix are also accepted.

| Command | Purpose |
| --- | --- |
| `prepare_workspace` | Copy Step7/Copilot templates into the workspace. |
| `get_logs` | Return recent Step7 Output log entries captured by the extension. |
| `open_project` | Open a `.s7p` or `.s7l` project. |
| `close_project` | Close the active Step7 project. |
| `current_project` | Return metadata for the active project. |
| `refresh` | Read the open Step7 project again (after changes in SIMATIC Manager) and refresh its tree. |
| `list_programs` | List S7 programs in the active project. |
| `list_blocks` | List blocks for one program. |
| `import_program` | Import all blocks and symbols for one program. |
| `import_project` | Import all programs from the active project. |
| `import_blocks` | Import selected blocks. |
| `import_hw_config` | Import hardware configuration. |
| `export_to_simatic` | Export workspace blocks into SIMATIC Manager. |
| `export_symbols_to_simatic` | Export the workspace symbol table into SIMATIC Manager. |
| `get_problems` | Return compile/export diagnostics captured by the extension. |
| `fix_compile_errors` | Run one export/compile diagnostics iteration. |

## Recommended Agent Workflow

1. Call `prepare_workspace` before creating project-specific files.
2. Call `open_project` with `openInSimaticManager: true` and `requireSimaticManager: true` when SIMATIC Manager is required.
3. Call `import_project` or a narrower import command.
4. Inspect generated files under `Step7Export/`.
5. Make source changes in the workspace.
6. Use `export_to_simatic` or `fix_compile_errors` only after confirming the intended scope.
7. Read `get_problems` after export or compile operations. A block that fails does not stop the export, but the blocks that use it are not sent: they are listed in `notExported` and go with the next export once it compiles. When the result has a `stopReason`, SIMATIC Manager could not be used (for example an open dialog): remove the cause and export again - it is not an error in the sources.
8. Use `get_logs` when a script needs the same operational details that appear in the Step7 Output panel.

## Safety Rules

- Do not commit `.step7/cli.json`.
- Do not hard-code the bridge port or token.
- Re-read `.step7/cli.json` after VS Code reloads.
- Prefer narrow export scopes when writing back to SIMATIC Manager.
- Fetch logs with `get_logs --limit <n>` when debugging automation failures; avoid storing logs permanently if they contain local project paths.
- Use `requireSimaticManager: true` when the operation must prove that SIMATIC Manager is open.
- Validate all imported/exported PLC changes in SIMATIC Manager before downloading to hardware.
