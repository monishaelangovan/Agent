import streamlit as st
import cohere
import os

# === Set up Cohere Client ===
# Get API key from environment variable
api_key = os.getenv("COHERE_API_KEY")

# Show error and stop if not found
if not api_key:
    st.error("Cohere API key not found. Please set the COHERE_API_KEY environment variable.")
    st.stop()

# Initialize Cohere client
co = cohere.Client(api_key)

# === Function to get response from Cohere ===
def get_cohere_response(question):
    response = co.generate(
        model='command',  # Available models: 'command', 'command-light', etc.
        prompt=question,
        max_tokens=100,
        temperature=0.5
    )
    return response.generations[0].text.strip()

# === Streamlit App Interface ===
st.set_page_config(page_title="Q&A with Cohere")
st.title("❓ Ask Me Anything")
st.write("Enter a question below, and I'll generate a response using Cohere's language model.")

# Input field and button
input_text = st.text_input("Your question:", key="input")
submit = st.button("Get Answer")

# Display response
if submit and input_text:
    with st.spinner("Thinking..."):
        response = get_cohere_response(input_text)
    st.subheader("💬 Response")
    st.write(response)
