<!-- VERSION-BADGE -->
[![Version](https://img.shields.io/badge/version-1.0.118-blue)](package.json)
<!-- /VERSION-BADGE -->

[![VS Code](https://img.shields.io/badge/VS%20Code-%3E%3D1.80.0-blue?logo=visual-studio-code)](https://code.visualstudio.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-informational)](https://www.microsoft.com/windows)
[![Author](https://img.shields.io/badge/author-Mariusz%20Czyrnek-orange?logo=linkedin)](https://www.linkedin.com/in/mariusz-czyrnek)
[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=68KF5N2K5QQVY)

# Step7 Import/Export — VS Code Extension

**Bidirectional bridge between VS Code and Siemens SIMATIC Manager (Step7 V5.x)** — open `.s7p` projects, import blocks and hardware data into local files, work on them with full VS Code + Copilot support, and export changes back to Step7. The extension is optimized for AWL/STL-centric workflows and for storing PLC logic in a source-control-friendly structure.

If this extension helps your Step7 workflow, you can support ongoing development with a voluntary [PayPal donation](https://www.paypal.com/donate/?hosted_button_id=68KF5N2K5QQVY)

---

## Key Features

### Import from Step7 Project

| Capability                              | Description                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------- |
| **Open `.s7p` Project**         | Browse any SIMATIC Manager project — stations, CPUs, programs                      |
| **Import Entire Project**         | One-click import of all programs with blocks, symbols, and sources                  |
| **Import Block Folder**           | Import all blocks in a folder (OB, FB, FC, DB, UDT, etc.)                           |
| **Import Single / Multi-Select**  | Import one block or Ctrl+click to select multiple blocks in the tree                |
| **Import Symbol Table**           | Export symbol table as JSON, XLSX, or CSV                                           |
| **Import Watch Tables**           | Export VAT (variable tables)                                                        |
| **Import Hardware Configuration** | Export station HW config (CPUs, CPs, network interfaces, Profibus/Profinet) as JSON |
| **Generate AWL Sources**          | Generate AWL/STL source files via Step7 COM API                                     |
| **Project Explorer**              | Browse the full Step7 project hierarchy in the VS Code sidebar                      |

### Smart Capabilities

- **Two-phase import** — Phase 1 reads blocks via libnodave (fast bulk read), Phase 2 upgrades COM-compatible blocks via Step7 COM API for full AWL source
- **Single COM session** — Phase 2 generates all blocks in one COM session with configurable progress grouping, instead of spawning a separate process per block
- **Bilingual mnemonic support** — German (AWL) or English (STL) instruction set
- **Know-how protected block detection** — detects and handles protected blocks gracefully
- **Symbolic names** — resolves symbolic addresses from the symbol table
- **Copilot instructions** — auto-generates `.github/copilot-instructions.md` with AWL syntax rules and project description templates
- **Workspace synchronization** — cleans existing blocks before import to keep workspace in sync with Step7 project
- **Progress reporting** — real-time progress with percentage in VS Code progress bar and output log
- **Cancellation support** — cancel long-running operations via VS Code progress UI
- **Status bar** — real-time project info
- **Export back to Step7** — send changed block files from the workspace back into SIMATIC Manager
- **Export Symbol Table back to Step7** — push workspace `_symbols.json` or `_symbols.csv` into SIMATIC Manager via COM
- **Modified block detection** — quickly find workspace files that diverged from the source project before export
- **Copilot tools** — expose Step7 import/export actions, including symbol table export, as Language Model Tools for AI-assisted workflows

---

## Requirements

| Requirement               | Version                             |
| ------------------------- | ----------------------------------- |
| **OS**              | Windows 10 / 11                     |
| **SIMATIC Manager** | Step7 V5.7+ (for COM API features)  |
| **.NET**            | .NET 10 Runtime                     |
| **VS Code**         | ≥ 1.80.0                           |
| **Node.js**         | 20+ (for building / packaging only) |

> Full AWL source generation requires **SIMATIC Manager V5.7** installed on the machine.
> Basic block reading (MC7 bytecode, metadata) works without SIMATIC Manager via libnodave.

> This extension is intended for classic **Step7 / SIMATIC Manager** projects, not for **TIA Portal** projects.

---

## Installation

1. Install the extension from VS Code Marketplace (or `code --install-extension mariusz-czyrnek.step7-import`)
2. Make sure .NET 10 Runtime is installed
3. For AWL source generation, ensure SIMATIC Manager V5.7 is installed
4. Optionally adjust settings via **File → Preferences → Settings → Step7 Import/Export**

The extension checks the required Step7 bridge components on activation. If the local .NET runtime is missing, it offers an installation command automatically.

---

## Usage

### Opening a Step7 Project

1. Open VS Code in a workspace folder
2. Click the **Step7 Import/Export** icon in the Activity Bar
3. Click **Open Step7 Project** or run the command `Step7: Open Project`
4. Select a `.s7p` project file from SIMATIC Manager

### Importing Blocks

1. Open a Step7 project
2. Browse the project structure in the **Project Structure** sidebar
3. Right-click on any node to import:
   - **Project** — import all programs with all blocks and symbols
   - **Program** — import all blocks for a single program
   - **Block Folder** (OB, FB, FC, DB…) — import all blocks of that type
   - **Block** — import a single block
   - **Symbol Table** — import the symbol table
   - **Watch Table** — import a VAT
4. Use **Ctrl+Click** in the tree to select multiple blocks, then right-click → **Import Selected Blocks**
5. Import hardware configuration via the $(server) icon on **Project** or **Station** nodes
6. Files are saved under `Step7Export/<Project>/<Station>/<CPU>/<Program>/` in your workspace

### Exporting Back to Step7

1. Import or prepare the Step7 workspace structure first
2. Modify exported AWL/SCL files in VS Code
3. In the **Project Structure** view or the Explorer context menu, run one of the export commands:
   - **Step7: Export to Step7** — export the current block, folder, program, or project
   - **Step7: Export via SIMATIC Manager** — push changes back using the SIMATIC Manager route
   - **Step7: Export Symbol Table via SIMATIC Manager** — import workspace `_symbols.json` or `_symbols.csv` into the Step7 symbol table
   - **Step7: Show Modified Blocks** — inspect which blocks changed before export
4. GitHub Copilot can also call `step7_export_symbols_to_simatic` through the registered Step7 Language Model Tools
5. Validate the imported changes inside SIMATIC Manager before downloading to hardware

### Exported Directory Structure

```
<Workspace>/
├── .github/
│   ├── copilot-instructions.md       # AI coding rules for AWL/STL files
│   └── ProjectDescription.md         # Auto-generated project description
├── Step7Export/
│   └── <ProjectName>/
│       └── <Station>/
│           └── <CPU>/
│               └── <Program>/
│                   ├── Blocks/
│                   │   ├── OB/
│                   │   │   ├── OB1 — Main.awl
│                   │   │   └── OB1 — Main.json
│                   │   ├── FB/
│                   │   ├── FC/
│                   │   ├── DB/
│                   │   └── UDT/
│                   ├── Sources/
│                   │   └── *.awl
│                   └── Symbols/
│                       ├── _symbols.json
│                       ├── _symbols.xlsx
│                       └── _symbols.csv
│           └── HWconfig/
│               └── _hwconfig.json          # Station hardware configuration
```

### Workspace Templates (`.github/`)

On first import (or when you run `Step7: Prepare Workspace`), the extension scaffolds the workspace with template files:

| File / Folder                                 | Purpose                                                                                                          |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **`.github/copilot-instructions.md`** | Instructions for GitHub Copilot with full AWL/STL syntax guide, block structure rules, and project documentation |
| **`.github/ProjectDescription.md`**   | Living document describing project architecture, populated automatically by Copilot                              |

Templates are created only if they do not already exist, so your existing workspace files are preserved.

---

## Extension Settings

| Setting                                | Description                                                   | Default         |
| -------------------------------------- | ------------------------------------------------------------- | --------------- |
| `step7Import.exportFolderName`       | Folder name for Step7 exports                                 | `Step7Export` |
| `step7Import.useSymbolicNames`       | Use symbolic names in AWL code                                | `true`        |
| `step7Import.includeSystemBlocks`    | Import system blocks (SFB, SFC)                               | `false`       |
| `step7Import.includeStructureJson`   | Generate `.struct.json` files for DB/UDT                    | `true`        |
| `step7Import.showDeleted`            | Show deleted blocks                                           | `false`       |
| `step7Import.exportKnowHowProtected` | Generate source for know-how protected blocks                 | `false`       |
| `step7Import.generateSourceFormat`   | Export format:`awl` or `awl+json`                         | `awl+json`    |
| `step7Import.mnemonicLanguage`       | Mnemonic language:`de` (German AWL) or `en` (English STL) | `en`          |
| `step7Import.symbolListFormat`       | Symbol table format:`json`, `xlsx`, or `csv`            | `json`        |
| `step7Import.comBatchSize`           | Blocks per COM API batch during source generation (1–100)    | `10`          |

---

## Commands

| Command                                  | Description                                           |
| ---------------------------------------- | ----------------------------------------------------- |
| `Step7: Open Project`                  | Open a `.s7p` project file                          |
| `Step7: Close Project`                 | Close the current project                             |
| `Step7: Import All`                    | Import all blocks for a program                       |
| `Step7: Import All Programs`           | Import all programs in the project                    |
| `Step7: Import Block`                  | Import a single block                                 |
| `Step7: Import Selected Blocks`        | Import multiple selected blocks (Ctrl+Click in tree)  |
| `Step7: Import Block Folder`           | Import all blocks of a type (OB, FB, FC, DB…)        |
| `Step7: Import Symbol Table`           | Import the symbol table                               |
| `Step7: Import Watch Tables`           | Import watch/variable tables                          |
| `Step7: Import Hardware Configuration` | Import HW config for all stations or a single station |
| `Step7: Generate AWL Source`           | Generate AWL source for a single block via COM API    |
| `Step7: Generate All AWL Sources`      | Generate AWL sources for all blocks via COM API       |
| `Step7: Refresh Project`               | Refresh the project tree                              |
| `Step7: Show Logs`                     | Open the extension output channel                     |
| `Step7: Open Settings`                 | Open extension settings page                          |
| `Step7: Toggle Export Format`          | Switch between AWL and AWL+JSON                       |
| `Step7: Toggle Mnemonic Language`      | Switch between German (AWL) and English (STL)         |
| `Step7: Toggle Symbolic Names`         | Toggle symbolic name resolution                       |
| `Step7: Toggle System Blocks`          | Toggle system block visibility                        |
| `Step7: Toggle Structure JSON`         | Toggle `.struct.json` generation                    |
| `Step7: Toggle Show Deleted`           | Toggle deleted block visibility                       |
| `Step7: Toggle Know-How Protected`     | Toggle know-how protected block export                |
| `Step7: Prepare Workspace`             | Scaffold workspace (`.github/`, template files)     |
| `Step7: Show Modified Blocks`          | Show changed blocks before export                     |
| `Step7: Export to Step7`               | Export selected workspace content back to Step7       |
| `Step7: Export via SIMATIC Manager`    | Export selected workspace content via SIMATIC Manager |
| `Step7: Export Symbol Table via SIMATIC Manager` | Export `_symbols.json` or `_symbols.csv` back to SIMATIC Manager |

---

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      VS Code Extension                       │
│                                                              │
│  ┌────────────┐  ┌──────────────┐  ┌───────────────────────┐│
│  │  Commands   │  │  Providers   │  │      Utilities        ││
│  │ (import/    │  │ (tree view,  │  │ (logger, config,      ││
│  │  export)    │  │  connection) │  │  statusBar, workspace)││
│  └──────┬─────┘  └──────┬───────┘  └───────────────────────┘│
│         │               │                                    │
│  ┌──────▼───────────────▼───────────────────────────────────┐│
│  │               Services Layer                             ││
│  │  step7Bridge · step7Project · blockExporter              ││
│  │  hwConfigService · hwConfigExporter                      ││
│  └──────────────────────┬───────────────────────────────────┘│
│                         │  stdin/stdout JSON-RPC             │
└─────────────────────────┼────────────────────────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────────┐
│                  Step7Bridge (.NET 10.0)                       │
│                                                              │
│  Program.cs ─► Handlers/                                     │
│                  ├── ProjectHandler.cs (libnodave)            │
│                  ├── HardwareHandler.cs (HW config)           │
│                  └── Step7ApiExporter.cs (COM API)            │
│                                                              │
│            libnodave: direct S7 file access                   │
│            Step7 COM API: SIMATIC Manager automation          │
└──────────────────────────────────────────────────────────────┘
```

The extension spawns `Step7Bridge.exe` as a child process, communicating via **JSON-RPC over stdin/stdout**. The bridge reads Step7 project files using **libnodave** for fast block extraction and optionally uses the **Step7 COM API** (SIMATIC Manager automation interface) for full AWL source generation.

---

## Support and Feedback

- Source repository: [cmariusz/Step7.ExtVScode](https://github.com/cmariusz/Step7ImportExport.VSEx)
- Issue tracker: [GitHub Issues](https://github.com/cmariusz/Step7ImportExport.VSExt/issues)
- Marketplace identifier: `MariuszCzyrnek.step7-import`

If you hit an import/export issue, include the Step7 version, whether SIMATIC Manager is installed, the executed command, and the relevant output from **Step7: Show Logs**.

---

## Third-Party Notices

Third-party dependency and redistribution notes are documented in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

---

## Siemens Disclaimer

This extension is an independent project and is **not affiliated with, endorsed by, or sponsored by Siemens**.

All Siemens product names, trademarks, and registered trademarks are the property of their respective owners and are used only to describe interoperability.

---

## Disclaimer of Liability

The extension is a development and automation tool, and all imports/exports modify engineering data at your own risk.

The author is not liable for any direct or indirect damages, production downtime, data loss, project corruption, safety incidents, or other consequences resulting from changes made to Step7 / SIMATIC Manager projects using this extension.

Users are fully responsible for validating, testing, and approving all generated or imported changes before deployment to real machines, production lines, or safety-related systems.

---

## Community — Share Your Scripts & Ideas

This extension scaffolds a workspace-ready `.github/copilot-instructions.md` file that teaches AI assistants how to work with exported AWL/STL files and Step7 project structures.

**We encourage you to contribute!** If you have created useful scripts, automation tools, or improvements to the Copilot instructions:

1. **Fork** the [Step7.ExtVScode](https://github.com/cmariusz/Step7ImportExport.VSExt) repository on GitHub
2. Propose improvements to the export structure, documentation templates, or `.github/copilot-instructions.md`
3. Include a short usage note or example when contributing automation helpers or workspace templates
4. **Open a Pull Request** — your contribution will help the Step7 + VS Code community

Every shared script or instruction improves the experience for all users. Don't hesitate to share even small utilities — they often save the most time!

---

## License

[MIT](LICENSE) — Copyright (c) 2026 Mariusz Czyrnek

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for bundled dependency notices relevant to redistribution.
