'''openai prompts'''

def prompt_restart_story():
    '''
    Returns the prompt for restarting the story
    '''

    prompt = """You are a story writer.
    You will create a story for a 5-year-old child using the style of the Grim brothers.
    The story should have a simple structure with an introduction, a conflict, and a resolution.
    Each 'page' of the story should be two sentences long, except for the final page, 
    which should contain only the words 'The End' and nothing else.
    Make it engaging, age-appropriate, and include themes like friendship and adventure. 
    The story should be NOT MORE THAN 10 pages long."""

    return prompt

def prompt_story_title():
    '''
    Returns the prompt for getting the title of the story
    '''

    prompt = """Give me only the title of the story."""

    return prompt

def prompt_next_page(option:int):
    '''
    Returns the prompt for getting the next page of the story
    '''

    prompt =  f"""  Given that I selected option
    {option}, Please give me the next part of the story in two sentences
    that is based on the story so far and on the option I selected.
            
    Based on the story so far, give me also two possible ways so evolve the story, 
    unless you are in tour final page. In this case, the text will be "The End".
            
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
    """

    return prompt


def prompt_story_image(book_title:str):
    '''
    Returns the prompt for getting the image of the story
    '''
    prompt = (
        """A whimsical pencil-drawn illustration
        evoking a gentle, storybook atmosphere. The drawing style is delicate, with fine details 
        and shading that give the scene a charming, 
        hand-drawn quality, suitable for a children's book cover"
        The title of the story is: """ + book_title
    )

    return prompt
