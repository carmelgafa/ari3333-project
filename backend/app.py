# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Sample page data
pages = [
    "This is the content of Page 1",
    "This is the content of Page 2",
    "This is the content of Page 3",
    "This is the content of Page 4",
]

@app.route('/api/page/<int:page_number>', methods=['GET'])
def get_page(page_number):
    if 0 <= page_number < len(pages):
        return jsonify({"content": pages[page_number]})
    else:
        return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
