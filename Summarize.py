import requests
from config import HF_API_KEY

text = input("Enter text to summarize: ")

if text.strip():
    print("\nAvailable Models:")
    print("1. Pegasus (google/pegasus-xsum)")
    print("2. BART (facebook/bart-large-cnn)")
    model_choice = input("Select a model (1 or 2, press Enter for default): ").strip()
    
    if model_choice == "1":
        model = "google/pegasus-xsum"
    else:
        model = "facebook/bart-large-cnn"

    print("\nSummarization Styles:")
    print("1. Concise Summary (50-150 tokens)")
    print("2. Detailed Summary (80-200 tokens)")
    style_choice = input("Select a style (1 or 2, press Enter for Concise): ").strip()

    if style_choice == "2":
        min_length, max_length = 80, 200
    else:
        min_length, max_length = 50, 150

    url = f"https://huggingface.co{model}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length,
            "do_sample": False
        }
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
        )

        result = response.json()

        if response.ok and isinstance(result, list) and result and "summary_text" in result[0]:
            print("\nSummary:")
            print(result[0]["summary_text"])
        else:
            if response.status_code == 503:
                print("\nModel is loading. Please try again in 20 seconds.")
            else:
                print("Error:", result)

    except requests.RequestException:
        print("Check your internet connection")

else:
    print("Please enter some text")
