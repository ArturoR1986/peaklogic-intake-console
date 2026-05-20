import json
import sqlite3
from pathlib import Path
from typing import List, Dict

DB_PATH = Path("data/intake_records.db")


def init_db(db_path: Path = DB_PATH) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS intake_records (
            intake_id TEXT PRIMARY KEY,
            date_created TEXT NOT NULL,
            status TEXT NOT NULL,
            payload_json TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def save_packet(packet: Dict, db_path: Path = DB_PATH) -> None:
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.execute(
        "INSERT OR REPLACE INTO intake_records (intake_id, date_created, status, payload_json) VALUES (?, ?, ?, ?)",
        (packet["intake_id"], packet["date_created"], packet["status"], json.dumps(packet)),
    )
    conn.commit()
    conn.close()


def list_packets(db_path: Path = DB_PATH) -> List[Dict]:
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT payload_json FROM intake_records ORDER BY date_created DESC").fetchall()
    conn.close()
    return [json.loads(row[0]) for row in rows]
