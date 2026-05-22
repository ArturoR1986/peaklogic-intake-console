from src.models import REVIEW_WARNING
from src.packet_builder import build_field_packet, build_metadata


def create_field_packet(
    raw_field_note: str,
    job_name: str = "",
    address: str = "",
    date: str = "",
    foreman: str = "",
    crew: str = "",
):
    metadata = build_metadata(
        job_name=job_name,
        address=address,
        date=date,
        foreman=foreman,
        crew=crew,
    )
    packet = build_field_packet(raw_field_note, metadata)
    return packet.to_dict(), REVIEW_WARNING
