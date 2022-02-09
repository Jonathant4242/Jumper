from gameClasses.random_word import Random_word
from enum import Enum, auto

class GameStatus(Enum):
    WIN = auto()
    LOSE = auto()
    PLAY = auto()

class Guess:
    """The responsibility of this class is to generate a series of blank spaces matching the number of letters in the word to be guessed. It will fill in the blanks with the correct letter as the player guesses them. It will keep track of wrong guesses.
    
    Attributes:
        word: the word the player is trying to guess. 
        
        blanks: starts with empty blanks and fills in letters as correctly guessed. 
        
        guessed_letter: the letter the player guessed 
        
        num_wrong_guesses: how many times the player has guessed wrong

        max_num_wrong_guesses: 4
        
        game_status: says if game still in play, or ended in a win or loss.

        guess = chosen input from user.

    """
    def __init__(self):
        """Constructs a new guess.
        
        Arguments: 
            self (Guess): an instance of Guess"""
        self.word = ""
        self.puzzle = ""
        self.guessed_letters = []
        self.guess = ""
        self.num_wrong_guesses = 0
        self.MAX_NUM_WRONG_GUESSES = 4
        

    def set_word(self):
        """This method gets a random word from the Random_word class.
        
        Args: 
            self (Guess): An instance of Guess"""

        random_word = Random_word()
        self.word = random_word.generate_word()
        self.puzzle = ""
        for i in range(len(self.word)):
            self.puzzle = self.puzzle + "_ "

    def _update_puzzle(self):
        found = False
        pos = -1
        while True:
            pos = self.word.find(self.guess, pos+1)
            if pos == -1:
                break
            new_puzzle = ""
            new_puzzle = self.puzzle[:(pos*2)]
            new_puzzle = new_puzzle + self.guess
            new_puzzle = new_puzzle + self.puzzle[(pos*2)+1:]
            self.puzzle = new_puzzle
            found = True
        if not found:
            self.num_wrong_guesses += 1

    # _compare: compare guess to chosen word

    def make_guess(self):
        while True:
            choice = input('Guess a letter [A-Z] : ').lower()
            if len(choice) == 1:
                if choice.isalpha():
                    if choice in self.guessed_letters:
                        print("You already guessed this letter. Please try again.")
                    else:
                        self.guessed_letters.append(choice)
                        self.guess = choice
                        break
                else:
                    print("Please enter a letter.")
            else:
                print('Please enter one letter.')
        self._update_puzzle()


    def display_puzzle(self):
        print(self.puzzle)


    def get_num_wrong(self):
        return self.num_wrong_guesses
        

    def get_game_status(self):
        """This method determines if the game is still being played, has been won, or has been lost.
        
        Args:
            Self (Guess): an instance of Guess."""

        if self.num_wrong_guesses >= self.MAX_NUM_WRONG_GUESSES:
            # self.game_status = "Game over, you lost!"
            return GameStatus.LOSE

        if self.puzzle.find("_") == -1:
            # self.game_status = "Correct!, You won"
            return GameStatus.WIN

        # self.game_status = "Still playing"
        return GameStatus.PLAY

#code for testing:

# guess = Guess()
# guess.set_word()
# print(f'\nrandom word: {guess.word}')

# guess.make_blanks()
# print(*guess.blanks, sep='')

# guess.update_blanks('e')
# print(f'your guess is: {guess.guessed_letter}')
# print(f'your guess index is: {guess.guess_index}')
# print(f'number of wrong guesses: {guess.num_wrong_guesses}')

# separator = ''
# cleaned_blanks = separator.join(guess.blanks)
# print(f'updated blanks: {cleaned_blanks}')

# guess.get_game_status()
# print(f'game status: {guess.game_status}\n')

"""Methods:
   
    
    
    
    display_puzzle:
    display_guesses: above and beyond"""