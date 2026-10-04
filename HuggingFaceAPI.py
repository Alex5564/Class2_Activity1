import requests
from config import HF_API_KEY

MODEL_ID = "cardiffnlp/twitter-roberta-base-sentiment-latest"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

TEST_TEXTS = [
    "I love this movie",
    "I hate this product",
    "The package arrived today.",
    "This was a completely average experience.",
    "I'm not sure how I feel about the changes."
]

def analyze_sentiment(text: str):
    """Analyzes the sentiment of the given text using Hugging Face API."""
    payload = {"inputs": text}
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    
    if not r.ok: 
        raise RuntimeError(f"HF error {r.status_code}: {r.text}")
        
    data = r.json()
    if isinstance(data, dict): 
        raise RuntimeError(data.get("error", str(data)))
    predictions = data[0] if isinstance(data[0], list) else data

    top_prediction = max(predictions, key=lambda x: x['score'])
    
    label_mapping = {
        "positive": "POSITIVE",
        "negative": "NEGATIVE",
        "neutral": "NEUTRAL"
    }
    
    raw_label = top_prediction['label'].lower()
    sentiment_label = label_mapping.get(raw_label, raw_label.upper())
    confidence_score = float(top_prediction['score'])
    
    return sentiment_label, confidence_score

def bar(score01: float) -> str:
    """Creates a visual confidence loading bar."""
    blocks = int((score01 * 100) // 10)
    return "█" * blocks + "░" * (10 - blocks)

def main():
    print("🎭 Sentiment Analysis Tool")
    print("This tool classifies the sentiment of text inputs.\n")

    while True:
        print("Type 'demo' to test examples, or 'custom' to type your own, or 'exit'.")
        mode = input("Mode: ").strip().lower()
        if mode == "exit":
            print("Bye! 🚀")
            break

        if mode == "demo":
            for i, text in enumerate(TEST_TEXTS, 1):
                try:
                    sentiment, score = analyze_sentiment(text)
                    pct = round(score * 100, 1)
                    print(f"\n{i}) Input Text: \"{text}\"")
                    print(f"   Sentiment:  {sentiment}")
                    print(f"   Confidence: {pct}% [{bar(score)}]")
                except Exception as e:
                    print(f"\nError processing text {i}: {e}")
            print("\n" + "="*40 + "\n")

        elif mode == "custom":
            text = input("\nEnter text to analyze: ").strip()
            if not text:
                print("Please type something to analyze.\n")
                continue
            try:
                sentiment, score = analyze_sentiment(text)
                pct = round(score * 100, 1)
                print(f"\nResults:")
                print(f"Sentiment:  {sentiment}")
                print(f"Confidence: {pct}% [{bar(score)}]\n")
            except Exception as e:
                print(f"An error occurred: {e}\n")

        else:
            print("Please type: demo / custom / exit\n")

if __name__ == "__main__":
    main()
