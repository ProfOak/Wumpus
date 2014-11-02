from Tile import Tile
from Player import Player

class Wumpus():
    def __init__(self, size=10):
        """ Initiate a wumpus game """
        self.size = size
        # Board determined by size
        self.world = [ [ Tile() for t in range(size)] for i in range(size) ]
        self.world[0][0].player = True
        
        self.player = Player([0, 0])

        # generate random location for wumpus
        # wumpus is a non-moving player
        self.wumpus = Player([1, 1])
        # generate smells

        # generate pits

        # generate breezes

        # generate random gold location, can be same as Wumpus
        
    
    def print_board(self):
        """ Printing the board, used for the wumpus world """
        for i in range(self.size):
            for j in range(self.size):
                if self.player.location == [i, j]:
                    print "P ",
                else:
                    print "# ",
            print
    def message(self, msg1, msg2="", msg3=" "):
        """
        ====================================
        | (1, 1) | sbWPG
        | You move left!
        | It stinks in here!
        | It's cold in here!
        | You meet the Wumpus (RIP)
        | It's a long drop from here! (rip)
        =====================================

        """
        print "==========================================="
        print "|%s" % msg2 # status messages (location, contents of tile)
        print "|%s" % msg1 # main message
        for m in msg3:
            print "|%s" % m # personalized message based on context
        print "==========================================="
    def game_loop(self):
        """ Game driver """
        # resolve 
        while self.player.alive or self.wumpus.alive:
            self.print_board()
            cmd = raw_input("> ")
            if cmd == "q":
                break
            # movement controls
            elif cmd == "l" and self.player.location[1] != 0 :
                self.player.location[1] -= 1
                self.message("You have moved left!")
            elif cmd == "r" and self.player.location[1] != self.size - 1:
                self.player.location[1] += 1
                self.message("You have moved right!")
            elif cmd == "u" and self.player.location[0] != 0:
                self.player.location[0] -= 1
                self.message("You have moved up!")
            elif cmd == "d" and self.player.location[0] != self.size - 1:
                self.player.location[0] += 1
                self.message("You have moved down!")
            # /movement controls
            else:
                self.message("Sorry, didn't understand that command")
w = Wumpus(4).game_loop()

