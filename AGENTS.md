## CMsoft Import for Step7

Step7 V5.7 projects are mirrored into the workspace (`Step7Export/`) and exported back to SIMATIC Manager with the
**CMsoft Import for Step7** VS Code extension. The complete instructions are shared with GitHub Copilot:

- [.github/instructions/step7-import.instructions.md](.github/instructions/step7-import.instructions.md) — the AWL /
  STL source format, block structure, editing and re-import, rules;
- [.github/instructions/step7-import-cli.instructions.md](.github/instructions/step7-import-cli.instructions.md) —
  the CLI bridge (`.step7/cli.json`).

Pull request guidelines:

- Keep changes scoped to the requested task. Avoid drive-by reformatting of Step7-generated files: every changed
  file counts as a modified block, and the export sends it back into SIMATIC Manager and compiles it.
- Never edit the hidden `.source-hashes.json` files - they record what the last import wrote or the last export
  sent, and tell the extension which blocks were modified.
