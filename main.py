import streamlit as st
import ollama

st.title("Local AI Markdown Generator")

prompt = st.text_area("Enter your prompt:")
if st.button("Generate Markdown"):
    if prompt:
        response = ollama.chat(model="your_model", messages=[{"role": "user", "content": prompt}])
        markdown_output = response['message']['content']
        st.markdown(markdown_output)
        st.code(markdown_output, language="markdown")
    else:
        st.warning("Please enter a prompt.")
