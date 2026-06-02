# Change Log

All notable changes to the **Step7 Import/Export** extension will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.114] - 2026-04-30

### Added

- **Single COM session for all blocks** — Phase 2 (COM API upgrade) now generates all block sources in one COM session instead of spawning a separate `Step7ComHelper.exe` process per block, dramatically reducing import time for large programs
- **Per-block progress reporting** — VS Code progress bar now shows which blocks are being generated during COM source generation
- **AWL source splitter** — if COM API returns a multi-block AWL file, it is automatically split into individual block sources
- **Graceful fallback** — if COM session fails, the extension automatically falls back to per-block process spawning

### Changed

- **Progress pipeline** — progress notifications from .NET COM helper flow through the full chain (ComHelper → ComHelperProcess → Bridge → VS Code progress bar)

---

## [1.0.0] - 2026-04-01

### Added

- **Import Hardware Configuration** — read station HW config (CPUs, CPs, network interfaces, Profibus/Profinet master systems) from Step7 projects
- **Per-station HW export** — import HW config for a single station via inline icon on station nodes, or all stations from the project node
- **HWconfig directory** — exported to `Step7Export/<Project>/<Station>/HWconfig/_hwconfig.json`
- **Dedicated HW services** — separate `HardwareHandler` (C#), `HwConfigService` and `HwConfigExporterService` (TypeScript)

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
- **.NET Bridge** — `Step7Bridge.exe` (JSON-RPC over stdin/stdout) using libnodave and Step7 COM API
