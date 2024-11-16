'''
The backend for the OpenAI Story Writer app
'''

# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from openai_story_writer import OpenAIStoryWriter
from openai_story_painter import OpenAIStoryPainter
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
    return jsonify(next_page)


@app.route('/api/title', methods=['GET'])
def get_title():
    '''
    Returns the title of the story
    '''
    print("Fetching the book title")  # This will log to the console
    writer.restart_story()
    title = writer.get_story_title()
    return jsonify({"title": title})


@app.route('/api/image/<string:book_title>', methods=['GET'])
def get_image(book_title):
    '''
    Returns the image of the story
    '''
    print("Fetching the book image")  # This will log to the console
    image_url = painter.get_story_image(book_title)
    print(image_url)
    return jsonify({"image_url": image_url})

if __name__ == '__main__':
    app.run(debug=True)
