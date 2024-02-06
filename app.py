from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import io
import pdf2image
import base64

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        # Take the first page for simplicity, or loop through images for all pages
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

# st.set_page_config(page_title="Resume Expert")
# Set page title and description
st.set_page_config(
    page_title="Resume Expert",
    page_icon="✨",
    layout="wide"
)

st.header("Your own AI ATS Scanner😎")
# st.subheader('This Application helps you in your Resume Review with help of GEMINI AI [LLM]')

# Navigation bar
st.sidebar.title("Resume Review by GOOGLE.")
st.sidebar.markdown("---")

input_text = st.text_input("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your Resume(PDF)...", type=["pdf"])
pdf_content = ""

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("What are the Keywords That are Missing")

submit4 = st.button("Percentage match")

input_prompt1 = """
You are an Technical Human Resource Manager with expertise in all the software related fields that exists and also have experience of a FAANG level recruiter, your task is to review the provided resume.
Please share your professional evaluation on whether the candidate's profile is good from the perspective of FAANG standard or not. 
The output should not include word "FAANG".
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements and provide feedback.
Please make a note that whatever suggestions/strengths/weakness you provide it should only be based on the content of the resume and the response should be more of a technical.
"""

input_prompt2 = """
You are an Technical Human Resource Manager with expertise in all the software related fields that exists and also have experience of a FAANG level recruiter, 
Your task is to scrutinize the resume and provide the candidate with a roadmap on strengthening his/her skills in the field which he/she is most experienced in which can be understood from his/her resume, also the roadmap should be concise and crisp and should also contain links of few courses/articles and youtubers which are renowned and most rated in tutorials for that particular field.
The output should not include word "FAANG".
The most important thing is your response should be irrespective of the job description provided and it should be related to TECHNICAL ASPECTS only.
There should be no name mentioned in the response at all.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of all fields of software which currently exists and ATS functionality, and also have experience of a highly experienced recruiter.
Your task is to evaluate the resume against the provided job description. As a Human Resource manager,assess the compatibility of the resume with the role. Give me a list of upto 10 keywords which are missing in the candidate's resume when compared with the provided job description.
The output should not include word "FAANG".
While matching the name of technologies between provided job description and resume, make sure you ignore case sensitive matching, for example: CSS and Css are same, also ignore any special characteristic mismatch for example: ""Node.js", "NodeJS" and "Node"" all are SAME.
"""
input_prompt4 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of all fields of software which currently exists and ATS functionality and also have experience of a FAANG level recruiter, 
Your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches the job description. First the output should come as percentage and then upto top 5 keywords missing and last final thoughts as well as strengths and weaknesses strictly related to job description.
While matching the name of technologies between Job Description and resume content, make sure you ignore case sensitive matching, example: CSS and Css are same, also ignore any special characteristic mismatch for example: Node.js and NodeJS is same.
Also the first line of output that is percentage should have a keyword saying Percentage Match or something like that, should be bold and bigger in fontsize as compared to whole response and after percentage the output should start on a new line.
The output should not include word "FAANG".
The content shouldnt be in bold except the headers and it should be properly and neatly formatted.
"""


if submit1:
    if uploaded_file is not None:
        with st.spinner("Fetching data..."):
            pdf_content = input_pdf_setup(uploaded_file)
            if input_text is not None:
                response = get_gemini_response(input_prompt1, pdf_content, input_text)
            else:
                response = get_gemini_response(input_prompt1, pdf_content, "null")
            st.subheader("The Highlight of the resume is:")
            st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit2:
    if uploaded_file is not None:
        with st.spinner("Fetching data..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt2, pdf_content, input_text)
            st.subheader("The Recommendation is:")
            st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit3:
    if uploaded_file is not None:
        with st.spinner("Fetching data..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
            st.subheader("The Missing Keywords are:")
            st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit4:
    if uploaded_file is not None:
        with st.spinner("Fetching data..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt4, pdf_content, input_text)
            st.subheader("The match is:")
            st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")


st.markdown("---")
st.caption("Resume Expert - Making Job Applications Easier")