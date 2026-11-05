# Change Log

All notable changes to the **CMsoft Import for Step7** extension (formerly Step7 Import/Export) are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.5.0] - 2026-11-05

### Added

- **S7-GRAPH support** — sequencers are imported as `.gr7` files and exported as GRAPH sources, compiled by S7-GRAPH, new sequencers included; compile errors are shown in PROBLEMS.
- **What's New** — after an update a tab shows what the version brings and the new CMsoft video; **Step7: What's New** opens it again.
- **MCP server for AI agents** (PRO) — Claude Code, Claude Desktop, Cursor and Copilot's agent mode can use the Step7 tools.
- **LAD and FBD blocks keep their language** — an exported block is saved in LAD or FBD again, and a new block can be created in FBD.
- **I/O modules in the hardware configuration** — the imported hardware configuration lists the modules with their order numbers and I/O addresses.
- **Functional descriptions of existing programs** — the AI instructions of Prepare Workspace explain how to document a program from its code.
- **Problems of imports and exports in PROBLEMS** — what an import or export could not write, or wrote with a warning, is listed with the reason.

### Changed

- **PROBLEMS after an export** — an export replaces only the entries of the files it exported.

### Fixed

- **Instance DBs go with their FB** — an export compiles the instance DBs of an exported FB with it, so the blocks that call the FB compile; a caller that was not exported is named in PROBLEMS.
- **No block is lost after a failed compile** — a block the compile removed is put back, or kept in the program's sources as `<block>_previous` with the reason in PROBLEMS.
- **Faster export and Open Project** when SIMATIC Manager lists many projects; the log shows the time of every exported block.
- **Export order** — blocks that use multi-instances or UDTs declared by number are compiled after them.
- **Symbol table export** — the next import reads the new table, and no Notepad window is left open.
- **Refresh license status** works with an active license.

## [3.4.0] - 2026-10-24

### Changed

- **License check after an update** — the first start after an update checks the license with the license server once.
- **FREE plan: 10 blocks per import or export, 15 minutes between operations** — the same limits as in CMsoft Import for TiaPortal; PRO and the free trial have no limits.
- **License dialog: one button** — **Buy License** opens the license panel.
- **Terms of Sale 1.3** — PRO is sold as a monthly or yearly subscription.

## [3.3.0] - 2026-10-19

### Changed

- **No .NET runtime to install** — the extension runs on the .NET Framework 4.8 built into Windows 10 and 11; licenses stay valid.

## [3.2.0] - 2026-10-17

### Changed

- **README: website link** — the README starts with a link to [www.cmsoft.com.pl](https://www.cmsoft.com.pl).

## [3.1.0] - 2026-10-17

### Added

- **Prepare Workspace next to the other CMsoft extensions** — the AI instructions are in files and sections named after the extension, so one workspace holds the instructions of several CMsoft extensions.
- **FREE and PRO** — opening projects, the import and the AWL packages are free; the unlimited export, the AI tools, the CLI bridge and Prepare Workspace are PRO, with a 14-day free trial ([Terms of Sale](TERMS.md)).
- **The user manual inside VS Code** — **Step7: Open User Manual** shows it offline; **Step7: Search the User Manual** opens a chapter.

### Changed

- **New name: CMsoft Import for Step7** — the extension ID, the command IDs and the settings stay the same.
- **New icons.**
- **License change** — the extension is commercial software under the [End User License Agreement](LICENSE.md); versions up to 2.0.3 remain MIT-licensed.
- **Much smaller package.**
- **The log** in the format of the other CMsoft extensions.
- **Safer workspace writes and clearer errors.**
- **The CMsoft shop** has its own address: <https://shop.cmsoft.com.pl>.
- **Disclaimer of liability** in the user manual and the walkthrough.

### Fixed

- **Imports keep your work** — a source changed in the workspace is kept, and files that are not block files are no longer deleted.
- **Umlauts and Polish letters** survive the way between Step7 and VS Code.
- **SIMATIC Manager is no longer closed** when a project is opened.
- **Safer exports via SIMATIC Manager** — a block that fails to compile is put back, compile warnings no longer fail an export, an export stops when SIMATIC Manager cannot be used, and blocks that use a failed block are held back.
- **Exports touch only the objects they mean** — sources, programs and projects are matched by their exact names.
- **Modified blocks** — only the blocks you changed count as modified; system blocks are never exported.
- **Generate AWL Sources** writes the sources SIMATIC Manager generates.
- **Refresh Project** shows blocks added in SIMATIC Manager.
- **Symbol tables** — the export reads the file you saved last.
- **Projects with localized folder names** are imported via SIMATIC Manager.
- **Fewer and clearer messages** — one message when a project cannot be opened, installation problems reported once, errors of CLI and Copilot imports reported.
- **No more freezes** when SIMATIC Manager shows a dialog.
- **The log** no longer lists the other projects of SIMATIC Manager.
- **Copilot** — the `@step7` chat participant runs the Step7 tools, and `step7_fix_compile_errors` no longer stops until a window reload.
- **Workspace files** — Import All no longer overwrites `.github/copilot-instructions.md`, and `.gitignore` keeps the CLI token out of Git.
- **The CLI client** runs on the runtime of VS Code.
- **Smaller fixes** in the Project Structure view, the Problems view and the settings toggles.

## [2.0.3] - 2026-07-06

### Changed

- **CLI bridge is now opt-in** — `step7Import.cli.enabled` defaults to `false`.
- **CLI enable prompt** — starting the CLI bridge while it is off offers to enable it.

### Added

- **CLI Bridge toggle** — in the Step7 Connection view.

## [2.0.0] - 2026-06-10

### Added

- **External CLI bridge** — Step7 import and export operations for scripts, on this computer only.
- **Bundled Node.js CLI client** — `step7-cli.js` with the same command names as the Copilot tools.
- **Automation diagnostics** — `get_logs` for the recent log entries.

### Changed

- **CLI payload handling** — inline JSON, files and stdin.
- **CLI command compatibility** — command names with or without the `step7_` prefix.

## [1.0.122] - 2026-06-08

### Fixed

- **Opening STEP 7 projects on other computers** — the package contains the complete bridge.
- **Disconnect** — Close Project reliably clears the connection.

## [1.0.116] - 2026-06-02

### Added

- **Export Symbol Table via SIMATIC Manager** — the workspace symbol table goes back into the Step7 program.
- **Copilot symbol export tool** — `step7_export_symbols_to_simatic`.

### Changed

- **Project tree export menu** — the symbol table export is on the Program and Symbol Table nodes.

## [1.0.114] - 2026-04-30

### Added

- **Faster import of large programs.**
- **Per-block progress** in the progress bar.

## [1.0.0] - 2026-04-01

### Added

- **Import Hardware Configuration** — CPUs, CPs, network interfaces and master systems of a station or of all stations.

## [0.1.0] - 2025-06-30

### Added

- **Open Step7 Project** — `.s7p` projects with stations, CPUs and programs.
- **Import** — all blocks of a program, a block folder, single or selected blocks, symbol tables and watch tables.
- **Generate AWL sources** through SIMATIC Manager.
- **German (AWL) or English (STL) mnemonics** and symbolic names.
- **Know-how protected blocks** are recognized.
- **Progress reporting** and a status bar with the project.
- **Copilot instructions and a project description template** for AI-assisted work.
