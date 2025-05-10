import streamlit as st
import cohere

# Initialize Cohere client with your API key
co = cohere.Client('wZ4UKDzrLDLjyocfH0o6pAqGZkAd6VWJansdFqMc')  # Replace with your actual key

# Function to get study material or tips based on the subject/topic
def get_study_material(topic):
    # Use the Cohere API to generate study material based on the given topic
    response = co.generate(
        model='command-r-plus',  # Use 'command-r' or 'command-r-plus' as available
        prompt=f"Provide study material and tips for the topic: {topic}",
        max_tokens=500  # You can adjust the token limit as needed
    )
    
    return response.generations[0].text.strip()

# Streamlit User Interface
st.title('Study Scout Agent')
st.write("Enter a topic or subject, and get personalized study material and tips!")

# Input the study topic from the user
topic = st.text_input("Enter the topic or subject you need help with:")

# Generate study material when the user clicks the button
if st.button('Get Study Material'):
    if topic:
        study_material = get_study_material(topic)
        st.write("Study Material and Tips:\n")
        st.write(study_material)
    else:
        st.write("Please enter a subject or topic to get study material!")
