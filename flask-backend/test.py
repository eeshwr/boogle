from boogle_solve import boogle


def test():

    game = boogle()

    game.deck = ['p', 'l', 'a', 'y', 'h', 'o', 'm',
                 'x', 'r', 'l', 'e', 'z', 'g', 'g', 't', 'a', ]

    game.board = game.add_boarders()

    assert game.board == '+++++++play++homx++rlez++ggta+++++++'

    game.words = set(["play", "lay", "home", "hole", "role", "leg", "egg", "get",
                      "eat", "let", "tea", "max", "hoax", "meat", "mole", "ram", "hari", "mohan"])

    game.prefixes = set([word[:i]
                         for word in game.words for i in range(len(word))])

    assert game.possible_words() == set(["play", "lay", "home", "hole", "role",
                                         "leg", "egg", "get", "eat", "let", "tea", "max", "hoax", "meat", "mole"])

    neighbours = game.neighbours(20, 6)

    neighbours.sort()

    assert neighbours == [13, 14, 15, 19, 21, 25, 26, 27]

    return 'tests pass'
