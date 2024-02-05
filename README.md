# ATS Scanner Web App

## Overview

The **ATS Scanner Web App** is a tool designed to streamline the resume scanning process for job applications. This application allows users to input a job description, upload a resume in PDF format, and then analyze the resume for relevance to the provided job description. Additionally, users can calculate the **percentage match** between the job description and the resume content.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- **Python 3.6 or higher**
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

The **ATS Scanner Web App** is a valuable tool for recruiters and hiring managers looking to efficiently review and match resumes to specific job requirements. By leveraging advanced language models, the app aims to save time and improve the accuracy of the candidate selection process.

Feel free to contribute, report issues, or suggest enhancements to make this tool even more powerful!
