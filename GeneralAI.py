import streamlit as st
from google import genai
st.markdown(
    """
    <h1 style='text-align: center;'>AI Assistant</h1>
    <p style='text-align: center; font-size:18px;'>
        Ask any question. 1Shoe is here for you!
    </p>
    """,
    unsafe_allow_html=True,
)
jarvis = genai.Client(api_key=st.secrets["MY_API"])
mychat = jarvis.chats.create(model = "gemini-flash-lite-latest") #to hold the history of conversation
#Placeholder for the response
response_placeholder = st.empty()
question = st.text_input(" ", placeholder="Enter your question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
    send = st.button ("Send")

if send:
    response = mychat.send_message(question)
    st.write(response.text)
