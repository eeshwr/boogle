class boogle():
    words = {"play", "lay", "home", "hole", "role", "leg", "egg",
             "eat", "let", "tea", "max", "hoax", "meat", "mole", "drink", "sleep", "watch", "donkey", "consider"}

    prefixes = set(word[:letter]
                   for word in words for letter in range(len(word)))
    border = '+'

    n = 6

    def __init__(self):
        pass

    def generate_board(self):
        # deck = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        # import random
        # random.shuffle(deck,)
        # abcd = 'abcdefghijklmnopqrsquvwxyz'
        self.board = [x for x in '+++++++play++homx++rlez++ggta+++++++']

    def Board(self):
        """Input is a string of space-separated rows of N letters each;
        result is a string of size (N+2)**2 with borders all around."""
        rows = "play homx rlez ggta".split()
        b = self.border
        N = len(rows)
        rows = [b*N] + rows + [b*N]
        self.board = ''.join(b + row + b for row in rows)
        return self.board

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
