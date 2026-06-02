# Third-Party Notices

This project includes third-party components. Redistribution of this extension should preserve the applicable third-party license notices and terms.

> Informational notice: this file is a practical compliance aid and not legal advice.

## Project License

- This project source code is licensed under MIT (see `LICENSE`).

## Runtime dependencies (Node.js)

- No runtime npm dependencies are declared in `package.json`.
- Packaging and development tooling dependencies (`typescript`, `eslint`, `@vscode/vsce`, `@types/*`) are used to build the extension and are not required by end users at runtime.

## .NET bridge dependencies (NuGet)

- `DotNetProjects.DotNetSiemensPLCToolBoxLibrary` (4.4.9)
  - Used by `Step7Bridge` for reading Step7 project structures and block data.
  - The exact redistribution obligations should be verified against the package license metadata and upstream project terms before publication.

## Bundled runtime components

- `Step7Bridge.exe` and its .NET runtime files are bundled with the VS Code extension package.
- `Step7ComHelper` is published as a self-contained x86 helper to communicate with the 32-bit Step7 COM automation layer.

## Siemens software dependency notice

- Some features require a locally installed Siemens SIMATIC Manager / Step7 environment.
- This extension does not grant any Siemens license rights; end users remain responsible for their own valid Siemens software licenses.

## Recommended compliance checklist

- Keep this `THIRD_PARTY_NOTICES.md` file in source control and packaged artifacts.
- Preserve the project `LICENSE` file.
- Re-check dependency licenses before each Marketplace release, especially after updating NuGet packages or bundling additional runtime files.
- Verify whether any transitive dependencies of `DotNetProjects.DotNetSiemensPLCToolBoxLibrary` introduce extra notice requirements.

## Audit basis (current snapshot)

- Node.js metadata from `package.json`.
- NuGet references from `dotnet/Step7Bridge/Step7Bridge.csproj` and `dotnet/Step7ComHelper/Step7ComHelper.csproj`.