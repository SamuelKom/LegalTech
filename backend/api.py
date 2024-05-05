from flask import Flask, request, jsonify
from flask_cors import CORS

from ref_parser import Parser
from google_api import get_book_google

app = Flask(__name__)
CORS(app)
parser = Parser()

@app.route('/check', methods=['POST'])
def check():
    print(request)
    bibliography = request.get_json().get('bibliography')

    if bibliography:
        booklines = bibliography.splitlines()
        for book in booklines:
            parserinfo = parser.get_data_obj(book, [",", "/", ";"])
            get_book_google(parserinfo.authors, parserinfo.title, parserinfo.year)

        #google api
        return jsonify({'received_text': bibliography}), 200
    else:
        return jsonify({'error': 'Parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
