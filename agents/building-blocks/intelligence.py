from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
def llm_call(prompt: str) -> str:
    # Initialize the OpenAI client with default settings
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[{"role": "user", "content": prompt}]
    )
    return response.output_text

if __name__ == "__main__":
    result  = llm_call("What is Machine Learning ?")
    print("LLM response: " + result)