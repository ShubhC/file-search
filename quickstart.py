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
          {"role": "system", "content": ("You are a File search Assistant. For this task you are given a #query# and you have to get all the possible regex keywords for that query."
                                         "Those regex keywords will be used for file search."
                                         "The file search indexing follows regex search."
                                         "The output should not be case sensitive code will handle that just return regex"
                                         "Generate all possible regex for a given query not only one mentioned in examples"
                                         "Final Output will be comma seperated keyword list.")},
          {"role": "user", "content": "All payslips files"},
          {"role": "assistant", "content": "*payslip.pdf, *payslip.doc, *payslip.csv, *payslip, *payslips, payslip, payslips"},
          {"role": "user", "content": "All files ending with .csv"},
          {"role": "assistant", "content": "*.csv"},
          {"role": "user", "content": "Resume.pdf"},
          {"role": "assistant", "content": "*Resume.pdf"},
          {"role": "user", "content": "Payslips"},
          {"role": "assistant", "content": "*Payslips, *Payslip, *Payslip.pdf, *Payslip.doc, Payslip, Payslips"},
          {"role": "user", "content": user_query}
      ]
  )

  return response.choices[0].message.content