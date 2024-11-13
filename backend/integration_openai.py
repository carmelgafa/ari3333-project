import openai


API_KEY="""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"""

openai.api_key = API_KEY


def chat_with_gpt(prompt):
    
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Start chatting with GPT! Type 'quit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Ending the chat. Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("GPT:", response)
