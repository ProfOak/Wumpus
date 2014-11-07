from Tile import Tile
from Player import Player

class Wumpus():
    def __init__(self, size=10):
        """ Initiate a wumpus game, default size = 10 """
        self.size = size
        # Board determined by size
        self.world = [ [ Tile() for t in range(size)] for i in range(size) ]
        
        self.player = Player([0, 0])
        self.world[1][1].add("W")
        self.world[2][2].add("b")


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
                    print self.player.character,
                elif self.world[i][j].has_death():
                    print "! ",
                elif self.world[i][j].has_hazard():
                    print "? ",
                else:
                    print "# ",
            print
    def message(self, msg1, msg2="", msg3=" "):
        """ output a message to the screen of a specific format """

        """
        EXAMPLE
        ====================================
        | You are facing south [1, 2]
        | You move forward
        | It stinks in here!
        | You meet the Wumpus (RIP)
        | It's cold in here!
        | It's a long drop (RIP)
        | Oo shiny!
        | You found the gold! Congrats!
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
        last_cmd_msg = "Welcome to the Wumpus World"
        while self.player.alive or self.wumpus.alive:

            self.message(last_cmd_msg, "You are facing %s %s" % (self.player.direction, self.player.location))
            self.print_board()
            cmd = raw_input("> ")
            if cmd == "q":
                break
            # movement controls

            elif cmd == "f":
                # move forward
                d = self.player.direction
                if d == "west" and self.player.location[1] != 0:
                    self.player.location[1] -= 1
                elif d == "east" and self.player.location[1] != self.size - 1:
                    self.player.location[1] += 1
                elif d == "north" and self.player.location[0] != 0:
                    self.player.location[0] -= 1
                elif d == "south" and self.player.location[0] != self.size - 1:
                    self.player.location[0] += 1
                else:
                    last_cmd_msg = "There's a wall in your path"
                    continue
                last_cmd_msg = "You have moved forward"
                # /move forward

            elif cmd == "l":
                self.player.left()
            elif cmd == "r":
                self.player.right()
            # /movement controls
            else:
                last_cmd_msg = "Sorry, didn't understand that command"

Wumpus(4).game_loop()

