from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

articles = [
    'How to load a CSV file in Python',
    'What is the best way to learn machine learning?',
    'What are the benefits of using a GPU for deep learning?'
]

for article in articles:
    response = client.responses.create(
        model="gpt-5.4",
        input=f"Write an article about: {article}"
    )
    print(response.output_text)
