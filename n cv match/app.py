import streamlit as st
import fitz  # PyMuPDF
from analyse_pdf import analyse_resume_gemini

# Configure the page settings
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")

# --- CUSTOM FUNCTION TO READ UPLOADED PDF ---
def extract_text_from_uploaded_pdf(uploaded_file):
    # Read the file directly from memory
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# --- APP INTERFACE ---
st.title("📄 AI Resume Matcher")
st.write("Upload a resume and provide a job description to see if the candidate is a good fit.")

# 1. File Uploader for the Resume
uploaded_file = st.file_uploader("Upload Resume (PDF format)", type=["pdf"])

# 2. Text Box for Job Description
job_description = st.text_area("Paste the Job Description here:", height=200, 
                               placeholder="We are looking for a software engineer with...")

# 3. Analyze Button
if st.button("🔍 Analyze Resume", type="primary"):
    
    # Check if both inputs are provided
    if uploaded_file is None:
        st.error("⚠️ Please upload a resume PDF first.")
    elif not job_description.strip():
        st.error("⚠️ Please paste a job description.")
    else:
        # Show a loading spinner while the AI thinks
        with st.spinner("Analyzing resume... This usually takes 5-10 seconds."):
            try:
                # Extract text from the uploaded PDF
                resume_content = extract_text_from_uploaded_pdf(uploaded_file)
                
                # Send to Gemini
                result = analyse_resume_gemini(resume_content, job_description)
                
                # Display the result in a nice box
                st.success("Analysis Complete!")
                st.subheader("📊 Results")
                
                # st.markdown allows the AI's bolding, bullet points, and formatting to show up properly
                st.markdown(result) 
                
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")


                