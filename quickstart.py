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
          {"role": "system", "content": ("You are a file search assistant, which will take a user query and get all the possible keywords from that, which will be used in a file search."
                                         "Final Output will be comma seperated keyword list."
                                         "If the user Query is directly a file name only then just return that only no keywords required for that."
                                         "If Query seems to be regex type then consider that return regex keyword basd on that")},
          {"role": "user", "content": "All payslips files"},
          {"role": "assistant", "content": "payslips.pdf, payslips.docx, salary"},
          {"role": "user", "content": "All files ending with .csv"},
          {"role": "assistant", "content": "*.csv"},
          {"role": "user", "content": "Resume.pdf"},
          {"role": "assistant", "content": "Resume.pdf"},
          {"role": "user", "content": "All Payslip docs"},
          {"role": "assistant", "content": "*payslip.pdf, *payslip.doc, *payslip.csv, *payslip, *Payslip, *payslips"},
          {"role": "user", "content": user_query}
      ]
  )

  return response.choices[0].message.content