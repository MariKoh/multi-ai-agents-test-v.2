import streamlit as st
import google.generativeai as genai

# Instruction
Instruction = "Act as a professional male trader who would assist answer to users' questions bases on the document provided and not use external information to provide the answers."

# Title and subheader
st.title("🐧 MariKoh Professional Trader Chatbot")
st.subheader("Conversation")

# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")

# Initialize the Gemini Model if API key is provided
if gemini_api_key:
    try:
        # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")
else:
    model = None  # Ensure model is None when API key is not provided

# Initialize session state for storing chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Start with an empty list

# Display previous chat history
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# Capture user input and generate bot response
user_input = st.chat_input("Type your message here...")

if user_input:
    # Store and display user message
    full_input = Instruction + user_input
    st.session_state.chat_history.append(("user", full_input))
    st.chat_message("user").markdown(user_input)

    # Generate bot response using Gemini AI if model is initialized
    if model:
        try:
            full_input = Instruction + user_input
            response = model.generate_content(full_input)
            bot_response = response.text

            # Store and display the bot response
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")