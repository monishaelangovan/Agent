import streamlit as st
import cohere

# Initialize Cohere client with your API key
co = cohere.Client('wZ4UKDzrLDLjyocfH0o6pAqGZkAd6VWJansdFqMc')  # Replace with your actual key

# Function to get book recommendations
def get_book_recommendations(preferences):
    # Use the Cohere API to generate book recommendations based on the user's preferences
    response = co.generate(
        model='command-r-plus',  # You can use 'command-r' or 'command-r-plus'
        prompt=f"Suggest me books based on the following preferences: {preferences}",
        max_tokens=500  # You can adjust the token limit
    )
    
    return response.generations[0].text.strip()

# Streamlit User Interface
st.title('Book Recommendation Agent')
st.write("Enter your book preferences, and get personalized book recommendations!")

# Input preferences from the user
preferences = st.text_input("Enter your preferences (e.g., genre, mood, authors, or themes):")

# Generate recommendations when the user clicks the button
if st.button('Get Book Recommendations'):
    if preferences:
        recommendations = get_book_recommendations(preferences)
        st.write("Recommended Books:\n")
        st.write(recommendations)
    else:
        st.write("Please enter some preferences!")