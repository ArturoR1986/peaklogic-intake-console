import streamlit as st

from src.logic import create_field_packet
from src.exporters import packet_to_json, packet_to_markdown
from src.sample_loader import load_sample_text

st.set_page_config(page_title="PeakLogic Roofing Field Intake Console", layout="wide")

st.title("PeakLogic Roofing Field Intake Console")
st.caption("Local v0.1 Streamlit MVP. The field packet is a reviewable output, not a final customer report.")

with st.sidebar:
    st.header("Job Metadata")
    job_name = st.text_input("Job name")
    address = st.text_input("Address")
    date = st.text_input("Date")
    foreman = st.text_input("Foreman")
    crew = st.text_input("Crew")
    if st.button("Load sample"):
        st.session_state["raw_note"] = load_sample_text()

raw_note = st.text_area(
    "Paste messy roofing field update",
    key="raw_note",
    height=240,
    placeholder="Paste foreman notes, voice transcript text, WhatsApp-style updates, or photo comments...",
)

if st.button("Generate Reviewable Field Packet", type="primary"):
    packet, _ = create_field_packet(
        raw_note,
        job_name=job_name,
        address=address,
        date=date,
        foreman=foreman,
        crew=crew,
    )
    markdown = packet_to_markdown(packet)
    json_text = packet_to_json(packet)

    st.subheader("Reviewable Field Packet")
    st.warning(packet["customer_facing_draft"]["warning"])

    tab_packet, tab_markdown, tab_json = st.tabs(["Packet", "Markdown", "JSON"])
    with tab_packet:
        st.json(packet)
    with tab_markdown:
        st.markdown(markdown)
        st.download_button("Download Markdown", markdown, "field_packet.md", "text/markdown")
    with tab_json:
        st.code(json_text, language="json")
        st.download_button("Download JSON", json_text, "field_packet.json", "application/json")
