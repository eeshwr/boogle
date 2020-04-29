import random
from flask import Flask, jsonify
from flask_cors import CORS
from boogle_solve import boogle
app = Flask(__name__)
CORS(app)


@app.route('/boogle')
def boogle_board():
    deck = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    import random
    random.shuffle(deck,)
    return jsonify([deck[i:i+4] for i in range(0, 16, 4)])


@app.route('/load_boogle')
def load_boogle():
    game = boogle()
    game.generate_board()
    words = list(game.possible_words())
    board = [['P', 'L', 'A', 'y'], ['H', 'O', 'M', 'X'],
             ['R', 'L', 'E', 'Z'], ['G', 'G', 'T', 'A']]

    return jsonify({'board': board, 'correct_words': words})


if __name__ == '__main__':
    app.run(debug=True)
