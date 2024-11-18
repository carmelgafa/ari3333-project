import openai
import openai_secret
from openai_prompts import prompt_restart_story
from openai_prompts import prompt_story_title
from openai_prompts import prompt_next_page

openai.api_key = openai_secret.API_KEY


class OpenAIStoryWriter:
    '''
    Class for generating stories
    '''

    def __init__(self):
        self.restart_story()
        self.page_number=0

    def restart_story(self):
        '''
        Restarts the story
        '''
        self.messages = [{"role": "user", "content": prompt_restart_story()}]

    def get_story_title(self):
        '''
        Returns the title of the story
        '''

        title_prompt = {"role": "user", "content": prompt_story_title()}
        self.messages.append(title_prompt)

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )

        title = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": title})
        self.page_number+=1
        return title

    def get_next_page(self, option:int):
        '''
        Returns the next page of the story
        '''
        next_page_prompt = {"role": "user", "content": prompt_next_page(option)}

        self.messages.append(next_page_prompt)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        next_page = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": next_page})

        self.page_number+=1

        return next_page

if __name__ == "__main__":
    writer = OpenAIStoryWriter()

    print("Title:", writer.get_story_title())

    while writer.get_next_page(1).strip() != "The End":
        print("Page:", writer.get_next_page(1))
