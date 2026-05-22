from pathlib import Path


def load_sample_text(path: str = "sample_data/messy_foreman_updates.md") -> str:
    return Path(path).read_text(encoding="utf-8")
