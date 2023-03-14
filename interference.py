import json
from transformers import pipeline


def generate_response(file):
    question_answerer = pipeline("question-answering", model="model")
    return question_answerer(question=file['question'], context=file['context'])['answer']


with open('sample.json', "rb") as json_file:
    sample = json.load(json_file)

response = generate_response(sample)

print(response)
