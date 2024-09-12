import streamlit as st
from docx import Document
from openai import OpenAI
import os
import pickle
import requests

# from openai import OpenAI
API_KEY=st.secrets.api_key
API_URL = 'https://api.openai.com/v1/chat/completions'

# Load instructions from a file
def load_instructions(filename):
    """ Load editing instructions from a file. """
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return "Default instructions if file doesn't exist."

# Save instructions to a file
def save_instructions(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def read_docx(file_path):
    """ Extract text from DOCX file. """
    doc = Document(file_path)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def process_text_with_api(text, instructions):
    # global instructions
    messages = [
        {"role": "system", "content": instructions},
        {"role": "user", "content": text}
    ]
    """ Call the OpenAI API with the extracted text and instructions. """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'model': 'gpt-4-turbo',
        'messages':messages,
        'max_tokens': 1024,
        'temperature': 0.7,
        'top_p': 1,
        'frequency_penalty': 0,
        'presence_penalty': 0
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return "An error occurred: " + response.text

def process_document(filename, options,report_features,edits):
    """ Read the DOCX file, process the text with loaded instructions and additional features, call the API. """
    text = read_docx(filename)
    instructions = load_instructions(edit_config[options])
    combined_text = instructions + " " + " ".join([report_features[feature] for feature in edits])
    # st.write(combined_text)
    return process_text_with_api(text, combined_text) 

#################################################################
# Define the path for instruction files
edit_config = {
    "Standard": 'standard.pkl',
    "Developmental": 'developmental.pkl',
    "ProofReading": 'proofreading.pkl'
}
# Report features for additional processing options
report_features = {
    "aspects of research": """State the novelty, contributions, relevance, findings, practical implications, future scope of research and limitations of this research (30-50 words for each point).""",
    "research_gaps": """Identify the gaps in information presented in the current article in terms of novelty, methodology details, contributions, relevance, findings, practical implications, future scope, and limitations. Check if these aspects of information are explicitly stated in the Abstract (all), Introduction (existing research gap, motivation, rationale for methodology, hypotheses and possible contribution), Methodology (reproducibility), Results (findings), Discussion (data interpretation, contribution, relevance, limitations), and Conclusions section (all).""",
    "synopsis": """Write a synopsis/plain language summary for this study based on the following guidelines: The rationale/motivation/problem statement behind the study and the reason behind the chosen line of investigation. The aim/purpose of the study and the intended outcome. A brief summary of the methodology employed in simple language with the techniques highlighted. The key results obtained from the study and the inferences that can be drawn. The major conclusions drawn from the study. The implications of the study results in the area of research and the industry problem that can be targeted through these results (if applicable).""",
    "highlights": """Outline key highlights. Make five separate points, each for the novelty, contributions, relevance, findings, and practical implications into complete sentences of 10-12 words as Highlights of the research (within 85 characters including spaces).""",
    "title": """Suggest a concise and descriptive title between 10-12 words that incorporates the key content/topics and highlights the main novelty/impact/contribution in the simplest & most comprehensive manner. Max length: 15 words.""",
    "keywords": """Extract significant keywords that represent the current research topic and could be classified as relevant keywords to improve the discoverability of the present topic.""",
    "cover_letter": """Write a cover letter addressed to a journal editor succinctly pitching the main objective, motivation (research gap addressed), methodology, contributions, relevance, key findings, and practical implications of this study."""
}
# Streamlit UI
st.title("Text Editor")

edit_styles=['Standard','Developmental','ProofReading']
style = st.selectbox("Select the type of editing", edit_styles)

uploaded_file=st.file_uploader("Upload the text document to process.",type=["docx","pdf","csv"],key='orig')
edits = st.multiselect('Select required options:',report_features)

if st.button('Edit Text'):
    response=process_document(uploaded_file,style,report_features,edits)
    st.write(response)
