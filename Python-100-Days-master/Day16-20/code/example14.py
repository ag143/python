"""
object oriented
Enumerations - There are only a limited number of options for the value of a variable, the most suitable type is an enumeration
By enumeration we can define symbolic constants, which are better than literal constants
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """Suit (enumeration)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """Card"""
    
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        suites = ('♠️', '♥️', '♣️', '♦️')
        faces = ('', 'A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{suites[self.suite.value]} {faces[self.face]}'


class Poker():
    """poker"""
    
    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """Shuffle"""
        self.index = 0
        random.shuffle(self.cards)

    def deal(self):
        """Licensing"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        """Are there more cards"""
        return self.index < len(self.cards)


class Player():
    """Player"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """Draw a card"""
        self.cards.append(card)

    def arrange(self):
        """Organize the cards in hand"""
        self.cards.sort(key=lambda card: (card.suite, card.face))


def main():
    """Main function"""
    poker = Poker()
    poker.shuffle()
    players = [
        Player('East evil'), Player('West poison'),
        Player('Southern Emperor'), Player('Northern Beggar')
    ]
    while poker.has_more:
        for player in players:
            player.get_card(poker.deal())
    for player in players:
        player.arrange()
        print(player.name, end=': ')
        print(player.cards)


if __name__ == '__main__':
    main()