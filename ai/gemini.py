import streamlit as st
import google.generativeai as genai
import os

# Cấu hình API Key cho Gemini
genai.configure(api_key="AIzaSyAsJkBpXnoaN6cgBY6IEBw2LZ91KM2hQck")


model = genai.GenerativeModel(model_name=f'tunedModels/generate-num-9797')
# Khởi tạo model và cuộc trò chuyện
# model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Function để xử lý câu trả lời của chatbot
def chatbot_response(prompt, stream=False):
    try:
        # Gửi tin nhắn đến Gemini với streaming
        response = chat.send_message(prompt, stream=stream)
        
        if stream:
            response_text = ""
            # Dùng st.empty() để cập nhật Markdown liên tục
            response_placeholder = st.empty()
            for chunk in response:
                response_text += chunk.text
                response_placeholder.markdown(f"**Chatbot trả lời:**\n\n{response_text}")
            return response_text
        else:
            return response.text if hasattr(response, "text") and response.text else "Xin lỗi, tôi không thể trả lời câu hỏi của bạn."
    except Exception as e:
        return f"Đã xảy ra lỗi: {e}"

# Streamlit UI
st.title("HCMZooS")
st.subheader("Dashboard thị trường việc làm Việt Nam")

# Embed Power BI Dashboard using iframe
st.markdown("""
<div style="display: flex; justify-content: center;">
<iframe title="G09_Jobs_Dashboard" width="90%" height="600" 
src="https://app.powerbi.com/reportEmbed?reportId=d2b4ae58-4015-4704-9482-208c58f38f19&autoAuth=true&embeddedDemo=true" 
frameborder="0" allowFullScreen="true"></iframe>
</div>
""", unsafe_allow_html=True)

# Nhập câu hỏi
user_input = st.text_input("Nhập câu hỏi:")
if user_input:
    # Lưu câu hỏi vào lịch sử (nhưng không hiển thị)
    chat.history.append({"role": "user", "parts": user_input})
    
    # Xử lý câu trả lời từ chatbot
    with st.spinner("Chatbot đang xử lý..."):
        response = chatbot_response(user_input, stream=True)
    
    # Lưu câu trả lời vào lịch sử (nhưng không hiển thị)
    chat.history.append({"role": "model", "parts": response})


