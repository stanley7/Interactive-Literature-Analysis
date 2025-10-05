import re
from google import genai

# Initialize client with API key
client = genai.Client(api_key="")

def extract_abstract(text):
    match = re.search(r"(?i)abstract(.+?)(\n\s*\n|introduction|1\.|I\.)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text[:1500]

def summarize_paper(text):
    try:
        content = extract_abstract(text)
        prompt = (
            "Summarize the following research paper abstract in 3-5 sentences, "
            "focusing on the main findings and contributions. Ignore author names and affiliations.\n\n"
            + content
        )
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp", 
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def extract_contributions(text):
    try:
        content = extract_abstract(text)
        prompt = (
            "List the main contributions and novel ideas of the following research paper as bullet points. "
            "Ignore author names and affiliations.\n\n"
            + content
        )
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def answer_question(text, question):
    try:
        content = extract_abstract(text)
        prompt = f"{question}\n\nPaper Abstract:\n{content}"
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
