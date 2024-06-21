import streamlit as st
import google.generativeai as genai

# Google Gemini API setup
genai.configure(api_key="AIzaSyDl2nIaYT9ef8vJ6NDhXnIOUj-Z_UmYfXU")
model = genai.GenerativeModel("gemini-1.0-pro")
chat = model.start_chat(history=[])

# Function to generate career guidance using Gemini model
def generate_career_guidance(career_field, experience_level):
    msg = (f"Provide practical career guidance for someone interested in the field of '{career_field}' "
           f"with '{experience_level}' experience. The guidance should include: "
           f"1. A brief introduction to the career field, "
           f"2. Main skills and qualifications needed, "
           f"3. Typical career paths and job roles, "
           f"4. Recommended learning resources and certifications, "
           f"5. Networking and professional development tips, "
           f"6. Job search strategies, "
           f"7. Additional resources with hyperlinks for further reading.")
    response = chat.send_message(msg, stream=True)
    return ''.join([chunk.text for chunk in response])  # Extract the text content from the response

# Streamlit UI
st.title("Career Guidance Bot")

st.markdown("### Enter the details below to receive career guidance:")

career_field = st.text_input("Career Field or Interest")
experience_level = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Get Career Guidance"):
    if career_field and experience_level:
        career_guidance = generate_career_guidance(career_field, experience_level)
        st.markdown("### 📝 Career Guidance")
        st.markdown(career_guidance, unsafe_allow_html=True)
    else:
        st.error("Please enter both the career field and experience level.")
