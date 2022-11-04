import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Text Summarizer" ,layout="wide", page_icon=":books:")
st.header("Text Summarizer")
st.subheader("Summarize your text in a few clicks")

text = st.text_area("Enter Text Here")

if st.button("Summarize"):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=400, min_length=250, do_sample=False)
    summary = summary[0]['summary_text']
    st.write(summary)
