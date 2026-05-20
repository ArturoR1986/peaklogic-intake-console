import argparse
from pathlib import Path

from src.database import save_packet
from src.export_utils import write_packet_json
from src.logic import create_field_packet


def main() -> None:
    parser = argparse.ArgumentParser(description="PeakLogic Intake Console CLI")
    parser.add_argument("--input", required=True, help="Path to raw field note text file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    raw_note = Path(args.input).read_text(encoding="utf-8").strip()
    packet, warning = create_field_packet(raw_note)
    packet["review_warning"] = warning

    write_packet_json(packet, args.output)
    save_packet(packet)

    print(f"Saved packet: {packet['intake_id']}")
    print(f"Output JSON: {args.output}")
    print(f"Review warning: {warning}")


if __name__ == "__main__":
    main()
