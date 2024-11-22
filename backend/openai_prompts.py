'''openai prompts'''

def prompt_restart_story():
    '''
    Returns the prompt for restarting the story
    '''

    prompt = """You are a story writer.
    You will create a story for a 15-year-old child using the style of Edgar Allan Poe.
    The story should have a simple structure with an introduction, a conflict, and a resolution.
    Each 'page' of the story should be two sentences long, except for the final page, 
    which should contain only the words 'The End' and nothing else.
    Make it engaging and age-appropriate but make sure that there is tension and a sense or horror.
    The story should be NOT MORE THAN 10 pages long.
    Introduce the main character of the story in the first page."""

    # prompt = """You are a story writer.
    # You will create a story for a 5-year-old child using the style of Elisabetta Dami .
    # The story should have a simple structure with an introduction, a conflict, and a resolution.
    # Each 'page' of the story should be two sentences long, except for the final page, 
    # which should contain only the words 'The End' and nothing else.
    # Make it engaging, age-appropriate, and include themes like friendship and adventure. 
    # The story should be NOT MORE THAN 10 pages long.
    # Introduce the main character of the story in the first page."""

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
    
    Make sure that the part that you give me extends the story and expands on the selected option.
            
    Give me also two possible ways so evolve the story, that should be not more than ten words;
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
        """A  pencil-drawn illustration
        evoking a storybook atmosphere with horror undertones. 
        The drawing style is delicate, with fine details 
        and shading that give the scene a uncomfortable, 
        hand-drawn quality, suitable for a teenagers horror book cover"
        The title of the story is: """ + book_title
    )
        
    # prompt = (
    #     """A whimsical pencil-drawn illustration
    #     evoking a gentle, storybook atmosphere. The drawing style is delicate, with fine details 
    #     and shading that give the scene a charming, 
    #     hand-drawn quality, suitable for a children's book cover"
    #     The title of the story is: """ + book_title
    # )

    return prompt
