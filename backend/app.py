'''The backend for the OpenAI Story Writer app'''

# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from openai_story_writer import OpenAIStoryWriter
from openai_story_painter import OpenAIStoryPainter
from azure_story_teller import azure_tts


app = Flask(__name__)
CORS(app)  # Enable CORS

writer = OpenAIStoryWriter()
painter = OpenAIStoryPainter()

@app.route('/api/page/<int:option>', methods=['GET'])
def get_page(option):
    '''
    Returns the next page of the story
    '''
    next_page = writer.get_next_page(option=option)

    next_page_dict = eval(next_page)

    print("before azure tts")

    next_page_dict["textURL"] = azure_tts(
        f"""{next_page_dict["part"]}
        You have two options. Option 1 is 
        {next_page_dict["option1"]}
        and option 2 is
        {next_page_dict["option2"]}"""
        )

    print("after azure tts")
    print(next_page_dict)


    return jsonify(next_page_dict)


@app.route('/api/title', methods=['GET'])
def get_title():
    '''
    Returns the title of the story
    '''

    writer.restart_story()

    book_title = writer.get_story_title()
    image_url = painter.get_story_image(book_title)

    return jsonify({"title": book_title, "image_url": image_url})


if __name__ == '__main__':
    app.run(debug=True)
