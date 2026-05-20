import json

import streamlit as st

from src.database import list_packets
from src.logic import create_field_packet

st.title("PeakLogic Intake Console v0.1")
st.caption("Review surface only. Human approval required before customer use.")

raw_note = st.text_area("Raw field note", height=180)

if st.button("Generate field packet"):
    packet, warning = create_field_packet(raw_note)
    packet["review_warning"] = warning
    st.subheader("Structured packet")
    st.json(packet)

st.subheader("Saved records")
records = list_packets()
st.write(f"{len(records)} records")
if records:
    st.code(json.dumps(records[0], indent=2), language="json")
