import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(model="gpt-3.5-turbo", prompt="Say this is a test", temperature=0, max_tokens=7)

##print response from openai
print(response)
