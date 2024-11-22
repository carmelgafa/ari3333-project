'''The backend for the OpenAI Story Writer app'''

import json
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from openai_story_writer import OpenAIStoryWriter
from openai_story_painter import OpenAIStoryPainter
from azure_story_teller import generate_speech


app = Flask(__name__)
CORS(app)  # Enable CORS

# Create an instance of OpenAIStoryWriter that 
# is used to generate stories and titles
writer = OpenAIStoryWriter()
# Create an instance of OpenAIStoryPainter that
# is used to generate images
painter = OpenAIStoryPainter()

@app.route('/api/page/<int:option>', methods=['GET'])
def get_page(option):
    '''
    Returns the next page of the story
    '''

    # Generate the next page
    next_page = writer.generate_next_page_text(option=option)

    next_page_dict = json.loads(next_page)

    # Generate the speech for the next page and options
    next_page_dict["textURL"] = generate_speech(
        format_speech(next_page_dict)
        )

    return jsonify(next_page_dict)


def format_speech(next_page_dict):
    '''Formats the speech for the page'''

    return f"""{next_page_dict["part"]}
        You have two options. Option 1 is 
        {next_page_dict["option1"]}
        and option 2 is
        {next_page_dict["option2"]}"""


@app.route('/api/title', methods=['GET'])
def get_title():
    '''
    Returns the title of the story
    '''

    writer.restart_story()

    book_title = writer.generate_story_title()
    image_url = painter.get_story_image(book_title)

    return jsonify({"title": book_title, "image_url": image_url})


if __name__ == '__main__':
    app.run(debug=True)
