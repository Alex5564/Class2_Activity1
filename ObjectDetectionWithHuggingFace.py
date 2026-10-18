import os
import time
import requests
from PIL import Image, ImageDraw

API_URL = (
    "https://router.huggingface.co/"
    "hf-inference/models/facebook/detr-resnet-50"
)


TOKEN = os.getenv("HF_TOKEN")

if not TOKEN:
    print("Please set your Hugging Face token first!")
    raise SystemExit

headers = {
    "Authorization": f"Bearer {TOKEN}",
}

try:
    image = Image.open("ny_picture.jpg").convert("RGB")
    print("Picture opened successfully.")

except FileNotFoundError:
    print("Please put ny_picture.jpg in this folder.")

with open ("ny_picture.jpg", "rb") as file:
    picture_data = file.read()

results = None

for attempt in range(3):
    try:
        print("AI is looking at the picture...")

        response = requests.post(
            
            API_URL,
            headers=headers,
            data=picture_data, 
            timeout=60
        )

        response.raise_for_status()
        results = response.json()
        break

    except (requests.RequestException, ValueError) as error:
        print("Something went wrong:", error)
        
        if attempt < 2:
            print("Trying again...")
            time.sleep(2 ** attempt)

if results is None:
    print("AI could not finish. Please try later.")
    raise SystemExit

draw = ImageDraw.Draw(image)
count = 0

if isinstance(results, list):
    for item in results:
        if not isinstance(item, dict) or "box" not in item:
            continue

        box = item["box"]
        label = item.get("label", "Object")
        score = float(item.get("score", 0.0))

        if score < 0.60:
            continue

        left = int(box["xmin"])
        top = int(box["ymin"])
        right = int(box["xmax"])
        bottom = int(box["ymax"])

        draw.rectangle(
            [(left, top), (right, bottom)],
            outline="red",
            width=4
        )

        text = f"{label}: {score:.2f}"

        draw.text(
            (left, max(0, top - 20)),
            text,
            fill="blue"
        )

        print(f"Found: {label} ({score:.2f})")
        count += 1

image.save("detected_picture.png")
print("Objects found:", count)
print("Saved as detected_picture.png")

image.show()
