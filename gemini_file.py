import google.generativeai as genai
from img_handling import img
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
def summarize_image(image):
    summarize_response = model.generate_content(["Summarize these notes: ", image])
    return summarize_response.text
def make_questions(image):
    question_response = model.generate_content(["Generate test questions for these notes: ", image])
    return question_response.text
def return_text(image):
    text_response = model.generate_content(["Convert this image to text: ", image])
    return text_response.text

print(summarize_image(img))
print(make_questions(img))
print(return_text(img))