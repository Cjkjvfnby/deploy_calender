"""
CSS injection.

Based on:
https://discuss.streamlit.io/t/creating-a-nicely-formatted-search-field/1804/2?u=cjkjvfnby
"""
from pathlib import Path

import streamlit as st


def add_local_css(file_path: Path) -> None:
    with file_path.open() as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)
