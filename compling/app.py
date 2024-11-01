# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.tree import Tree

# Download any necessary NLTK packages (e.g., the parser)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)
CORS(app)

@app.route('/parse', methods=['POST'])
def parse_sentence():
    data = request.get_json()
    sentence = data.get('sentence')

    if not sentence:
        return jsonify({"error": "No sentence provided"}), 400

    # Here, use any parsing logic you like. This example assumes you have a syntax tree generator.
    # For simplicity, we'll use a dummy tree as an example.
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    tree = Tree.fromstring("(S (NP (DT The) (NN cat)) (VP (VBD sat) (PP (IN on) (NP (DT the) (NN mat)))))")
    tree_data = str(tree)

    return jsonify({"syntax_tree": tree_data})

if __name__ == '__main__':
    app.run(port=5000)
