import ast
import json
from pathlib import Path

import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_manifest() -> dict:
    manifest_path = REPO_ROOT / "meta" / "MANIFEST.json"
    with manifest_path.open("r", encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


def load_skill_frontmatter(skill_directory: Path) -> dict:
    skill_md_path = skill_directory / "SKILL.md"
    raw_text = skill_md_path.read_text(encoding="utf-8")
    parts = raw_text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"SKILL.md in {skill_directory} is missing YAML frontmatter delimiters")

    frontmatter_section = parts[1]
    data: dict[str, object] = {}
    for line in frontmatter_section.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        key, separator, value = stripped.partition(":")
        if not separator:
            continue
        key = key.strip()
        raw_value = value.strip()
        if not raw_value:
            data[key] = ""
            continue
        try:
            data[key] = ast.literal_eval(raw_value)
        except (ValueError, SyntaxError):
            data[key] = raw_value

    return data


class TestManifestConsistency(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = load_manifest()

    def test_allowed_tools_alignment(self) -> None:
        mismatches = []
        for skill in self.manifest["skills"]:
            skill_dir = REPO_ROOT / skill["path"]
            frontmatter = load_skill_frontmatter(skill_dir)
            if frontmatter.get("allowed-tools") != skill.get("allowed-tools"):
                mismatches.append(skill["id"])

        self.assertListEqual(
            mismatches,
            [],
            msg="Allowed tools lists must match between SKILL.md and MANIFEST.json",
        )

    def test_version_alignment(self) -> None:
        mismatches = []
        for skill in self.manifest["skills"]:
            skill_dir = REPO_ROOT / skill["path"]
            frontmatter = load_skill_frontmatter(skill_dir)
            if frontmatter.get("version") != skill.get("version"):
                mismatches.append(skill["id"])

        self.assertListEqual(
            mismatches,
            [],
            msg="Version fields must match between SKILL.md and MANIFEST.json",
        )

    def test_description_alignment(self) -> None:
        mismatches = []
        for skill in self.manifest["skills"]:
            skill_dir = REPO_ROOT / skill["path"]
            frontmatter = load_skill_frontmatter(skill_dir)
            if frontmatter.get("description") != skill.get("description"):
                mismatches.append(skill["id"])

        self.assertListEqual(
            mismatches,
            [],
            msg="Description fields must match between SKILL.md and MANIFEST.json",
        )

    def test_when_to_invoke_section_present(self) -> None:
        missing_sections = []
        for skill in self.manifest["skills"]:
            skill_md_path = REPO_ROOT / skill["path"] / "SKILL.md"
            raw_text = skill_md_path.read_text(encoding="utf-8")
            if "## When to Invoke" not in raw_text:
                missing_sections.append(skill["id"])

        self.assertListEqual(
            missing_sections,
            [],
            msg="Every skill should document a '## When to Invoke' section for auto-activation.",
        )


if __name__ == "__main__":
    unittest.main()
