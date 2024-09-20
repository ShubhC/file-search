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
                                         "Final Output will be comma seperated keyword list."
                                         "Don't take full file take out keywords from that and gerate regex for those"
                                         "The final regex should contain all the main keywords"
                                         "Don't geneate regex for rach keyword"
                                         "Generate the keywords such that it will search in full file name not only in starting or between"
                                         "Use some smart way to generate keywrod main keyword should have seperate regex won't combine it with others"
                                         "Given a query generate the wildcard expressions of keywrods also consist of * and ."
                                         "Generate keyword for specific word not not wordls like is, and, all, the check for the main highlighted word in the query")},
          {"role": "user", "content": "All payslips files"},
          {"role": "assistant", "content": ("*payslip.pdf, *payslip.doc, *payslip.csv, *payslip, *payslips, payslip, payslips, .*payslip(s)?.*, .*pay.*slip(s)?.*, .*payslip(s)?.*doc.*, .*payslip(s)?.*pdf.*"
                                            ".*payslip(s)?.*txt.*, .*pay.*slip(s)?.*doc.*, .*pay.*slip(s)?.*pdf.*, .*pay.*slip(s)?.*txt.*" )},
          {"role": "user", "content": "All files ending with .csv"},
          {"role": "assistant", "content": "*.csv, .*\\.csv$, .*\\.CSV$"},
          {"role": "user", "content": "Resume.pdf"},
          {"role": "assistant", "content": "*Resume.pdf"},
          {"role": "user", "content": "Payslips"},
          {"role": "assistant", "content": "*Payslips, *Payslip, *Payslip.pdf, *Payslip.doc, Payslip, Payslips"},
          {"role": "user", "content": "All files for march 30"},
          {"role": "assistant", "content": ("march30*, *march 30*, *march-30*, *march_30*, *march30, *march 30, *march-30, *march_30, *march30.pdf, *march 30.pdf, *march-30.pdf, *march_30.pdf, *march30.doc," 
                                            "*march 30.doc, *march-30.doc, *march_30.doc, *march30.csv, *march 30.csv, *march-30.csv, *march_30.csv, *march30.txt, *march 30.txt, *march-30.txt, *march_30.txt," 
                                            "*march30.docx, *march 30.docx, *march-30.docx, *march_30.docx, *march30.xls, *march 30.xls, *march-30.xls, *march_30.xls, *march30.xlsx, *march"
                                            "\bMarch30\.(doc|pdf|txt)\b, \b30March\.(doc|pdf|txt)\b, \b30_March\.(doc|pdf|txt)\b, \bMarch_30\.(doc|pdf|txt)\b, \b30-March\.(doc|pdf|txt)\b, \bMarch-30\.(doc|pdf|txt)\b")},
          {"role": "user", "content": user_query}
      ]
  )

  return response.choices[0].message.content