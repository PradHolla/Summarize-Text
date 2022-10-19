#Text summarization app
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Text Summarizer" ,layout="wide", page_icon=":books:")
st.header("Text Summarizer")

# Creating a summarizer object
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Creating a text input box
text = st.text_area("Enter Text Here")

# Creating a button
if st.button("Summarize"):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    st.write(summary[0]['summary_text'])
