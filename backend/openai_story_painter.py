import openai
import openai_secret

openai.api_key = openai_secret.API_KEY

class OpenAIStoryPainter:
    def __init__(self):
        pass
        
    
    def get_story_image(self, book_title="The Brave Bunny and the Fox Friend"):
        prompt = (
            "A whimsical pencil-drawn illustration"
            "evoking a gentle, storybook atmosphere. The drawing style is delicate, with fine details "
            "and shading that give the scene a charming, hand-drawn quality, suitable for a children's book cover"
            "The title of the story is: " + book_title
        )

        # Generate the image
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256"
        )

        # Extract the URL of the generated image
        image_url = response['data'][0]['url']

        return image_url

if __name__ == "__main__":
    
    painter = OpenAIStoryPainter()
    image_url = painter.get_story_image()
    print(image_url)


