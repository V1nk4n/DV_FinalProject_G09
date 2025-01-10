import streamlit as st
from openai import OpenAI
import os
import pandas as pd

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

# Chatbot Function
def chatbot_response(prompt):
    # Gọi OpenAI API
    completion  = client.chat.completions.create(
        model="gpt-4o-mini",  # Thay bằng model bạn muốn sử dụng
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


# Streamlit UI
st.title("Chatbot OpenAI + Power BI Dashboard")
st.subheader("Hỏi chatbot hoặc tương tác với dashboard!")

# User input
user_input = st.text_input("Nhập câu hỏi:")
if user_input:
    with st.spinner("Chatbot đang xử lý..."):
        response = chatbot_response(user_input)
    st.text_area("Chatbot trả lời:", response, height=200)

# Embed Power BI Dashboard using iframe
st.markdown("""
<iframe title="G09_Jobs_Dashboard" width="100%" height="600" 
src="https://app.powerbi.com/reportEmbed?reportId=d2b4ae58-4015-4704-9482-208c58f38f19&autoAuth=true&embeddedDemo=true" 
frameborder="0" allowFullScreen="true"></iframe>
""", unsafe_allow_html=True)
