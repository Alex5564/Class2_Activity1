import requests

url = "https://opentdb.com/api.php?amount=5&type=multiple"
response = requests.get(url)
data = response.json()
questions = data["results"]

score = 0

for index, q in enumerate(questions, 1):
    print(f"\nQuestion {index}:")
    print(q["question"])

    choices = [q["correct_answer"]] + q["incorrect_answers"]

    for i, choice in enumerate(choices, 1):
        print(f"  {i}. {choice}")

    user_input = input("Your answer (1, 2, 3, or 4): ")
    user_choice = int(user_input)

    selected_answer = choices[user_choice - 1]

    if selected_answer == q["correct_answer"]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
        print("Correct Answer:", q["correct_answer"])

print(f"\nFinal Score: {score} out of 5")
