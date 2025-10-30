# Changelog

All notable changes to BMAD Skills will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.1] - 2025-11-15

### Changed
- Synchronized README and Makefile messaging with the current automated test suite and documented the manual conversational QA flow.
- Simplified development commands by removing references to deprecated E2E npm scripts.

### Documentation
- Updated onboarding guidance to point contributors to `tests/WHY_NO_E2E_TESTS.md` for the manual regression checklist.

## [2.2.0] - 2025-10-30

### Added
- **Development Infrastructure**: Complete Makefile for bootstrap and common tasks
- **CLI Integration Tests**: 8 comprehensive tests validating installation, backup, and validation
- **Full Workflow Test**: End-to-end bash script testing complete installation flow
- **CI/CD Integration Tests Job**: Automated CLI validation in GitHub Actions
- **Consolidated Audit Documentation**: AUDIT-COMPLET.md providing complete audit trail
- **Development Setup Section**: Comprehensive onboarding guide in README

### Changed
- **Test Scripts**: Reorganized npm scripts - removed non-existent E2E tests, added integration tests
- **CLAUDE.md**: Updated with manual conversational testing strategy, removed obsolete E2E automation claims
- **Version Synchronization**: All manifests, package.json, and Python scripts now at 2.2.0

### Fixed
- **CLI Test Mode**: Added BMAD_TEST_MODE environment variable to allow testing from repo
- **MANIFEST Parsing**: Fixed skill iteration to handle both string and object formats
- **Integration Test Reliability**: Tests now pass consistently with proper environment setup

### Documentation
- Clarified that conversational E2E tests are manual, not automated
- Added references to `.project-archive/TESTING.md` for test strategy
- Moved individual audit files to `.project-archive/` for cleaner root

## [2.1.9] - 2025-10-30

### Added
- 73 unit tests for Python tooling (workflow_status, activation_metrics, sprint_status)
- 62% code coverage with pytest-cov
- Structured logging module (logger.py) with color-coded output
- SHA256 checksums for bundle verification
- CI/CD workflows (test.yml, release.yml)
- Atomic installation with 5-stage validation and automatic rollback

### Changed
- Migrated activation_metrics.py from print() to structured logging
- Enhanced bin/cli.js with validation, backup, and rollback features

## [2.1.5] - 2025-10-30

### Fixed
- Critical bug: MANIFEST.json missing version field at root
- Removed unused execSync import from bin/cli.js
- Documentation for PyYAML requirement

## [2.1.0] - 2025-10-29

### Added
- Initial public release on npm
- 12 integrated skills (BMAD + OpenSpec workflows)
- Complete conversational activation system
- CLI installation tool
- Comprehensive documentation

[2.2.1]: https://github.com/bacoco/bmad-skills/compare/v2.2.0...v2.2.1
[2.2.0]: https://github.com/bacoco/bmad-skills/compare/v2.1.9...v2.2.0
[2.1.9]: https://github.com/bacoco/bmad-skills/compare/v2.1.5...v2.1.9
[2.1.5]: https://github.com/bacoco/bmad-skills/compare/v2.1.0...v2.1.5
[2.1.0]: https://github.com/bacoco/bmad-skills/releases/tag/v2.1.0
