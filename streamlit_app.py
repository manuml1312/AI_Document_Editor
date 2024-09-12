import streamlit as st
from openai import OpenAI

edit_styles=['Basic','Standard','Pro']
# Streamlit UI
st.title("Text Editor")

# if st.button('Generate'):
style = st.selectbox("Select the style of the tattoo", edit_styles)

# if st.button("Edit Image"):
uploaded_file=st.file_uploader("Upload the text document to process.",type=["docx","pdf","csv"],key='orig')

edits = st.multiselect('Select three known variables:',['A','B','C'])

st.button('Edit Text')
