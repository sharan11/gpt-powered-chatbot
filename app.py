import streamlit as st
from get_response import get_response

st.set_page_config(layout="wide")  # Set the layout to wide mode
st.title("Conversational Bot")

if 'history' not in st.session_state:
    st.session_state['history'] = []

def clear_chat_history():
    st.session_state['history'] = []

user_input = st.text_input("Type your message here...", key="input", placeholder="Type here...", label_visibility="collapsed")

if st.button("Clear Chat"):
    clear_chat_history()

if user_input:
    bot_response = get_response(user_input)
    st.session_state['history'].append(f"You: {user_input}")
    st.session_state['history'].append(f"Bot: {bot_response}")

st.markdown("### Chat History")
for chat in st.session_state['history']:
    st.markdown(f"> {chat}")