---
applyTo: "**"
description: "CMsoft Import for Step7 - Siemens Step7 V5.7 projects in the workspace: AWL / STL source format, block structure, CLI, rules"
---
<!-- cmsoft:managed step7-import - Prepare Workspace of CMsoft Import for Step7 updates this file; delete this line to keep your own version -->
# Copilot Instructions for Siemens Step7 V5.7 Projects

## Project Description

The file `.github/ProjectDescription.md` contains a comprehensive description of the project architecture, communication software structure, library blocks, protocols, and data flow. It is shared with the other add-ons of the workspace — keep their parts.

The functional description of automation systems should provide the developer with a clear and detailed understanding of what the system is supposed to do and what are the requirements to achieve this. It should also provide guidance on how the system should be designed and implemented to effectively meet these requirements.

**Rule:** The project description should include:

1. General description of the system.
2. Detailed functional requirements for devices controlled by the automation system taking into account the technological division into objects (e.g. pump, valve, measurement) or groups of objects with the full structure of nesting objects, the so-called "plant hierarchy".
3. The object description should include:
   - a brief description of the operation of the facility,
   - operating modes,
   - in automatic mode, the algorithm for developing commands controlling an object (if applicable to a single object or a reference to the description of control of a larger group of objects),
   - description of interlocks with logic (e.g. for start, operation, opening, closing etc.)
   - handling of errors and exceptions,
   - control method with HMI
4. The automatic operation of a group of objects should be described with the same requirements as for individual objects. In addition, the object control algorithm should clearly describe how the system is to be controlled (settings, emergency situations, calculations, performance requirements, control loops etc.)
5. In case of sequences of activities, the following should be described:
   - starting conditions, interruptions of sequences with logic,
   - description of sequence steps with the commands for a given step,
   - conditions for transitions between steps with logic,
   - the sequence should be represented graphically.
6. Data exchange interfaces between systems

**Always** consult this file for context when answering questions about the project.

## Step7 CLI Automation

The file `.github/instructions/step7-import-cli.instructions.md` describes how to control the CMsoft Import for Step7 extension through the local CLI bridge. Use it when preparing the workspace, opening Step7 projects, importing blocks, exporting changes to SIMATIC Manager, or reading diagnostics from an AI agent or external script.

**Rule:** Before using CLI automation, **always** consult `.github/instructions/step7-import-cli.instructions.md` and follow its safety rules. Never hard-code the bridge port or token; read `.step7/cli.json` for each automation run.

**Rule:** Prefer CLI commands over UI-only workflows when acting as an automation agent. Use `prepare_workspace` before creating project-specific files, then use `open_project`, `import_project`, `import_program`, or `import_blocks` according to the required scope.

**Rule:** When CLI automation fails or returns incomplete context, use `get_logs` / `step7_get_logs` to fetch recent entries from the CMsoft Import for Step7 Output channel before retrying or changing files.

**Rule:** When making changes that affect the project structure, architecture, communication logic, block hierarchy, message definitions, or data block layout, **always** update `.github/ProjectDescription.md` to reflect those changes. This includes:

- Adding, removing, or renaming program blocks (FB, FC, OB, DB, UDT)
- Changing message IDs, data structures, or communication channels
- Modifying the call hierarchy or adding new communication channels
- Changes to library blocks

**Rule:** If `.github/ProjectDescription.md` is empty, still the template text or does not exist, and you are analyzing the project's software structure (e.g. reviewing program blocks, communication logic, library blocks, or data flow), **always** generate and populate `ProjectDescription.md` with a comprehensive description of the project before proceeding.

**Rule:** When creating or updating `ProjectDescription.md`, **always** include **Mermaid diagrams** (````mermaid`) to visually illustrate key aspects of the project. At minimum, include diagrams for:

- **Architecture overview** — block/folder dependencies and relationships (use `graph TD`)
- **Communication channel topology** — MPI, Profibus, Ethernet connections, ports (use `graph LR`)
- **Call hierarchy** — OB → FB → FC call tree (use `graph TD`)
- **Data flow / sequence diagrams** — message send/receive sequences for each communication direction (use `sequenceDiagram`)
- **State machines** — for blocks with complex internal state logic (use `stateDiagram-v2`)
- **Data structures** — for key UDT/message layouts (use `packet-beta` or `block-beta`)
- **Queue/scheduling logic** — for FIFO managers or priority systems (use `flowchart LR`)

Place each diagram **directly above or below** the corresponding textual description it illustrates. Keep text descriptions alongside diagrams — diagrams supplement, not replace, the text.

---

## Project Directories

### `Step7Export/`

Exported project, mirroring SIMATIC Manager hierarchy:

- `Step7Export/<Project>/<Station>/<CPU>/<Program>/Blocks/<TYPE>/` — the block sources (`<symbol>_<block>.awl` / `.scl`, plus `.meta.json` / `.struct.json` in the `awl+json` format); **these are the working copies to edit**
- `Step7Export/<Project>/<Station>/<CPU>/<Program>/Sources/` — sources generated by SIMATIC Manager ("Generate AWL Source")
- `Step7Export/<Project>/<Station>/<CPU>/<Program>/_symbols.csv` — the symbol table (or `.json` / `.xlsx`)
- `Step7Export/<Project>/<Station>/HWconfig/_hwconfig.json` — the hardware configuration of the station

### `Tools/`

Directory with utility scripts for the project (Python, PowerShell, etc.). Each script has a corresponding `.md` file with a description, usage examples, and dependencies.

**Rule:** When creating a new script, **always** place it in `Tools/` and create a matching `.md` description file (e.g. `Tools/_myScript.py` + `Tools/_myScript.md`).

### `UserFiles/`

Directory for user-generated output files produced by scripts from `Tools/` (Excel reports, CSV exports, logs, etc.). Scripts should write their default output here.

## File Structure

- `.awl` files contain AWL/STL source code for PLC blocks (FB, FC, DB, OB, UDT)
- `.scl` files contain SCL (Structured Control Language) source code
- `.meta.json` files contain block metadata (author, version, timestamps, dependencies)
- `.struct.json` files contain DB/UDT data structure definitions as JSON
- `.source-hashes.json` (one per folder) holds the hash of each source as last imported from Step7 or last exported to it — the baseline of "modified" and of what an import may overwrite; do not edit it
- `_symbols.json` / `_symbols.csv` contain the complete symbol table mapping symbolic names to addresses
- `Blocks/VAT/*.json` files contain watch/variable tables
- `Sources/*.awl` files are formatted for import back into SIMATIC Manager

## Step7 V5.7 AWL Source File Format

AWL (Anweisungsliste / Statement List) is the text-based programming language for Siemens S7-300/400.

### Mnemonic Languages

Files may use German (AWL) or English (STL) mnemonics:

| German (AWL) | English (STL) | Description        |
| ------------ | ------------- | ------------------ |
| U            | A             | AND                |
| O            | O             | OR                 |
| UN           | AN            | AND NOT            |
| ON           | ON            | OR NOT             |
| =            | =             | Assign             |
| S            | S             | Set                |
| R            | R             | Reset              |
| L            | L             | Load               |
| T            | T             | Transfer           |
| SPA          | JU            | Jump unconditional |
| SPB          | JC            | Jump conditional   |
| AUF          | OPN           | Open data block    |
| CALL         | CALL          | Call block         |
| ZV           | CU            | Counter Up         |
| ZR           | CD            | Counter Down       |
| E            | I             | Input              |
| A            | Q             | Output             |
| M            | M             | Memory             |
| DB           | DB            | Data Block         |
| FB           | FB            | Function Block     |
| FC           | FC            | Function           |
| OB           | OB            | Organization Block |

### Data Types

| Type          | Size     | Description            |
| ------------- | -------- | ---------------------- |
| BOOL          | 1 bit    | Boolean                |
| BYTE          | 8 bit    | Unsigned byte          |
| WORD          | 16 bit   | Unsigned word          |
| DWORD         | 32 bit   | Unsigned double word   |
| INT           | 16 bit   | Signed integer         |
| DINT          | 32 bit   | Signed double integer  |
| REAL          | 32 bit   | Floating point         |
| TIME          | 32 bit   | Time value             |
| DATE          | 16 bit   | Date value             |
| TIME_OF_DAY   | 32 bit   | Time of day            |
| DATE_AND_TIME | 64 bit   | Date and time combined |
| STRING        | variable | Character string       |
| STRUCT        | variable | Structure              |
| ARRAY         | variable | Array of elements      |

### Memory Areas

| Prefix (DE/EN) | Area       | Description               |
| -------------- | ---------- | ------------------------- |
| E / I          | Inputs     | Process inputs (Eingang)  |
| A / Q          | Outputs    | Process outputs (Ausgang) |
| M / M          | Flags      | Markers/flags (Merker)    |
| DB             | Data Block | Global data               |
| L              | Local      | Temp variables            |
| T              | Timers     | Timer values              |
| Z / C          | Counters   | Counter values            |

Address format (German mnemonics):

- `E` = Input, `A` = Output, `M` = Memory
- `EB`/`AB`/`MB` = Byte, `EW`/`AW`/`MW` = Word, `ED`/`AD`/`MD` = DWord
- `DB` = Data Block, `FB`/`FC`/`OB` = Code blocks
- `T` = Timer, `Z` = Counter

### Block Types

| Type | Description           | Typical Use                                                           |
| ---- | --------------------- | --------------------------------------------------------------------- |
| OB   | Organization Block    | System entry points (OB1 = main cycle, OB35 = 100ms, OB100 = startup) |
| FB   | Function Block        | Reusable logic with instance data (state machines, regulators)        |
| FC   | Function              | Stateless logic (calculations, conversions)                           |
| DB   | Data Block            | Global data storage                                                   |
| UDT  | User Data Type        | Reusable structure definitions                                        |
| SFB  | System Function Block | Built-in S7 blocks (SFB0..SFB65535)                                   |
| SFC  | System Function       | Built-in S7 functions (SFC0..SFC65535)                                |

### AWL Source Structure

```
FUNCTION_BLOCK FB10
TITLE = Motor Control
// Block description comment
AUTHOR : ENGR
NAME : MotCtrl
VERSION : 1.0

VAR_INPUT
  Start : BOOL;
  Stop : BOOL;
END_VAR

VAR_OUTPUT
  Running : BOOL;
  Fault : BOOL;
END_VAR

VAR
  SR_Latch : BOOL;
END_VAR

VAR_TEMP
  temp1 : INT;
END_VAR

BEGIN
NETWORK
TITLE = Start/Stop Logic
// RS flip-flop for motor control
      U     #Start;
      S     #SR_Latch;
      U     #Stop;
      R     #SR_Latch;
      U     #SR_Latch;
      =     #Running;

END_FUNCTION_BLOCK
```

### Data Block Source Structure

```
DATA_BLOCK DB10
TITLE = Motor Data
AUTHOR : ENGR
NAME : MotData
VERSION : 1.0
  STRUCT
    Speed : INT := 0;
    Temperature : REAL := 0.0;
    Status : BOOL := FALSE;
    Name : STRING[32] := '';
    Config : UDT1;
  END_STRUCT
BEGIN
  Speed := 1500;
  Temperature := 20.5;
END_DATA_BLOCK
```

### Instance Data Block

```
DATA_BLOCK DB20
TITLE = Motor 1 Instance
FB10
BEGIN
  Start := FALSE;
  Stop := FALSE;
END_DATA_BLOCK
```

## Symbol Table

The symbol table maps absolute addresses to symbolic names:

| Symbol       | Address | Data Type | Comment               |
| ------------ | ------- | --------- | --------------------- |
| Motor1_Start | E0.0    | BOOL      | Motor 1 start button  |
| Motor1_Stop  | E0.1    | BOOL      | Motor 1 stop button   |
| Motor1_Run   | A0.0    | BOOL      | Motor 1 contactor     |
| Speed_SP     | MW10    | INT       | Speed setpoint        |
| MotorCtrl    | FB10    | FB10      | Motor control block   |
| MotorData    | DB10    | FB10      | Motor 1 instance DB   |

## Key Validation Rules

1. Every FB call (`CALL FB10, DB20`) must have a matching instance DB
2. Block numbers must be unique within their type
3. UDT references in DBs must exist
4. Parameter types in CALL statements must match the FB/FC interface
5. Symbolic names must match the symbol table entries
6. Timer/Counter numbers are limited by CPU type (e.g. S7-315: T0–T255, Z0–Z255)
7. Local data (TEMP) is not retained between OB cycles
8. OB1 is mandatory — it is the main cyclic program
9. STAT variables in FB are retained in the instance DB
10. Array indices in Step7 V5.7 start from user-defined lower bound (commonly 0 or 1)

## Editing and Re-import

Edit the block files in `Blocks/`. The CMsoft Import for Step7 extension sends them back:

- **Step7: Show Modified Blocks** lists the blocks changed since the last import or export. A new block written into `Blocks/<TYPE>/` counts as modified, so the export creates it.
- **Step7: Export via SIMATIC Manager** (Copilot: `step7_export_to_simatic`, `step7_fix_compile_errors`) imports the modified blocks into the open Step7 project and compiles them, in dependency order. Compile errors appear in the Problems view with their line, and the previous version of a block that fails is put back in Step7. Blocks that use a block that failed are not sent until it compiles.
- **Step7: Export to Step7** writes an AWL package to `Step7Export/<Project>/ExportPackage/` for a manual import.
- System blocks (SFB, SFC, SDB) are never exported - their sources are for reference only.
- An import from Step7 (*Only changed*, the default of the tools) keeps the sources changed in the workspace and reports them as *kept*; it never deletes a block written in the workspace that is not in Step7 yet. Only *Overwrite all* (`overwriteAll: true`) replaces workspace changes with the Step7 version.

A manual import in SIMATIC Manager:

1. Open the Step7 project in SIMATIC Manager
2. Navigate to the S7 Program → Sources
3. Import the .awl file via "Insert Object → External Source"
4. Compile the source to generate the block

**Rule:** Validate every change in SIMATIC Manager before it is downloaded to a PLC.

**Rule:** Generated and changed code is the user's responsibility: never claim it is verified or safe to run, and remind the user to review and test it before it is exported into SIMATIC Manager or downloaded to a PLC.

**Rule:** Safety programs (F-blocks of an F-CPU): never export or compile them unless the user confirms that the change was independently reviewed - checked by a qualified person other than the one who made it.
