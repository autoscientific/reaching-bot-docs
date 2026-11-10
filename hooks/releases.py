"""Renders data/app-releases.yml into the app downloads page.

The release workflow in autoscientific/reaching-bot-app appends one entry to
that YAML per published tag. Keeping the data separate from the prose means a
release changes a structured file rather than editing Markdown by hand — a
one-entry diff a reviewer can read, and nothing to get wrong in a regex.

MkDocs calls this through the `hooks:` key in mkdocs.yml. It replaces the
`<!-- app-releases -->` marker wherever it appears.
"""

from __future__ import annotations

import os

import yaml

MARKER = "<!-- app-releases -->"
DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "app-releases.yml")

_NO_RELEASES = """!!! warning "No published build yet"
    There is no published release of the ReachingBot app, so there is nothing
    to download from here yet. Ask
    [info@autoscientific.co.uk](mailto:info@autoscientific.co.uk) for a build in
    the meantime.
"""


def _render(data: dict) -> str:
    releases = data.get("releases") or []
    if not releases:
        return _NO_RELEASES

    base = (data.get("base_url") or "").rstrip("/")
    out: list[str] = []
    for i, release in enumerate(releases):
        version = release.get("version", "")
        heading = f"## ReachingBot app {version}"
        if i == 0:
            heading += " { .latest }"
        out.append(heading)
        out.append("")

        date = release.get("date")
        notes = release.get("notes")
        if date:
            out.append(f"*Released {date}*")
            out.append("")
        if notes:
            out.append(notes)
            out.append("")

        files = release.get("files") or []
        if files:
            out.append("| Download | Size |")
            out.append("| --- | --- |")
            for item in files:
                url = f"{base}/{version}/{item['filename']}"
                size = item.get("size", "")
                out.append(f"| [{item['label']}]({url}) | {size} |")
            out.append("")
    return "\n".join(out)


def on_page_markdown(markdown: str, **_kwargs) -> str:
    if MARKER not in markdown:
        return markdown
    with open(DATA) as handle:
        data = yaml.safe_load(handle) or {}
    return markdown.replace(MARKER, _render(data))
