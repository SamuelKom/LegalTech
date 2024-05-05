from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['POST'])
def check():
    print(request)
    bibliography = request.args.get('bibliography')

    if bibliography:
        print(bibliography)
        #parser
        #google api
        return jsonify({'received_text': bibliography}), 200
    else:
        return jsonify({'error': 'Parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
