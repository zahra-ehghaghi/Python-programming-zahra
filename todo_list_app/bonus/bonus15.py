import json
with open("../files/questions.json","r") as file:
     questions = json.loads(file.read())
print(questions)
for  question in questions:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(f"{index +1} - {alternative}")
    answer = int(input("Enter Your Answer: "))
    question["user_choice"]=answer

sum = 0
for index, question in enumerate(questions):
    if question["user_choice"] == question["correct_answer"]:
        message = "Correct Answer"
        sum +=1
    else:
        message = "Wrong Answer"
    print(f"{message} {index+1} - Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}")

print(f"{sum}/{len(questions)}")