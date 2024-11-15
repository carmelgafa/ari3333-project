import openai

API_KEY = """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"""

openai.api_key = API_KEY

class OpenAIStoryWriter:
    def __init__(self):
        self.restart_story()
        self.page_number=0
        
    def restart_story(self):
        # Resets the story to its initial state with the prompt for a 5-year-old's story
        self.messages = [
            {"role": "user", "content":
            """You are a story writer. 
            You will create a story for a 5-year-old child using the style of the Grim brothers.
            The story should have a simple structure 
            with an introduction, a conflict, and a resolution.
            Each 'page' of the story should be two sentences long, 
            except for the final page, 
            which should contain only the words 'The End' and nothing else.
            Make it engaging, age-appropriate, and include 
            themes like friendship and adventure. 
            The story should be about 10 pages long."""}
        ]
    
    def get_story_title(self):
        title_prompt = {"role": "user", "content":
            """
            Give me only the title of the story. Package your title 
            in a JSON object with the following format:
            {
                "title": "The title of the story"
            }
            """}
        self.messages.append(title_prompt)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        title = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": title})
        self.page_number+=1
        return title

    def get_next_page(self, option:int):
        next_page_prompt = {"role": "user", "content":
            f"""
            Given that I selected option 
            {option}, Please give me the next part of the story in two sentences.
            
            Give me also two possible ways so evolve the story, 
            unless you are in tour final page. In this case, the text will be "The End".
            Options must have a maximum of five words. and must be referenced in the part of the story.
            Label them "Option 1" and "Option 2".
            
            Give me also a status for the story, which can be one of the following:
            "In Progress" or "Complete".
            
            Package your reply in a JSON
            object with the following format:
            {{
                "part": "The next part of the story",
                "option1": "Option 1",
                "option2": "Option 2",
                "status": "Status"
            }}
            """}
        self.messages.append(next_page_prompt)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        next_page = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": next_page})  # Log the response for continuity
        
        self.page_number+=1
        
        return next_page

if __name__ == "__main__":
    writer = OpenAIStoryWriter()

    print("Title:", writer.get_story_title())

    while writer.get_next_page(1).strip() != "The End":
        print("Page:", writer.get_next_page(1))
