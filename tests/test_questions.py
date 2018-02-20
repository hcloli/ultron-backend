
import json

quiz = json.load(open("../questions/quiz.json"))
for qu in quiz["questions"]:
    del qu['answer']
print(quiz)