import openai

API_KEY = """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"""

openai.api_key = API_KEY

class OpenAIStoryWriter:
    def __init__(self):
        self.restart_story()
        self.page_number = 0

    def restart_story(self):
        self.messages = [
            {"role": "user", "content":
            """You are a story writer. Write a magical, adventurous story for a 5-year-old in the style of the Grimm brothers. 
            The story must have a lovable main character, a vivid setting, and themes of friendship and wonder. 
            Each 'page' must be two sentences long, except the final page, which simply says 'The End.
            The story should be about 10 pages long.'"""}
        ]
    
    def get_story_title(self):
        self.messages.append(
            {"role": "user", "content": "Suggest a whimsical and engaging title for this story."}
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        title = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": title})
        self.page_number += 1
        return title

    def get_next_page(self, option: int):
        self.messages.append(
            {"role": "user", "content": 
            f"""Continue the story based on option {option}. Keep it whimsical and age-appropriate. 
            Provide two logical options for what happens next. If the story ends, respond with 'The End.' 
            Format your response as a JSON object: {{'part': '', 'option1': '', 'option2': '', 'status': ''}}."""}
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        next_page = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": next_page})
        self.page_number += 1
        return next_page
