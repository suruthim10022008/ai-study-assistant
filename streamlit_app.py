import streamlit as st

st.set_page_config(page_title="AI Study Assistant", page_icon="🤖")

st.title("🤖 AI Study Assistant")
st.write("Your personal study helper")

question = st.text_area(
    "📚 Enter your question:",
    placeholder="Example: What is Machine Learning?"
)

if st.button("✨ Ask AI"):
    if question:
        st.info("Your question is ready! AI answer feature will be connected next.")
    else:
        st.warning("Please enter a question.")
