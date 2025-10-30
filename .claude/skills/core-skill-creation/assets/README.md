# Assets Directory - core-skill-creation

## Purpose

This directory contains reference template files for skill creation. Note that current scripts use inline templates with Python's string.Template (stdlib) rather than these Jinja2 files.

## Available Templates (Reference Only)

### skill-template.md.jinja
Reference template showing the structure for SKILL.md files with proper frontmatter, structure, and metadata.

**Note**: `init_skill.py` uses an inline Python template instead of this file.

### validation-report-template.md.jinja
Reference template for skill validation reports showing the structure for validation output.

**Note**: `quick_validate.py` performs validation directly without using template files.

### package-manifest-template.json.jinja
Reference template for package manifests when bundling skills for distribution.

**Note**: `package_skill.py` generates manifests programmatically.

## Current Implementation

The core-skill-creation scripts use Python's stdlib `string.Template` with inline templates for zero-dependency operation, rather than loading external Jinja2 templates. The .jinja files in this directory serve as documentation and reference examples.
