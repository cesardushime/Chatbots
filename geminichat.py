import google.generativeai as genai
import os


genai.configure(api_key = 'AIzaSyBBPETsDFIna-_Hf_aK9ktWhOHR6W1cYEQ..')

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Teach me something I have never learned")
print(response.text)