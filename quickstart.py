import os
from openai import AzureOpenAI

def generate_keywords(user_query):
  client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01"
  )

  response = client.chat.completions.create(
      model="FileSearch", # model = "deployment_name".
      messages=[
          {"role": "system", "content": "You are a file keyword generator assistant, which will take a user query and get all the possible keywords from that, which will be used in a file search. Final Output will be comma seperated keyword list"},
          {"role": "user", "content": "All payslips files"},
          {"role": "assistant", "content": "keywords: [payslips.pdf, payslips.docx, salary, etc..]"},
          {"role": "user", "content": user_query}
      ]
  )

  return response.choices[0].message.content