# actions-guard

<div align="center">
  <img src="assets/banner.svg" alt="actions-guard project banner" width="100%"/>
  <br/>
  ![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
  ![Status](https://img.shields.io/badge/Status-Early%20Development-F59E0B?style=for-the-badge)
</div>

> Audit GitHub Actions workflow files for risky permissions, unpinned actions, and common trust-boundary mistakes.

## Why it exists

A focused, inspectable starter for a real developer workflow. It favors explicit behavior, local execution, and small pieces that are easy to understand and extend.

## Features

- Finds missing explicit permissions blocks
- Flags third-party actions not pinned to full commit SHAs
- Warns about pull_request_target and persisted checkout credentials
- Supports a single workflow file or a workflow directory

## Architecture

```mermaid
flowchart LR
  A[Local input] --> B[actions-guard]
  B --> C[Validation and core logic]
  C --> D[Readable report]
  C --> E[CI exit status]
```

## Requirements

- Python 3.10+ / standard library
- A terminal and a local checkout of this repository

## Quick start

```bash
python src/actions_guard.py .github/workflows/
```

## Example

```bash
python src/actions_guard.py .github/workflows/build.yml
```

## Project status and limitations

This repository contains an initial working implementation, not a production-certified product. Review the source and test it against your own fixtures before adopting it in critical workflows.

This is a lightweight text-based audit, not a complete YAML parser. Review workflow context and untrusted inputs manually.

## Roadmap

- [ ] Parse YAML with an optional strict mode
- [ ] Add reusable-workflow permission analysis
- [ ] Emit SARIF for code scanning

## Contributing

Issues and pull requests are welcome. Include a small reproducible example for bug reports, keep changes focused, and add tests for new behavior. Do not submit secrets or private data.

## License

MIT. See [LICENSE](LICENSE). Third-party services or optional dependencies remain subject to their own terms.
