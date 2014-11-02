class Tile():
    def __init__(self, wumpus=False, pit=False, gold=False, player=False, smell=False, breeze=False):
        """ Each tile on the board is this """
        self.wumpus = wumpus
        self.smell = smell
        self.pit = pit
        self.breeze = breeze
        self.gold = gold
        self.player = player



