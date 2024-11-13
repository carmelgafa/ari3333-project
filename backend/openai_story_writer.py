import openai

API_KEY = """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"""

openai.api_key = API_KEY

class OpenAIStoryWriter:
    def __init__(self):
        self.restart_story()
        
    def restart_story(self):
        # Resets the story to its initial state with the prompt for a 5-year-old's story
        self.messages = [
            {"role": "user", "content": """You are a story writer. You will create a story for a 5-year-old child.
            The story should have a simple structure with an introduction, a conflict, and a resolution.
            Each 'page' of the story should be two sentences long, 
            except for the final page, which should contain only the words 'The End' and nothing else.
            Make it engaging, age-appropriate, and include themes like friendship, adventure, or kindness."""}
        ]
    
    def get_story_title(self):
        title_prompt = {"role": "user", "content": "Give me only the title of the story."}
        self.messages.append(title_prompt)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        title = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": title})  # Log the title response 
        return title

    def get_next_page(self):
        next_page_prompt = {"role": "user", "content": 
            """
            Please give me the next part of the story. Give me also two possible ways so evolve the story.
            Options must have a maximum of five words.Label them "Option 1" and "Option 2".
            """}
        self.messages.append(next_page_prompt)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        next_page = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": next_page})  # Log the response for continuity
        return next_page

if __name__ == "__main__":
    writer = OpenAIStoryWriter()

    print("Title:", writer.get_story_title())

    
    while writer.get_next_page().strip() != "The End":
        print("Page:", writer.get_next_page())
   