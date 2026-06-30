import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")

# Safety check: Prevent the script from running if the key is missing or formatted wrong
if not api_key or not api_key.startswith("AIza"):
    print("❌ ERROR: Invalid or missing API Key in your .env file.")
    print("Please make sure your .env file contains exactly: GEMINI_API_KEY=AIzaYourRealKeyHere")
    exit()

# Initialize the new Google GenAI client
client = genai.Client(api_key=api_key)

# Configuration
configuration = types.GenerateContentConfig(
    temperature=1.0,
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
    response_mime_type="text/plain"
)

def analyse_resume_gemini(resume_content, job_description):
    prompt = f"""
    You are a professional resume analyzer.

    Resume:
    {resume_content}

    Job Description:
    {job_description}

    Task:
    - Analyze the resume against the job description.
    - Give a match score out of 100.
    - Highlight missing skills or experiences.
    - Suggest improvements.

    Return the result in structured format:
    Match Score: XX/100
    Missing Skills:
    - ...
    Suggestions:
    - ...
    Summary:
    ...
    """
    
    # Generate content using the fast and free Flash model
    response = client.models.generate_content(
        model = "gemini-3.1-flash-lite-preview",
        contents=prompt,
        config=configuration
    )
    
    return response.text