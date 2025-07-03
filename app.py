import streamlit as st
from transformers import pipeline
def local_css(file_name):
  
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the HuggingFace GPT-2 model
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

# Streamlit app layout
st.title(" AI Story Generator")
prompt = st.text_area("Enter your story prompt:")

if st.button("Generate Story"):
    with st.spinner("Crafting your story... ✨"):
        story = generator(prompt, max_length=250, num_return_sequences=1)[0]['generated_text']
        st.write(story)

