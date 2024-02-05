# ATS Scanner Web App

## Overview

The **ATS Scanner Web App** is a powerful tool designed to streamline the resume scanning process for job applications. This application offers a range of features to assist recruiters and hiring managers in efficiently evaluating resumes. The key features include:

1. **Percentage Match:** Calculate the percentage match between a given job description and an uploaded resume.

2. **Missing Keywords Analysis:** Identify keywords that are missing in the resume concerning the provided job description.

3. **Skills Improvement Suggestions:** Receive personalized suggestions on how to improve skills based on the content of the resume.

4. **Resume Overview:** Quickly gather essential information about a resume, including skills, experience, and education.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- **Python 3.9 or higher**
- **Streamlit:** Install using `pip install streamlit`

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/ats-scanner-web-app.git
    cd ats-scanner-web-app
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    streamlit run app.py
    ```

4. Access the application in your web browser at `http://localhost:8501`.

## Google Gemini API and LLM Model

This application utilizes the **Google Gemini API** and its **LLM (Large Language Model)** for analyzing and extracting information from resumes. Please ensure you have the necessary credentials or API keys from Google Gemini to access the API.

## Future Scope

- **Enhanced Resume Analysis:** Continuously improve the resume analysis algorithm to provide more accurate and detailed insights.
  
- **User Authentication:** Implement user authentication to manage multiple users and provide a personalized experience.

- **Integration with ATS Systems:** Explore integration possibilities with popular **Applicant Tracking Systems (ATS)** for seamless recruitment workflows.

## Usefulness

The **ATS Scanner Web App** is a valuable tool for recruiters and hiring managers. Its multifaceted features allow users to not only match resumes with job descriptions but also receive insights on missing keywords, skill improvement suggestions, and a quick overview of resumes. By leveraging advanced language models, the app aims to save time and improve the accuracy of the candidate selection process.

Feel free to contribute, report issues, or suggest enhancements to make this tool even more powerful!
