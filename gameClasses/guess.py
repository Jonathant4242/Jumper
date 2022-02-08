from random_word import Random_word

class Guess:
    """The responsibility of this class is to generate a series of blank spaces matching the number of letters in the word to be guessed. It will fill in the blanks with the correct letter as the player guesses them. It will keep track of wrong guesses.
    
    Attributes:
        word: the word the player is trying to guess. 
        
        blanks: starts with empty blanks and fills in letters as correctly guessed. 
        
        guessed_letter: the letter the player guessed 
        
        num_wrong_guesses: how many times the player has guessed wrong
        
        guess_index: a list composed of the indices at which the guessed letter is located in the random  word. If this is an empty list the player has guessed wrong.
        
        game_status: says if game still in play, or ended in a win or loss.

    """
    def __init__(self):
        """Constructs a new guess.
        
        Arguments: 
            self (Guess): an instance of Guess"""
        self.word = ''
        self.blanks = []
        self.guessed_letter = ''
        self.num_wrong_guesses = 0
        self.guess_index = []
        self.game_status = ''

    def set_word(self):
        """This method gets a random word from the Random_word class.
        
        Args: 
            self (Guess): An instance of Guess"""

        random_word = Random_word()
        self.word = random_word.generate_word()

    def make_blanks(self):
        """Generates a list composed of blank spaces ("_ "). It makes one space for each of the letters in the random word.
        
        Args:
            Self (Guess): An instance of Guess"""

        for i in range(len(self.word)):
            self.blanks.append('_ ')
            
            #this is the code to remove all the brackets and commas when printing self.blanks: 
            #print (*self.blanks, sep='')


    def update_blanks(self, player_guess):
        """This method finds the index of the guessed letter in the random word. It stores the indices in the list "guess_index". It replaces a blank with the guessed letter at the appropriate index. Adds 1 to num_wrong_guesses if the guess_index is empty.
        
        Args:
            Self (Guess): An instance of Guess
            player_guess: the letter the player guessed."""
            
        self.guessed_letter = player_guess

        #go through the word to see if the guessed letter is in it. 
        # If the letter is there it will put it's index in the list 'guess_index'
        # If the letter isn't there, guess_index will be empty and num_wrong guesses will increase by one.        
        for pos,char in enumerate(self.word):
            if(char == self.guessed_letter):
                self.guess_index.append(pos)
        if self.guess_index == []:
            self.num_wrong_guesses += 1   
        #print(self.guess_index)
        #print(self.numb_wrong_guesses)

        #This replaces the blank with the letter guessed
        for i in self.guess_index:
            self.blanks[i] = self.guessed_letter
            
            #print(i)

        #print(*self.blanks, sep='')
    
    def get_game_status(self):
        """This method determines if the game is still being played, has been won, or has been lost.
        
        Args:
            Self (Guess): an instance of Guess."""

        if self.num_wrong_guesses >= 4:
            self.game_status = "Game over, you lost!"
        if len(self.guess_index) == len(self.word):
            self.game_status = "Correct!, You won"
        else:
            self.game_status = "Still playing"

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