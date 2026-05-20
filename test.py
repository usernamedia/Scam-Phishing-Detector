from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

# local email path 
path = r"C:\Users\emoking\Downloads\sample-1.eml"

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    email_content = f.read()

llm = ChatOllama(
    model="llama3",
    temperature=0
)

prompt = f"""
You are a cybersecurity scam/phishing detection system.

Analyze this email and determine the likelihood
that it is a scam/phishing attempt.

Return EXACTLY in this format:

Safe /Suspicious /Scam
Your reasoning here

Email:

{email_content}
"""

response = llm.invoke([HumanMessage(content=prompt)])

result = response.content

print("\n=== PHISHING ANALYSIS ===\n")
print(result)
