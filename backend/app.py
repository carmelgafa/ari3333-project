'''
The backend for the OpenAI Story Writer app
'''

# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from openai_story_writer import OpenAIStoryWriter
from openai_story_painter import OpenAIStoryPainter
from azure_story_teller import azure_tts
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
    print("Fetching the book title")
    writer.restart_story()
    title = writer.get_story_title()
    return jsonify({"title": title})


@app.route('/api/image/<string:book_title>', methods=['GET'])
def get_image(book_title):
    '''
    Returns the image of the story
    '''
    print("Fetching the book image")
    image_url = painter.get_story_image(book_title)
    print(image_url)
    return jsonify({"image_url": image_url})

@app.route('/api/speech/<string:book_text>', methods=['GET'])
def get_speech(book_text):
    '''
    Returns the speech of the story
    '''
    print("Fetching the book speech")
    
    result:bool = azure_tts(book_text)
    result = "True"
    
    return jsonify({"speechAvailable": result})


if __name__ == '__main__':
    app.run(debug=True)
