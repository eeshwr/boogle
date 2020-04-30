import random


class boogle():
    words = {"play", "lay", "home", "hole", "role", "leg", "egg",
             "eat", "let", "tea", "max", "hoax", "meat", "mole", "drink", "sleep", "watch", "donkey", "consider"}

    prefixes = set(word[:letter]
                   for word in words for letter in range(len(word)))
    border = '+'

    n = 6
    ncolumn = 4

    def __init__(self):
        self.deck = self.generate_board()
        self.board = self.add_boarders()

    def board_4X4(self):
        return [self.deck[i:i+4] for i in range(0, 16, 4)]

    def generate_board(self):
        self.deck = [x for x in 'abcdefghijklmnopqrstuvwxyz']
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
