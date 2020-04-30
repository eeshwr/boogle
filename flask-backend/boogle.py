import random
from flask import Flask, jsonify
from flask_cors import CORS
from boogle_solve import boogle
app = Flask(__name__)
CORS(app)


@app.route('/load_boogle')
def load_boogle():
    game = boogle()
    words = list(game.possible_words())
    board = game.board_4X4()

    return jsonify({'board': board, 'correct_words': words})


if __name__ == '__main__':
    app.run(debug=True)
