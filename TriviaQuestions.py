import requests 

url = "https://opentdb.com/api.php?amount=1"

response = requests.get(url)

data = response.json()

question = data['results'][0]['question']
answer = data['results'][0]['correct_answer']

print("Question:")
print(question)

user_answer = input("\nYour Answer: ")

if user_answer.lower() == answer.lower():
    print("Correct Answer")
else:
    print("Wrong Answer")
    print("Correct Answer:", answer)
