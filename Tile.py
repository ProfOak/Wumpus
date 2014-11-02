class Tile():
    def __init__(self, wumpus=False, pit=False, gold=False, player=False, smell=False, breeze=False):
        """ Each tile on the board is this """
        # a tile can possibly contain =  WsPbD
        # Used for printing purposes only
        # W = wumpus
        # s = Smell
        # P = Pit
        # b = Breeze
        # G = Gold
        self.contains = ""
        
        """
        self.wumpus = wumpus
        self.smell = smell
        self.pit = pit
        self.breeze = breeze
        self.gold = gold
        # self.player = player
        """
    
    def add(self, s):
        if s not in self.contains:
            self.contains += s

    def to_string(self):
        s = ""
        # upper case for fatal dangers
        # lower case for dangerous indicators

        if self.wumpus:
            s += "W"
        elif self.smell:
            s += "s"
        elif self.pit:
            s += "P"
        elif self.breeze:
            s += "b"
        elif self.gold:
            s += "G"

        return s

