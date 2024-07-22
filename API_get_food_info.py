from openai import OpenAI
import base64
import requests
import os 

# Set model name and API key
MODEL = 'gpt-4o'
client = OpenAI(api_key='sk-proj-Fkp0iDgnHXsMIFrpCRJDT3BlbkFJtV2uHwzzLOgYIIzwkMgT')

def encode_image(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

IMAGE_PATH = 'test_item.jpg'
base64_image = encode_image(IMAGE_PATH)

response = client.chat.completions.create(
  model= MODEL,
  messages=[
    {
      "role": "user",
      "content": [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"}
        },{
            "type": "text",
            "text": "Send back name and calorie of this item using certain form below:\nname:\ncalorie:"
        }
    ]},
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)