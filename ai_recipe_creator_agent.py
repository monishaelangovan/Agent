import cohere

# Initialize Cohere client with your API key
co = cohere.Client('Qvfrotinw2WTuoDjfD4Kzqi8gLDSEQdVv6i5gjym')  # Replace with your actual API key

# Get ingredients from user
ingredients = input("Enter the ingredients (comma separated): ")

# Ask Cohere to create a recipe
response = co.chat(
    model='command-r-plus',
    message=f"Give me a detailed recipe using these ingredients: {ingredients}",
)

# Print the recipe
print("\nGenerated Recipe:\n")
print(response.text.strip())

