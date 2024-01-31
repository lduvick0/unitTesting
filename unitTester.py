from numpy import random as rand
# Task: Write unit tests for several functions related to a poker game based on only spades.
# All of the functions will deal with strings from this tuple:
cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
cValue=(2,3,4,5,6,7,8,9,10,11,12,13,14)
# These correspond to the cards 2 of Spades, 3 of Spades, and so on through Jack, Queen, King, and Ace of Spaced.
# S2 has numerical value 2. S3 has numerical value 3, and so on. SJ has numerical value 111, SQ has value 12, SK has value 13,
# and SA has value 14.
# You can type this in a word processing document, or a notepad, or even on paper.
# Write up test cases for each of the following functions. You don’t need to write as many as possible,
# but you need to write enough to give high confidence the function performs correctly.
def check_straight(card1, card2, card3):
    card1Name = cards.index(card1)
    card2Name = cards.index(card2)
    card3Name = cards.index(card3)
    card1Value = cValue[card1Name]
    card2Value = cValue[card2Name]
    card3Value = cValue[card3Name]
    cardOrder=[card1Value,card2Value,card3Value]
    cardOrder.sort()
    if cardOrder[1] == (cardOrder[0] + 1) and cardOrder[2] == (cardOrder[1] + 1):
        return cardOrder[2]
    else:
        return 0
# If the cards passed in are three cards in a sequence, this function returns the greatest value.
# Otherwise, it returns 0. For example, check_straight('S5','S6','S7') would return 7. check_straight('S6', 'S5', 'S7') would also return 7.
# check_straight('S3','SQ','SK') would return 0. Come up with several tests.
def check_3ofa_kind(card1, card2, card3):
    card1Name = cards.index(card1)
    card2Name = cards.index(card2)
    card3Name = cards.index(card3)
    card1Value = cValue[card1Name]
    card2Value = cValue[card2Name]
    card3Value = cValue[card3Name]
    if card1Value==card2Value and card3Value==card1Value:
        return card1Value
    else:
        return 0

# If the three cards passed in are all the same, return the value. Otherwise return 0.
# For example, check_3ofa_kind('S9', 'S9', 'S9') would return 9. check_3ofa_kind('S2', 'S4', 'S2') would return 0.
def check_royal_flush(card1, card2, card3):

    if check_straight(card1, card2, card3)==14:
        return 14
    else:
        return 0
# (The code in this function will make use of the check_straight function from earlier, and will assume it’s been tested already and
# is functioning correctly.) If the cards passed in are a straight with the value of 14, then this function returns 14.
# Otherwise, it returns 0. For this one, you only need maybe three tests.
def play_cards(left1, left2, left3, right1, right2, right3):
    leftScore=0
    rightScore=0
    if check_royal_flush(left1, left2, left3)!=0:
        leftScore=check_royal_flush(left1, left2, left3)
    elif check_straight(left1, left2, left3) != 0:
        leftScore=check_straight(left1, left2, left3)
    elif check_3ofa_kind(left1, left2, left3) != 0:
        leftScore=check_3ofa_kind(left1, left2, left3)

    if check_royal_flush(right1, right2, right3) != 0:
        rightScore=check_royal_flush(right1, right2, right3)
    elif check_straight(right1, right2, right3) != 0:
        rightScore=check_straight(right1, right2,right3)
    elif check_3ofa_kind(right1, right2, right3) != 0:
        rightScore=check_3ofa_kind(right1, right2, right3)

    if leftScore > rightScore:
        return -1
    elif leftScore < rightScore:
        return 1
    elif leftScore == rightScore:
        return 0
    #check hands through each check individually, create value storage for return value and int linked to which hand left and right has

play_cards('S2','S3','S3', 'SQ','SK','SA')


# This method takes three cards for the left player (left1, left2, left3) and three cards for the right player (right1, right2, right3)
# and determines who wins.
# If left wins, it returns -1.
# If neither win (a draw), it returns 0.
# If right wins, it returns 1.
#
# Here’s how play_cards determines the winner:
# If both players play a straight, the highest value wins. (If both straights have the same value, the game is a draw.)
# If both players have three-of-a-kind, the higher value wins. (If they’re the same, it’s a draw.)
# If one player plays a straight and the other has a three-of-a-kind, the straight wins regardless of value.
# If one player plays a royal flush and the other doesn’t, the flush wins.
# In all other cases, it’s a draw.
