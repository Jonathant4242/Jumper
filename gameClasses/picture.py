class Picture:   
    def __init__(self):
    # 2) Create the class constructor. Use the following method comment.
        """Constructs a new Picture.

        Attribute:
            self (chute): Picture of a parachute.
            self (head): O - still in the game
            self (dead_head): X - losing game.
            self (body): The jumper's body and ground
            MAX_WRONG_INPUT: 4 incorrect guess.

        
        Methods:
            draw_jumper(number of wrong answers)
        
        """
        self.chute =[[" _____"],
                     ["/_____\ "],
                     ["\     /"],
                     [" \   /"],
                     ["   O"],
                     ["  /|\ "],
                     ["  / \ "],
                     ["^^^^^^^^"]] 
        
                    # [["   X"],
                    #  ["  /|\ "],
                    #  ["  / \ "]]                      
    #def display_image(self,image): ==> To insert and print in the result (terminal services)
        #print(image)
    
    def draw_jumper(self, num_wrong):
        for line in range(num_wrong, len(self.image)):
            print(self.image[line][0])

    def draw_zero_wrong(self):
        print('  _____  ')
        print(' /_____\\')
        print(' \\     /')
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')

    def draw_one_wrong(self):
        print(' /_____\\')
        print(' \\     /')
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')
    def draw_two_wrong(self):
        print(' \\     /')
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')
    def draw_three_wrong(self):
        print('  \\   /')
        print('    O')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')
    def draw_four_wrong(self):
        print('    X')
        print('   /|\\')
        print('   / \\')
        print('')
        print('^^^^^^^^^')


   
#for testing:
jumper = Picture()
jumper.draw_jumper(0)
jumper.draw_jumper(1)
jumper.draw_jumper(2)
jumper.draw_jumper(3)
jumper.draw_jumper(4)
# jumper.draw_zero_wrong()
# jumper.draw_one_wrong()
# jumper.draw_two_wrong()
# jumper.draw_three_wrong()
# jumper.draw_four_wrong()