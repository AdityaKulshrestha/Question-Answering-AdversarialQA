import json
from transformers import pipeline

#Funtion to perform inference
def generate_response(file: json):
    question_answerer = pipeline("question-answering", model="model")
    return question_answerer(question=file['question'], context=file['context'])['answer']

# Inferencing on a sample
with open('sample.json', "rb") as json_file:
    sample = json.load(json_file)

response = generate_response(sample)

print(response)
