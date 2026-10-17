# Change Log

All notable changes to the **CMsoft Import for Step7** extension (formerly Step7 Import/Export) will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.2.0] - 2026-10-17

### Changed

- **README: website link** — the README starts with a link to [www.cmsoft.com.pl](https://www.cmsoft.com.pl); its *FREE and PRO* table is headed like in the other CMsoft extensions.

## [3.1.0] - 2026-10-17

### Added

- **Prepare Workspace next to the other CMsoft extensions** (CMsoft workspace protocol) — the instructions for AI agents are in files named after the extension (`.github/instructions/step7-import.instructions.md` — applied by Copilot to every file —, `step7-import-cli.instructions.md`, `Tools/step7_cli_example.py`); `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.gitignore` and `Tools/README.md` get one section of CMsoft Import for Step7 next to the sections of CMsoft Import for TiaPortal and the migrators, so a shared workspace holds the instructions of all of them. The block list of *Import All* is a section of its own (`step7-import.blocks`); the list of earlier versions moves into it. Running Prepare Workspace again updates the extension's own section and files; your text outside the sections, and files you made your own, stay. Unchanged copies of the templates of earlier versions are replaced; `prepare_workspace` returns what changed. The workspace `.gitignore` now also ignores `UserFiles/*`.

- **FREE and PRO** — opening and browsing projects, the import from Step7 (blocks, symbol tables, watch tables, hardware configuration), Generate AWL, Show Modified Blocks, the export of AWL packages to a folder and the symbol table export via SIMATIC Manager stay free; the block export via SIMATIC Manager is free for up to 10 blocks per operation. **PRO** unlocks the unlimited export, the Copilot tools and the `@step7` chat participant, the CLI bridge and Prepare Workspace. The license panel (**CMsoft Import for Step7: Manage License / Subscription**) offers a free 14-day trial and the purchase of a subscription or a one-time license, with a 14-day money-back guarantee; each license covers one computer ([Terms of Sale](TERMS.md)). The license is shown in the **CMsoft** item in the status bar — one item for all installed CMsoft extensions — and in the *Connection* view.
- **The user manual inside VS Code** — **Step7: Open User Manual** shows the user manual (installation, setting up STEP 7, every function with screenshots, a complete worked example, Copilot and CLI, settings, license, troubleshooting) in VS Code's Markdown preview, offline; **Step7: Search the User Manual** opens a chapter or section. The manual also opens from the empty *Project Structure* view, from the walkthrough *Get Started* (*Welcome: Open Walkthrough…*) and from the **Open Help** button when a project cannot be opened. The **CMsoft** item in the status bar and **Help: CMsoft Manuals…** list the manuals of all installed CMsoft extensions.

### Changed

- **New name: CMsoft Import for Step7** — the extension formerly called *Step7 Import/Export* is now *CMsoft Import for Step7*: the activity bar view, the Output channel, the license commands (*CMsoft Import for Step7: …*), the walkthrough, the chat participant (`@step7` keeps its handle) and the user manual carry the new name; the other commands keep their *Step7:* prefix. The extension ID (`MariuszCzyrnek.step7-import`), the command IDs and the settings stay the same.
- **New icons** — the CMsoft cloud with *cm* and *Import* in blue; in the activity bar the same cloud with an *S*.
- **License change** — from this version the extension is commercial software under the [End User License Agreement](LICENSE.md). Versions up to 2.0.3 were released under the MIT License and remain MIT-licensed.
- **Much smaller package** — a fraction of the previous size: the COM helper for SIMATIC Manager runs on the .NET Framework 4.8 built into Windows 10 / 11 instead of carrying its own copy of the .NET runtime.
- **The log in the format of the other CMsoft extensions** — the Output channel is a VS Code log channel: every line starts with the date, the time and the level (`[info]`, `[warning]`, `[error]`) in colour, and the Output view filters it by level. Windows paths with blanks are written as file links, so a click opens them. `get_logs` (CLI) and `step7_get_logs` (Copilot) return the lines in the same form.
- **Safer workspace writes** — a replaced source is written all or nothing (an interrupted write leaves the previous file).
- **Clearer errors** — a request with a missing parameter names it ("Parameter 'programIndex' must be an integer"); errors of the COM helper no longer carry stack traces.
- **The CMsoft shop has its own address** — the README, the user manual and the documents that ship with the extension (End User License Agreement, Terms of Sale, Privacy Policy) point to <https://shop.cmsoft.com.pl>: the extension's page, the plans and the Terms of Sale, Refund and Privacy policies. The terms of the documents are unchanged.
- **The disclaimer of liability in the user manual and the walkthrough** — the user manual sums up sections 12–14 of the End User License Agreement in section 14.10 (*Disclaimer of liability*), warns in section 2.7 and says in section 11.9 that code written by an AI assistant is not reviewed or verified by CMsoft; the *Get Started* walkthrough has a step **Work safely**. The README's *Disclaimer of Liability* names the AI assistants and the project backups and follows the agreement: liability is excluded or limited to the extent permitted by law, and liability that the law does not allow to exclude and the rights of consumers are not affected. `@step7` and the instructions of **Prepare Workspace** tell assistants never to call generated code verified and to leave safety programs alone unless you confirm an independent review. The terms of the documents are unchanged.

### Fixed

- **The documentation assumed the sources of the extension** — the client script `step7-cli.js` needed a separately installed Node.js and its help showed only `npm run step7:cli`, which works in the source repository only; it now runs on the runtime of VS Code (the `step7` PowerShell function of section 12.4 of the manual, also in the agent instructions of **Step7: Prepare Workspace** and in the README). `Tools/step7_cli_example.py` no longer offers `--launch-extension-host` (it started VS Code on the source code of the extension). The manual prints its example scripts in full and no longer points to the repository, its `demo-project` folder or a build of the extension; the *License* badge of the README no longer breaks when the package is built, and a release copies the license, terms, privacy and security documents to the public documentation repository, which the links of the README on the Marketplace page lead to.
- **An import no longer overwrites or deletes your work** — with *Only changed* a source you changed since the last import or export is kept and reported as *kept* (a block changed in the workspace and in Step7 is named as such); before, any Step7 version that differed overwrote it. *Overwrite all* still replaces everything; **Import Block** on one block offers **Replace with Step7 Version**. Import All and Import Block Folder delete the file of a block that is gone from Step7 only while it is as the import wrote it: new blocks you write in `Blocks/` (not in Step7 yet), edited sources and files that are no block files (notes, `.gitkeep` …) are kept - before, every file in `Blocks/` the import did not write was deleted. The files of a block Step7 could not read are kept as well, and a cancelled import deletes nothing (it used to delete the files of all blocks it had not reached)
- **Umlauts and Polish letters survive the way between Step7 and VS Code** — blocks imported through SIMATIC Manager no longer get "�" instead of ä, ö, ü, ß, ą, ę, ł … in comments and string constants, and blocks and symbol tables exported to SIMATIC Manager no longer arrive garbled ("Ĺź" instead of "ż"): the extension now reads and writes the Windows ANSI code page that Step7 uses. A workspace file that still contains "�" from an earlier import is not exported; the export names the file and line, so you can import the block again first
- **SIMATIC Manager is no longer closed when a project is opened** — if SIMATIC Manager is already running without the requested project, the extension now asks you to open the project there instead of closing SIMATIC Manager (with your other projects and editors) and restarting it. A project is also recognized as open when it is not the active one in SIMATIC Manager, or when its name differs from the `.s7p` file name
- **A block whose new source fails to compile is no longer deleted from the project** — when the compile fails, its previous version is put back and the export says so. Blocks Step7 cannot generate a source for (e.g. compiled from SCL) cannot be saved; the export names them if a failed compile leaves them missing
- **Compile warnings no longer fail an export** — a block that compiled with warnings is exported; the warnings appear in the Problems view and now stay there after the export. Sources that fail the syntax check before an export are shown in the Problems view too
- **An export via SIMATIC Manager stops when SIMATIC Manager cannot be used** — when SIMATIC Manager does not answer (e.g. an open dialog) or is no longer running, or the project or program is not found, the export stops at that block with the reason instead of waiting up to 5 minutes for every further block; the blocks not sent are listed. A block that fails to compile still does not stop the export
- **Blocks that use a block whose export failed are held back** — compiled against the version Step7 still has, they failed as well or mixed old and new; they are now not sent, the Problems view says why ("uses FB10, whose export failed - fix FB10 first"), and they go with the next export
- **The "failed" count of an export counts blocks** — a block with several compile errors counts once ("1 failed" instead of "3 failed"); the notification is a warning when blocks failed and an error when the export stopped
- **An export via SIMATIC Manager touches only the objects it means** — sources, programs and projects are matched by their exact names: a source whose name merely contains the block's (e.g. `FB10` for `FB1`), another station's `S7 Program(10)` for `S7 Program(1)` or another project whose path contains the project name are no longer used. When a source of the same name cannot be replaced, the export now fails with that reason instead of deleting all sources of the program
- **The edited block is exported, not an older copy** — when a block has a file in `Blocks/` and in `Sources/` (e.g. from *Generate AWL*), the `Blocks/` working copy is exported; the other file is named in the log
- **Show Modified Blocks and the export of modified blocks work in the default `awl` format** — only blocks you changed since the import count as modified; before, every block did, and exporting "modified" blocks checked the whole program against Step7
- **An exported block no longer counts as modified** — a block that compiled in SIMATIC Manager, or that Step7 already had as it is in the workspace, is left out by Show Modified Blocks and the next *Only modified* export, and the next import may update it
- **System blocks are never exported** — SFB, SFC and SDB sources (from *Import system blocks* or *Generate All AWL Sources*) no longer count as modified, are not sent to SIMATIC Manager or into AWL packages, and the FREE limit does not count them; selecting only system blocks says why nothing is exported
- **Generate All AWL Sources writes the sources SIMATIC Manager generates** — like Import All and Generate AWL Source; before, it wrote decompiled sources (an FBD block came out as a dump). Blocks SIMATIC Manager generates no source for are decompiled and named in the log and the notification. System blocks are generated only with *Import system blocks*; the generated files no longer count as modified until you edit them, and the command can be cancelled
- **Generate AWL Source names the file it wrote** (e.g. `Motor_FB10.awl`) instead of `<block>.awl`
- **Refresh Project shows blocks added in SIMATIC Manager** — Refresh (also the `refresh` CLI command and Copilot tool) reads the project again from its files; before, it showed the block list read when the project was opened. An export that compiled blocks into Step7 reads the project again too, so new blocks appear in the Project Structure view
- **Export Symbol Table via SIMATIC Manager reads the file you saved last** — after a change of the symbol list format, an old `_symbols.json` no longer wins over an edited `_symbols.csv`; a newer `_symbols.xlsx` (not readable yet) is reported instead of silently exporting an older file
- **The symbol list format describes the file it writes** — `json`, `xlsx` or `csv` write one file `_symbols.<format>`; the setting promised `_symbols.json` in addition
- **Import via SIMATIC Manager into projects whose sources folder is not called "Sources"** — the *Sources* and *Blocks* folders of an S7 program are recognized by their object type instead of their name, so source import also works for projects created with older or localized Step7 versions (folder names such as "Source files" or "Sources Files"); previously it failed with "Sources container not found"
- **A failed Import All keeps the `Sources/` folder** — it is cleared only after the program has been read from Step7
- **Import Watch Tables appears on watch tables** in the Project Structure view; a watch table imported on its own goes to the same file as with Import All
- **One message when a project cannot be opened** — when the bridge program could not start, *Open Step7 Project* showed "Open in SIMATIC Manager failed: …" and then "Open Step7 project failed: …"; now only the second one, with **Open Help**. A SIMATIC Manager that cannot open the project shows no error any more: the project is read from its files. The same for the Copilot tool `step7_open_project` and the CLI command `open_project`, unless `requireSimaticManager` is set
- **Installation problems are reported once** — missing bridge files or a missing .NET runtime were reported at every start attempt of the bridge, up to three times in one *Open Step7 Project* (for the runtime: three times the question to install it). Now once per session, with **Open Help**
- **A SIMATIC Manager dialog no longer freezes the extension** — the COM helper is stopped when SIMATIC Manager does not answer for 5 minutes (SIMATIC Manager keeps running), every call has a time limit, and a bridge that ends unexpectedly closes the project with a message
- **Open Step7 Project no longer writes every project registered in SIMATIC Manager into the log** — only their number; the names and paths of other projects do not belong in a log that is shared or read by Copilot (`get_logs`). A project found in SIMATIC Manager's list is reported as *registered in SIMATIC Manager* instead of *attached*: it is not necessarily open there
- **Block languages in English** — the Project Structure view and Import Selected Blocks show FBD and LAD (German mnemonics: FUP and KOP) instead of always the German names
- **The Problems view forgets the problems of deleted sources** — deleting or renaming a source (also outside VS Code) removes its compile problems, and `get_problems` no longer returns problems of files that are gone
- **Imports from the CLI and Copilot report errors** — `import_blocks`, `import_program` and `import_project` answer `success: false` when a block could not be imported (e.g. `FB999` that does not exist: *Import of 1 block(s): 1 errors - FB999: Block FB999 not found*), with what was imported in `data`; before, they answered `success: true` and "Imported 1 block(s)". The CLI client exits with code 2
- **`step7-cli.js` reports a missing or invalid state file, invalid `--json` and an unreachable CLI bridge in one line** (exit code 1) instead of a stack trace
- **The @step7 chat participant runs the Step7 tools** — tool calls of the model were dropped, so the participant stopped after its first answer; it now runs them (with their confirmations) and knows the earlier turns of the conversation
- **`step7_fix_compile_errors` no longer refuses until a window reload** — its iteration limit counts one fix run (calls less than 10 minutes apart) and starts over after a successful compile
- **`.github/copilot-instructions.md` is no longer overwritten by Import All** — the import keeps only the block list section up to date; your own text stays. A missing file is created from the workspace template
- **The `.gitignore` of Prepare Workspace keeps the CLI bridge token out of Git** — it ignores `.step7/` (with the token in `cli.json`) and `CLAUDE.local.md`; before, it held only an entry that ignored the `.gitignore` itself
- **Settings toggles change the setting that is in effect** — a value from the workspace settings is changed there (before, the user setting was changed and stayed overridden); a hand-edited setting with an invalid value counts as not set. *Show Modified Blocks* on a program node uses that program

## [2.0.3] - 2026-07-06

### Changed

- **CLI bridge is now opt-in** — `step7Import.cli.enabled` defaults to `false`; the localhost JSON CLI bridge no longer starts automatically and `.step7/cli.json` is not created until the setting is enabled
- **CLI enable prompt** — running `step7.startCli` or clicking the CLI Bridge toggle while disabled now shows an information message with options to enable the setting or open Settings

### Added

- **CLI Bridge toggle** — new `step7.toggleCli` command and a **CLI Bridge** On/Off item in the Step7 Connection view

## [2.0.0] - 2026-06-10

### Added

- **External CLI bridge** — expose Step7 import/export operations through a localhost-only JSON bridge secured with a per-session token in `.step7/cli.json`
- **Bundled Node.js CLI client** — `step7-cli.js` for scripted access to project status, workspace preparation, logs, block listing, imports, and exports using the same command names as Copilot/MCP tools
- **Automation diagnostics** — add `get_logs` CLI access with limit, level, and text filters for recent Step7 output channel entries

### Changed

- **CLI payload handling** — support inline JSON, `@file` JSON payloads, stdin payloads, comma-separated block lists, timeout control, and explicit state-file selection for external automation
- **CLI command compatibility** — accept command names with or without the `step7_` prefix so scripts can use either short names or Copilot/MCP tool names

## [1.0.122] - 2026-06-08

### Fixed

- **Opening STEP7 projects on other computers** — the package contains the complete bridge (with its libraries and the native libnodave DLLs), so projects open on machines without a development setup
- **Step7 disconnect action** — make the Disconnect/Close Project command reliably clear the VS Code connection state, stop the bridge process, and avoid hanging if the bridge close request does not respond

## [1.0.116] - 2026-06-02

### Added

- **Export Symbol Table via SIMATIC Manager** — push workspace `_symbols.json` or `_symbols.csv` back into the Step7 program symbol table through the SIMATIC Manager COM API
- **Copilot symbol export tool** — new `step7_export_symbols_to_simatic` Language Model Tool lets Copilot export edited symbol tables from the workspace to SIMATIC Manager
- **Workspace symbol table reader** — JSON/CSV symbol table files are converted to STEP 7 SDF format before COM import

### Changed

- **Project tree export menu** — symbol table export is available from both Program and Symbol Table nodes

## [1.0.114] - 2026-04-30

### Added

- **Faster import of large programs** — all block sources are generated in one SIMATIC Manager session instead of one helper process per block
- **Per-block progress reporting** — VS Code progress bar now shows which blocks are being generated during COM source generation
- **AWL source splitter** — if COM API returns a multi-block AWL file, it is automatically split into individual block sources
- **Graceful fallback** — if that session fails, the blocks are generated one by one

---

## [1.0.0] - 2026-04-01

### Added

- **Import Hardware Configuration** — read station HW config (CPUs, CPs, network interfaces, Profibus/Profinet master systems) from Step7 projects
- **Per-station HW export** — import HW config for a single station via inline icon on station nodes, or all stations from the project node
- **HWconfig directory** — exported to `Step7Export/<Project>/<Station>/HWconfig/_hwconfig.json`

---

## [0.1.0] - 2025-06-30

### Added

- **Open Step7 Project** — browse `.s7p` project files with full station/CPU/program hierarchy
- **Import all blocks** — one-click import of all blocks from a program with two-phase pipeline (libnodave + COM API)
- **Import block folder** — import all blocks of a given type (OB, FB, FC, DB, UDT)
- **Import single block** — import individual blocks via tree context menu
- **Multi-select import** — Ctrl+Click multiple blocks in the tree, then import all selected
- **Import selected blocks** — QuickPick multi-select for choosing blocks to import
- **Import symbol table** — export as JSON, XLSX, or CSV
- **Import watch tables** — export VAT (variable tables)
- **Generate AWL sources** — full AWL/STL source generation via Step7 COM API
- **Bilingual mnemonics** — German (AWL) or English (STL) instruction set
- **Symbolic name resolution** — resolve addresses to symbolic names from the symbol table
- **Know-how protected block handling** — detect and gracefully handle protected blocks
- **Workspace synchronization** — clean existing blocks before import to keep workspace in sync
- **Progress reporting** — real-time percentage progress in VS Code UI and output log
- **Copilot instructions** — auto-generated `.github/copilot-instructions.md` with AWL syntax guide
- **Project description template** — `.github/ProjectDescription.md` for AI-assisted documentation
- **Status bar** — real-time project info display
