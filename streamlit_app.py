import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"{st.secrets['api_token']}"}

st.set_page_config(page_title="Text Summarizer" ,layout="wide", page_icon=":books:")
st.header("Text Summarizer")
st.subheader("Summarize your text in a few clicks")

text = st.text_area("Enter Text Here", height=300)
summarize = st.button("Summarize")

with st.sidebar:
    st.header("Summary Settings")
    st.subheader("Set the minimum and maximum no. of words of the summary")
    min_length = st.slider("Minimum Length", min_value=100, max_value=300, value=250)
    max_length = st.slider("Maximum Length", min_value=200, max_value=500, value=400)

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if text is not None and summarize:
    payload = {"inputs": text, "parameters": {"max_length": max_length, "min_length": min_length, "do_sample": False}}
    response = query(payload)
    summary = response[0]['summary_text']
    st.write(summary)