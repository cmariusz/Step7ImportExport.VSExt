# Third-Party Notices

This project includes third-party components. Redistribution of this extension should preserve the applicable third-party license notices and terms.

> Informational notice: this file is a practical compliance aid and not legal advice.

## Project License

- CMsoft Import for Step7 3.0.0 and later is proprietary commercial software licensed under the End User License Agreement (see `LICENSE.md`). Versions before 3.0.0 were released under the MIT License.
- The third-party components listed below keep their own licenses; the EULA does not limit the rights they grant.

## Runtime dependencies (Node.js)

- No runtime npm dependencies are declared in `package.json`.
- Packaging and development tooling dependencies (`typescript`, `eslint`, `@eslint/js`, `typescript-eslint`, `mocha`, `ts-node`, `@vscode/vsce`, `@types/*`) are used to build and test the extension and are not required by end users at runtime.

## .NET bridge dependencies (NuGet)

- `DotNetProjects.DotNetSiemensPLCToolBoxLibrary` (4.4.9)
  - Used by `Step7Bridge` for reading Step7 project structures and block data.
  - The exact redistribution obligations should be verified against the package license metadata and upstream project terms before publication.
- `System.Management` (8.0.0), `System.Security.Cryptography.ProtectedData` (8.0.0) and their dependency `System.CodeDom` (8.0.0) — Microsoft, MIT License
  - Used by `Step7Bridge` for the license check (hardware fingerprint via WMI, DPAPI-protected license store).
- `System.Text.Json` (10.0.12) and its dependencies `Microsoft.Bcl.AsyncInterfaces`, `System.Buffers`, `System.IO.Pipelines`, `System.Memory`, `System.Numerics.Vectors`, `System.Runtime.CompilerServices.Unsafe`, `System.Text.Encodings.Web`, `System.Threading.Tasks.Extensions` — Microsoft, MIT License
  - Used by `Step7ComHelper` for its JSON messages to `Step7Bridge`.

## Bundled runtime components

- `Step7Bridge.exe` and its library DLLs are bundled with the VS Code extension package; it runs on the locally installed .NET 10 runtime.
- `Step7ComHelper.exe` is an x86 helper for the 32-bit Step7 COM automation layer. It runs on the .NET Framework 4.8 built into Windows, so no .NET runtime is bundled.

## Siemens software dependency notice

- Some features require a locally installed Siemens SIMATIC Manager / Step7 environment.
- This extension does not grant any Siemens license rights; end users remain responsible for their own valid Siemens software licenses.

## Recommended compliance checklist

- Keep this `THIRD_PARTY_NOTICES.md` file in source control and packaged artifacts.
- Preserve the End User License Agreement (`LICENSE.md`).
- Re-check dependency licenses before each Marketplace release, especially after updating NuGet packages or bundling additional runtime files.
- Verify whether any transitive dependencies of `DotNetProjects.DotNetSiemensPLCToolBoxLibrary` introduce extra notice requirements.

## Audit basis (current snapshot)

- Node.js metadata from `package.json`.
- NuGet references from `dotnet/Step7Bridge/Step7Bridge.csproj` and `dotnet/Step7ComHelper/Step7ComHelper.csproj`.