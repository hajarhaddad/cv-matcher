import fitz  # PyMuPDF
from analyse_pdf import analyse_resume_gemini

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

pdf_path = "resume.pdf"

# Try to read the PDF, give a clear error if it's missing
try:
    resume_content = extract_text_from_pdf(pdf_path)
except Exception as e:
    print(f"❌ Error reading PDF: {e}")
    print("Make sure 'resume.pdf' is in the exact same folder as this script!")
    exit()

job_description = """We are looking for a skilled software engineer with experience in Python, machine learning, and cloud computing. The ideal candidate should have a strong background in data analysis, algorithm design, and software development. Experience with TensorFlow, PyTorch, and AWS is a plus. The candidate should also have excellent communication skills and the ability to work in a team environment."""

print("Analyzing resume... Please wait. This usually takes about 5-10 seconds.")

# Call the AI function
try:
    result = analyse_resume_gemini(resume_content, job_description)
    print("\n" + "="*40)
    print("       RESUME ANALYSIS RESULT       ")
    print("="*40)
    print(result)
except Exception as e:
    print(f"\n❌ An error occurred with the AI: {e}")