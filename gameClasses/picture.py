from gameClasses.guess import GameStatus

class Picture:   
    def __init__(self):
        """Constructs a new Picture.

        Attribute:
            self (_chute): Picture of a parachute.
            self (head): O - still in the game
            self (dead_head): X - losing game.
            self (body): The jumper's body and ground
            MAX_WRONG_INPUT: 4 incorrect guess.

        
        Methods:
            draw_jumper(number of wrong answers)
        
        """

        self._chute =[" _____",
                     "/_____\ ",
                     "\     /",
                     " \   /"]
        
        self._head = "   O"
        
        self._losing_head = "   X"
        
        self._body = ["  /|\ ",
                     "  / \ ",
                     "",
                     "^^^^^^^^"] 
        
                    # [["   X"],
                    #  ["  /|\ "],
                    #  ["  / \ "]]                      
    #def display_image(self,image): ==> To insert and print in the result (terminal services)
        #print(image)
    
    def draw_jumper(self, num_wrong, game_status):
        for line in range(num_wrong, len(self._chute)):
            print(self._chute[line])

        if game_status == GameStatus.LOSE:
            print(self._losing_head)
        else:
            print(self._head)
        
        for line in range(len(self._body)):
            print(self._body[line])
        







   
#for testing:
# jumper = Picture()
# jumper.draw_jumper(0, GameStatus.WIN)
# jumper.draw_jumper(1, GameStatus.WIN)
# jumper.draw_jumper(2, GameStatus.PLAY)
# jumper.draw_jumper(3, GameStatus.PLAY)
# jumper.draw_jumper(4, GameStatus.LOSE)
