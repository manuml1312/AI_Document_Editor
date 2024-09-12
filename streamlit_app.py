import streamlit as st
from docx import Document
from openai import OpenAI


# from openai import OpenAI
your_api_key=st.secrets.api_key
client=OpenAI(api_key=your_api_key)

edit_styles=['Basic','Standard','Pro']
# Streamlit UI
st.title("Text Editor")

# if st.button('Generate'):
style = st.selectbox("Select the style of the tattoo", edit_styles)

# if st.button("Edit Image"):
uploaded_file=st.file_uploader("Upload the text document to process.",type=["docx","pdf","csv"],key='orig')

edits = st.multiselect('Select three known variables:',['A','B','C'])

if st.button('Edit Text'):
  document = Document(uploaded_file)
  text=''
  for i in document.paragraphs:
    text+=i.text
  prompt=f'Correct any grammatical issues in the provided text.The provided text is:{text}'
  res = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",  # Choose the appropriate OpenAI GPT engine
      max_tokens=1028,
       messages=[
        {"role": "system", "content": """You are AI Assistant.Do as asked."""},
      {"role": "user", "content": str(prompt)}])
  response=dict(dict([dict(res)][0]['choices'][0])['message'])['content']
  st.write(response)



