'''
The backend for the OpenAI Story Writer app
'''

# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from openai_story_writer import OpenAIStoryWriter
app = Flask(__name__)
CORS(app)  # Enable CORS

writer = OpenAIStoryWriter()

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
    writer.restart_story()
    title = writer.get_story_title()
    return jsonify(title)


if __name__ == '__main__':
    app.run(debug=True)
