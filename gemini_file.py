import google.generativeai as genai
import img_handling as imgh
import os
import base64

image = r"images/unchanged_sharp.jpg"

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
summarize_response = model.generate_content([{'mime_type':'image/jpg', 'data': base64.b64encode(image.content).decode('utf-8')}, "Summarize these notes: "])
print(summarize_response.text)