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
    response = {"response": []};

    if bibliography:
        booklines = bibliography.splitlines()
        for book in booklines:
            try:
                parserinfo = parser.get_data_obj(book, [",", "/", ";"])
                result = get_book_google(parserinfo.author, parserinfo.title, int(parserinfo.year))
                if result == 'Es wurde eine neuere Version gefunden':
                    code = 1
                else:
                    code = 2
            except:
                result = "keine gültige quelle"
                code = 3
            response['response'].append({ 'book': book, 'result': result, 'code': code});
        return response, 200
    else:
        return jsonify({'error': 'Parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
