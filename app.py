import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)
st.set_page_config(
    page_title="Gemini AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 Gemini AI Code Reviewer")
st.markdown("Review source code using Google's Gemini AI")

st.divider()

language = st.selectbox(
    "💻 Select Programming Language",
    [
        "Python",
        "C",
        "C++",
        "Java",
        "JavaScript",
        "TypeScript",
        "C#",
        "Go",
        "Rust",
        "Ruby",
        "PHP",
        "R",
        "Swift",
        "Kotlin",
        "SQL",
        "HTML",
        "CSS",
        "Other"
    ]
)
uploaded_file = st.file_uploader(
    "📂 Upload Source Code",
    type=[
        "py", "c", "cpp", "h", "hpp",
        "java", "js", "ts", "cs",
        "go", "rs", "rb", "php",
        "r", "swift", "kt", "sql",
        "html", "css", "xml", "json",
        "yaml", "yml"
    ]
)

code = ""

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    st.success("✅ File Uploaded Successfully")

    st.code(code)

else:
    code = st.text_area(
        "✍️ Paste Your Source Code",
        height=350,
        placeholder="Paste your code here..."
    )

st.divider()
if st.button("🚀 Review Code", use_container_width=True):

    if not code.strip():
        st.warning("Please upload or paste code first.")
        st.stop()

    prompt = f"""
You are a senior software engineer and expert {language} code reviewer.

Review the following {language} code.

Provide your answer using Markdown.

# Sections

## 1. Bugs

Explain possible bugs.

## 2. Security Issues

Explain security vulnerabilities.

## 3. Performance Improvements

Suggest optimizations.

## 4. Best Practices

Suggest coding improvements.

## 5. Readability

Comment on readability.

## 6. Time Complexity

Estimate complexity if applicable.

## 7. Space Complexity

Estimate memory usage if applicable.

## 8. Code Quality Score

Give score out of 10.

## 9. Summary

Summarize the review.

Code:

{code}
"""

    with st.spinner("🤖 Gemini is reviewing your code..."):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success("✅ Review Completed")

            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error:\n\n{e}")

st.divider()

st.caption("Made with ❤️ using Streamlit + Gemini AI")
