import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key  # Import the API key from the apikey.py file

# Initialize the Google Generative AI API with the imported API key
genai.configure(api_key=google_gemini_api_key)

# Define model generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

# Create the model object
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)

# Streamlit Interface
st.title("ASK AI👣")

# Get user input (question)
user_input = st.text_input("Ask a question:")

# Create a chat session and get a response when the user submits a question
if st.button("Get Answer"):
    try:
        # Check if the user_input is empty
        if not user_input.strip():
            raise ValueError("Question cannot be empty. Please enter a question.")

        # Start the chat session with the initial user question
        chat_session = model.start_chat(
            history=[
                {"role": "user", "parts": [f"give me the big answer for whatever is asked\nquestion = {user_input}"]}
            ]
        )
        
        # Send the question as a message to the model
        response = chat_session.send_message(user_input)

        # Display the answer on the Streamlit app
        st.subheader("Answer:")
        st.write(response.text)

    except ValueError as e:
        # If the question is empty, show an error message
        st.error(str(e))
    
    except Exception as e:
        # Catch any other unexpected errors
        st.error(f"An error occurred: {str(e)}")
