import torch 
from diffusers import AutoPipelineForText2Image

model_id = "stable-diffusion-v1-5/stable-diffusion-v1-5"

pipeline = AutoPipelineForText2Image.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipeline= pipeline.to("cpu")

prompt = "A cute orange cat reading a book in a library"

image = pipeline(
    prompt,
    num_inference_steps=10,
    guidance_scale=7.5
).images[0]

image.save("my_ai_image.png")

print("Image saved successfully!")

