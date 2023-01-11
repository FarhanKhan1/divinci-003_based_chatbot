import os
import openai

openai.api_key = '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'

def generate_response(prom):
  start_sequence = "\nAI:"
  restart_sequence = "\nHuman: "
  prompt_ = prom
  response = openai.Completion.create(
    model="text-davinci-003",
    # prompt="""The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?
    # AI: I am an AI created by OpenAI. How can I help you today?\nHuman: can you please generate a job summary for my resume for data scientist?\n\nAI: Sure, I'd be happy to help. A job summary for a data scientist should include information about your technical skills in areas such as programming languages and databases, as well as your knowledge of business analysis techniques and industry trends. You should also highlight your ability to develop effective algorithms, create meaningful data visualizations, and communicate complex ideas in clear and concise terms.\nHuman: please generate it.\n\nAI: Experienced data scientist with a proven track record of success in developing efficient algorithms and meaningful data visualizations to gain insights from large datasets. Proficient in a variety of programming languages, databases, and business analysis techniques. Skilled at articulating complex ideas in clear and concise terms, as well as st\n\n\nAI: ay up-to-date with industry trends in order to create the most effective solutions. Dedicated to using data-based approaches to solve challenging business problems. Ready to leverage my skills to benefit any organization.\nHuman: please generate a resume for a 3 years experienced data scientist.\n\nAI: Experienced data scientist with three years of successful experience in developing efficient algorithms, meaningful data visualizations, and performing business analysis to gain insights from large datasets. Proven track record of utilizing various programming languages, databases, and industry trends to create successful solutions. Skilled in communicating complex ideas in clear terms and creating data-based approaches to solve challenging business problems. Ready to leverage my experience to benefit any organization.\nHuman: make it formatted please.\nAI: Sure. I can provide you with a professionally formatted, attractive resume that highlights your data science experience. The resume will include sections on your technical skills, relevant industry experience, and accomplishments. It will also be tailored to emphasize any unique qualifications that you may have. Let me know if you need any other specific changes.\nHuman: please generate skills for a data scientist.\nAI: Skills required for a data scientist include programming languages (such as Python, Java, and C++), databases (such as SQL, NoSQL, and Hadoop), business analysis techniques (such as predictive modeling and market research), data visualization tools (such as Tableau and PowerBI), and machine learning algorithms (such as random forests and neural networks). Additionally, data scientists should have strong problem-solving capabilities, excellent communication and interpersonal skills, and an understanding of the latest industry trends.\nHuman: please generate skills for a data scientist with commas. Programming languages (such as Python, Java, and C++), databases (such as SQL, NoSQL, and Hadoop), business analysis techniques (such as predictive modeling and market research), data visualization tools (such as Tableau and PowerBI), machine learning algorithms (such as random forests and neural networks), strong problem-solving capabilities, excellent communication and interpersonal skills, and an understanding of the latest industry trends.""",
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
