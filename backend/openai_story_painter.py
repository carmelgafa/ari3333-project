'''responsible to generate cover images for stories'''

import openai
import system_secret as system_secret
from openai_prompts import prompt_story_image

openai.api_key = system_secret.OPEANAI_API_KEY

class OpenAIStoryPainter:
    '''
    Class for generating images for stories
    '''

    def __init__(self):
        pass

    def get_story_image(self, book_title:str):
        '''
        Returns the image for the story given the title
        '''

        # Generate the image
        response = openai.Image.create(
            prompt=prompt_story_image(book_title),
            n=1,
            size="256x256"
        )

        # Extract the URL of the generated image
        image_url = response['data'][0]['url']

        return image_url

if __name__ == "__main__":

    painter = OpenAIStoryPainter()
    image_path = painter.get_story_image("The Adventures of Tom Sawyer")
    print(image_path)
