'''openai prompts'''

import json
import story_parameters

def prompt_restart_story()->str:
    '''
    Returns the prompt for restarting the story
    '''

    prompt = f"""
    You are a story writer.\n
    You will create a story for a {story_parameters.READER_AGE}-year-old  using the style of {story_parameters.BOOK_STYLE}.\n
    The story should have a simple structure with an introduction, a conflict, and a resolution.\n
    Each 'page' of the story should be two sentences long, except for the final page, 
    which should contain only the words 'The End' and nothing else.\n
    Make it engaging and age-appropriate but make sure that there is {story_parameters.BOOK_THEME}.\n
    The story should be NOT MORE THAN {story_parameters.MAXIMUM_PAGES} pages long.\n
    Introduce the main character of the story in the first page."""

    return prompt

def prompt_story_title()->str:
    '''
    Returns the prompt for getting the title of the story
    '''

    prompt = """Give me only the title of the story."""

    return prompt

def prompt_next_page(option:int)->str:
    '''
    Returns the prompt for getting the next page of the story
    '''

    data = {
        "part": "The next part of the story",
        "option1": "Option 1",
        "option2": "Option 2",
        "status": "Status"
    }

    prompt =  f"""
    
    Given that I selected option {option}, give me the next part of the story in a paragraph
    that extend the story so far and on the option I selected.\n


            
    Give me also two possible ways to evolve the story, that should be not more than ten words;
    unless you are in tour final page. In this case, the text will be "The End".\n
            
    Label them "Option 1" and "Option 2".\n
    
    Give me also a status for the story, which can be one of the following:
    "In Progress" or "Complete".\n
    
    Package your reply in a JSON
    object with the following format:
    {json.dumps(data)}
    """

    return prompt


def prompt_story_image(book_title:str)->str:
    '''
    Returns the prompt for getting the image of the story
    '''
    prompt = (
        f"""A  pencil-drawn illustration
        evoking a storybook atmosphere of {story_parameters.BOOK_THEME}.\n
        The drawing style is aligned with the writing of {story_parameters.BOOK_STYLE}".\n
        The title of the story is {book_title} """
    )
    return prompt
