import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key  # Import the API key from the apikey.py file

# Initialize the Google Generative AI API with the imported API key
genai.configure(api_key=google_gemini_api_key)

# Streamlit Interface
st.title("ASK AI 👣")

# Get user input (question)
user_input = st.text_input("Ask a question:")

# Define a function to handle the chat session and responses
def get_ai_response(question):
    """Fetch response from Google Generative AI for a given question."""
    try:
        # Ensure the question is not empty
        if not question.strip():
            raise ValueError("Question cannot be empty. Please enter a question.")

        # Define model generation configuration
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "max_output_tokens": 2048,
            "response_mime_type": "text/plain",
        }

        # Start a chat session with the user's question
        chat_session = genai.ChatModel(model="models/text-bison-001").start_chat(
            context="You are an AI designed to provide detailed answers to any question."
        )

        # Send the user's question to the model
        response = chat_session.send_message(
            question,
            generation_config=generation_config
        )

        return response.text

    except ValueError as e:
        # Raise validation errors
        raise e

    except Exception as e:
        # Catch unexpected errors
        raise RuntimeError(f"An error occurred while fetching the AI response: {str(e)}")

# Handle user interaction
if st.button("Get Answer"):
    try:
        # Get AI-generated response
        ai_response = get_ai_response(user_input)

        # Display the answer on the Streamlit app
        st.subheader("Answer:")
        st.write(ai_response)

    except ValueError as ve:
        # Handle validation errors
        st.error(str(ve))
    except RuntimeError as re:
        # Handle runtime errors
        st.error(str(re))
    except Exception as e:
        # Handle any other unexpected errors
        st.error(f"An unexpected error occurred: {str(e)}")
