import os
import openai

openai.api_key = ''

def generate_response(prom):
  start_sequence = "\nAI:"
  restart_sequence = "\nHuman: "
  prompt_ = prom
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt = prompt_,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  
  return response

while True:
  prom = input("Humman: ")
  print(generate_response(prom).choices[0]['text'])
