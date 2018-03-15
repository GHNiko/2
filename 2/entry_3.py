import random

class Card(object):
    
    colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                 '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, color=0, value=0):
        self.color = color
        self.value = value


    def __str__(self):
        return '{} {}'.format(Card.values[self.value],
                            Card.colors[self.color])

# Example1:
# input: >>> print(Card(1,11))
# output: Jack Diamonds


# Example2:
# return '%s of %s' % (Card.colors[self.color],
#                            Card.values[self.value])
# input: >>> print(Card(1, 2))
# output: Diamonds of 2
# input: >>> print(Card(1,12))
# output: Diamonds of Queen

## class Deck(object):
##
##     def __init__(self):
##         self.cards = []
##         for color in range(4):
##             for value in range(1, 4):
##                 card = Card(color, value)
##                 self.cards.append(card)
