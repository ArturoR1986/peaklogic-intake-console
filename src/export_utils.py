from pathlib import Path
from typing import Dict

from src.exporters import packet_to_json, packet_to_markdown


def write_packet_json(packet: Dict, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(packet_to_json(packet), encoding="utf-8")


def write_packet_markdown(packet: Dict, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(packet_to_markdown(packet), encoding="utf-8")
