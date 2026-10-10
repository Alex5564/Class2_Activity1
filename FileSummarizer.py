import requests
from config import HF_API_KEY

model = "facebook/bart-large-cnn"

url = f"https://api-inference.huggingface.co/models/{model}"


headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

text = input("Enter text to summarize: ")

if text.strip():
    try:
        response = requests.post(
            url,
            headers = headers,
            json = {"inputs": text},
        )

        result = response.json()

        if response.ok and isinstance(result, list) and result and "summary_text" in result[0]:
            print("\nSummary:")
            print(result[0]["summary_text"])
        else:
            print("Error:", result)

    except requests.RequestException:
        print("Check your internet connection")
    else:
        print("Please enter some text")

        

