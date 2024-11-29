import google.generativeai as genai
import img_handling as imgh
import os

genai.configure(os.environ(process.env.GEMINI_API_KEY))
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Summarize these notes : ")
print(response.text)
user_input = ""
while user_input != "stop":
    if user_input 
    take in input
    pass to gemini
    print response