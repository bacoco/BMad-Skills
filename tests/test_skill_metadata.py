import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "meta" / "MANIFEST.json"


def parse_frontmatter(raw: str) -> dict:
    frontmatter: dict[str, object] = {}
    for line in raw.strip().splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            frontmatter[key] = ""
            continue
        if value.startswith("[") and value.endswith("]"):
            # Evaluate simple JSON-style arrays used in allowed-tools definitions.
            frontmatter[key] = json.loads(value.replace("'", '"'))
        else:
            frontmatter[key] = value
    return frontmatter


def load_skill_data():
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        manifest = json.load(f)

    skills = []
    for entry in manifest.get("skills", []):
        skill_path = REPO_ROOT / entry["path"]
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            raise FileNotFoundError(f"Missing SKILL.md for {entry['id']} at {skill_md}")

        content = skill_md.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) < 3:
            raise ValueError(f"Invalid frontmatter format for {skill_md}")
        _, frontmatter_raw, body = parts
        frontmatter = parse_frontmatter(frontmatter_raw)
        skills.append((entry, frontmatter, body))
    return skills


SKILL_DATA = load_skill_data()
SKILL_IDS = [entry["id"] for entry, _, _ in SKILL_DATA]


@pytest.mark.parametrize("entry, frontmatter, _", SKILL_DATA, ids=SKILL_IDS)
def test_allowed_tools_alignment(entry, frontmatter, _):
    assert "allowed-tools" in frontmatter, f"{entry['id']} is missing allowed-tools in SKILL.md"
    assert frontmatter["allowed-tools"] == entry["allowed-tools"], (
        f"allowed-tools mismatch for {entry['id']}: SKILL.md has {frontmatter['allowed-tools']}, "
        f"but MANIFEST.json has {entry['allowed-tools']}"
    )


@pytest.mark.parametrize("entry, frontmatter, _", SKILL_DATA, ids=SKILL_IDS)
def test_version_alignment(entry, frontmatter, _):
    assert "version" in frontmatter, f"{entry['id']} is missing version in SKILL.md"
    assert frontmatter["version"] == entry["version"], (
        f"Version mismatch for {entry['id']}: SKILL.md has {frontmatter['version']}, "
        f"but MANIFEST.json has {entry['version']}"
    )


@pytest.mark.parametrize("entry, _, body", SKILL_DATA, ids=SKILL_IDS)
def test_when_to_invoke_section(entry, _, body):
    assert "## When to Invoke" in body, f"{entry['id']} is missing a '## When to Invoke' section"
