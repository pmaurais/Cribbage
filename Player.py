#+JMJ+
#Paul A Maurais
#2018

from Hand import Hand

class Player:

    def __init__(self):
        self.hand=Hand()
        self.dealer=False
        self.frontPeg=0
        self.backPeg=0

    def move(self,distance=0):
        self.backPeg=self.backPeg
        self.frontPeg=self.frontPeg+distance

    def scoreHand(self):
        #TODO generate methood to auto score and devise user scoring methood
        pass

#+JMJ+