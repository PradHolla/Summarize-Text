import streamlit as st
from transformers import pipeline
from summarizer import Summarizer, TransformerSummarizer

st.set_page_config(page_title="Text Summarizer" ,layout="wide", page_icon=":books:")
st.header("Text Summarizer")

st.sidebar.header("Summarizer")
st.sidebar.subheader("Select the summarizer you want to use")
summarizer = st.sidebar.selectbox("Summarizer", ("XLNet Summarizer", "BERT Summarizer","GPT 2","Hugging Face"))

text = st.text_area("Enter Text Here")

if st.button("Summarize"):
    if summarizer == "XLNet Summarizer":
        model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
        summary = model(text)

    elif summarizer == "BERT Summarizer":
        model = Summarizer()
        summary = model(text)

    elif summarizer == "GPT 2":
        GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
        summary = ''.join(GPT2_model(text, min_length=60))
        
    elif summarizer == "Hugging Face":
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=200, min_length=200, do_sample=False)
        summary = summary[0]['summary_text']
    st.write(summary)