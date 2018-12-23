# +JMJ+
# Paul A Maurais
# 2018

# 121 points
# two player game only
from Player import Player
from Deck import Deck
from Hand import Hand


def main():
    players = [Player(), Player()]
    deck = Deck()
    dealerIndex = selectDealer(players, deck)
    deck.shuffle()

    while (True):
        # every turn progresses: deal, discard, play, peg
        deal(players, deck, dealerIndex)
        crib = discard(players)
        play(players, dealerIndex)
        peg(players, dealerIndex, crib)


def selectDealer(players, deck):
    '''lowest cut card deals.  If their rank matches, the first card drawn is the lowest'''
    i = 0;
    playerIndex = 0
    low = 14
    for player in players:
        temp = deck.cut()['rank']
        if temp < low:
            low = temp
            playerIndex = i
        print("player " + str(i + 1) + " drew a " + str(temp))
        i = i + 1
    players[playerIndex].dealer = True
    print("player " + str(playerIndex + 1) + " drew a the lowest card and is dealer")

    return playerIndex


def deal(players, deck, dealerIndex):
    '''Deal cards to the players in player list'''
    for i in range(0, 12):
        players[(dealerIndex + 1 + i) % len(players)].hand.addCard(deck.dealCard())


def discard(players):
    '''Promp players to discard cards and use discarded cards to build the crib. returns crib (Hand)'''
    crib = Hand()
    playerNum = 1
    for player in players:
        for i in range(0, 2):
            if i == 0:
                string = 'first'
            else:
                string = 'second'
            string = string + " card to discard: \n"
            print(player.hand)
            discardIndex = getInput(playerNum, string)
            crib.addCard(player.hand.remCard(int(discardIndex) - 1))
        playerNum += 1

    return crib


# TODO
def play(players, dealerIndex):
    '''Play of the game, prompt each user to play cards until hands are exhausted'''
    curCount = 0  # keeps track of the current play count, resets at 31
    cardStack = []
    for i in range(0, 8):
        playerIndex = (dealerIndex + 1 + i) % len(players)
        curCard = playCard(players[playerIndex], playerIndex)
        curCount += curCard.value

        if curCount > 31:
            print('That goes over 31 you doofus!')
            players[playerIndex].hand.addCard(curCard)
            i -= 1
            continue

        cardStack.append(curCard)
        checkRun(cardStack)

        if curCount == 31:
            players[playerIndex].move(2)
            curCount = 0


def playCard(player, playerIndex):
    print(player.hand)
    cardIndex = getInput(playerIndex, 'card to play or type \'pass\' to pass')
    return player.hand.remCard(cardIndex)

#TODO
def checkRun(cardStack):
    pass


# TODO
def peg(players, dealerIndex):
    pass


def getInput(playerNum, string):
    '''broken into its own function for testing'''
    return input("Player " + str(playerNum) + ' Select index of ' + string)


if __name__ == '__main__':
    main()

# +JMJ+
