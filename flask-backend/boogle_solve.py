import random


class boogle():
    border = '+'
    n = 6
    ncolumn = 4

    def __init__(self):
        self.words, self.prefixes = self.read_words('words.txt')
        self.deck = self.generate_board()
        self.board = self.add_boarders()

    def board_4X4(self):
        return [self.deck[i:i+4] for i in range(0, 16, 4)]

    def generate_board(self):
        self.deck = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        random.shuffle(self.deck,)
        return self.deck[:16]

    def add_boarders(self):
        text = ''.join(r for r in self.deck)
        rows = [text[index: index + 4] for index in range(0, len(text), 4)]
        b = self.border
        rows = [b*4] + rows + [b*4]
        return ''.join(b + row + b for row in rows)

    def neighbours(self, position, n):
        return [position-1, position+1, position-n, position-n-1, position-n+1, position+n, position+n-1, position+n+1]

    def read_words(self, txt_file):
        word_list = set(open(txt_file).read().upper().split())
        prefix_list = set(
            p for word in word_list for p in self.get_prefixes(word))
        return word_list, prefix_list

    def get_prefixes(self, word):
        return [word[:i] for i in range(len(word))]

    def possible_words(self):

        found_words = set()

        def traverse_path(prefix, path):
            if prefix in self.words:
                found_words.add(prefix)
            if prefix in self.prefixes:
                for i in self.neighbours(path[-1], self.n):
                    if i not in path and self.board[i] is not self.border:
                        traverse_path(prefix+self.board[i], path+[i])

        for index, ch in enumerate(self.board):
            if ch != self.border:
                traverse_path(ch, [index])

        return found_words
