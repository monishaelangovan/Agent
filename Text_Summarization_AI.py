import cohere
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env (recommended for security)
load_dotenv()

# Get API key from environment OR fallback to hardcoded one
api_key = os.getenv("CO_API_KEY", "DqrKSstNCyHoS4ZH8BW8eOTLR5yDbMpNOeiRslJO")  # Put your key in .env ideally

# Show message based on API key availability
if not api_key:
    st.error("Cohere API key not found. Please set CO_API_KEY in your .env file or use a hardcoded value.")
    st.stop()
else:
    st.success("API key loaded successfully!")

# Initialize Cohere client
cohere_client = cohere.Client(api_key)

# Streamlit UI
st.title("Text Generation using Cohere")

user_input = st.text_input("Enter your prompt:")

if user_input:
    with st.spinner("Generating..."):
        try:
            response = cohere_client.generate(
                prompt=user_input,
                max_tokens=100
            )
            st.success("Response:")
            st.write(response.generations[0].text)  # Show actual generated text
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
