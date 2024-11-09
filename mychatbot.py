import openai

openai.api_key = "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" 

def chat_withMe(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
    )
    return response['choices'][0]['message']['content'].strip()

user_input = "Create a sample cover letter"

response = chat_withMe(user_input)
print("chatbot: ", response)