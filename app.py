from flask import Flask, request, jsonify
from spellchecker import SpellChecker

app = Flask(__name__)

sc = SpellChecker()

@app.route('/spellCorrect', methods=['POST'])
def spell_correct():
    print(request.is_json)
    content = request.get_json()
    suggestions = sc.correction(content['word'])
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
