import json

from src.exporters import SECTION_TITLES, packet_to_json, packet_to_markdown
from src.logic import create_field_packet


def test_json_export_returns_valid_json_with_required_keys():
    packet, _ = create_field_packet("Patched with TPO.")
    data = json.loads(packet_to_json(packet))

    assert data["customer_facing_draft"]["warning"]
    assert "missing_information" in data


def test_markdown_export_includes_required_sections():
    packet, _ = create_field_packet("Patched with TPO.")
    markdown = packet_to_markdown(packet)

    for title in SECTION_TITLES:
        assert f"## {title}" in markdown
