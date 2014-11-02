class Player():
    def __init__(self, location):
        """ stats for player character and wumpus """
        self.location = location
        # You can't make dead people, sorry
        self.alive = True    
        self.direction = "east"
        self.character = "> "

    def right(self):
        if self.direction == "east":
            self.direction = "north" 
            self.character = "^ "
        
        elif self.direction == "north":
            self.direction = "west"
            self.character = "< "
        
        elif self.direction == "west":
            self.direction = "south"
            self.character = "v "
        
        else:
            self.direction = "east"
            self.character = "> "

    def left(self):
        if self.direction == "east":
            self.direction = "south" 
            self.character = "v "
        
        elif self.direction == "south":
            self.direction = "west"
            self.character = "< "
        
        elif self.direction == "west":
            self.direction = "north"
            self.character = "^ "
        
        else:
            self.direction = "east"
            self.character = "> "

