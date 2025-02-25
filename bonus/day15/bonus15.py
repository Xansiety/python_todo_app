import json

with open('questions.json', 'r') as file:
    content = file.read()

# print(type(content)) # <class 'str'>
data = json.loads(content)
# print(type(data)) # <class 'list'>

score = 0

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives'], start=1):  # enumerate question['alternatives']:
        print(f"{index} - {alternative}")

    user_choice = int(input("Your answer (write the number): "))
    question["user_choice"] = user_choice

    correct_answer = question['alternatives'][question['correct_answer'] - 1]

    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        print(f"Good job! The answer is {correct_answer}. Correct answers in row: {score}")
    else:
        print(f"You lost!" f"The correct answer is {correct_answer}, your score is {score} / {len(data)}")

print(f"Your final score is {score} / {len(data)} {'🤠' if score == len(data) else '😭'}")
