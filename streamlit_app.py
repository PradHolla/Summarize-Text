import streamlit as st
from transformers import pipeline
from summarizer import Summarizer, TransformerSummarizer

st.set_page_config(page_title="Text Summarizer" ,layout="wide", page_icon=":books:")
st.header("Text Summarizer")

st.sidebar.header("Summarizer")
st.sidebar.subheader("Select the summarizer you want to use")
summarizer = st.sidebar.selectbox("Summarizer", ("t5-base","Hugging Face"))

text = st.text_area("Enter Text Here")

if st.button("Summarize"):
    if summarizer == "t5-base":
        GPT2_model = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        summary = GPT2_model(text, max_length=400, min_length=250, do_sample=False)
        summary = summary[0]['summary_text']


    elif summarizer == "Hugging Face":
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=400, min_length=250, do_sample=False)
        summary = summary[0]['summary_text']
    st.write(summary)