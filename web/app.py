import sys
import os

# Add the parent directory to Python's search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from main.summarizer import extractive_summary, abstractive_summary

st.title("📝 AI-Powered Text Summarizer")

text_input = st.text_area("Enter text to summarize:")
method = st.selectbox("Choose summarization method", ["Abstractive", "Extractive"])

if st.button("Summarize"):
    if method == "Abstractive":
        summary = abstractive_summary(text_input)
    else:
        summary = extractive_summary(text_input)

    st.write("### Summary:")
    st.write(summary)
