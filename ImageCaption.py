import requests 
import base64
import os
import re

from PIL import Image
from colorama import init, Fore, Style
from config import HF_API_KEY

init(autoreset=True)


ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

VISION_MODELS = [
    "meta-llama/Llama-3.2-11B-Vision-Instruct:sambanova",
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct:sambanova"
]

TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct:together",
    "mistralai/Mistral-7B-Instruct-v0.3:together"
]

def data_url(image_path):
    with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode("utf-8")

        return "data:image/jpeg;base64," + image_data

def query_api(payload):
    try:
        response = requests.post(
            ROUTER_URL,
            headers=HEADERS,
            json=payload,
            timeout=120
        )

        if response.status_code !=200:
            return None, f"API error {response.status_code}:{response.text}"

        return response.json(), None

    except requests.RequestException as error:
        return None, str(error)

def extract_text(data):
    message = data["choices"][0]["message"]
    content = message.get("content", "")    
    return content.strip() if isinstance(content, str) else ""

def run_models(models, messages, max_tokens=160):
    last_error = "No model returned text."

    for model in models:
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": 0.3
        }

        data, error = query_api(payload)

        if error:
            last_error = error
            continue

        try:
            result = extract_text(data)

            if result:
                return result, None

            last_error = "Empty response from model."

        except (KeyError, IndexError, TypeError):
            last_error= "Invalid API response."


    return None, last_error 


def words(text):
    return re.findall(r"\S+", (text or "").strip())

def exact_n_words(text, n):
    return " ".join(words(text)[:n])

def ensure_sentence_end(text):
    text = text.strip()

    if text and text[-1] not in ".!?":
        text += "."

    return text

def get_basic_caption(image_path):
    print(Fore.YELLOW + "Generating basic caption...")

    messages = [{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Describe the image in one complete sentence."
            },
            {
                "type": "image_url", 
                "image_url": {
                    "url": data_url(image_path)

                }
            }
        ]
    }]

    caption, error = run_models(VISION_MODELS, messages, 90)