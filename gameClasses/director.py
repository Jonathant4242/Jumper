from gameClasses.guess import Guess, GameStatus
from gameClasses.picture import Picture

"""attrubites:
    picture
    guess

methods:
    start game
    _take_turn
    _display_terminal_output
    __int__"""

class Director:
    
    def __init__(self) -> None:
        self.guess = Guess()
        self.picture = Picture()
        self._game_status = GameStatus.PLAY
    

    def start_game(self):
        self.guess.set_word()
        while True:
            self._display_terminal_output()
            self._take_turn()
            if self._game_status != GameStatus.PLAY:
                break
        self._display_terminal_output()
        if self._game_status == GameStatus.WIN:
            print('You successfully landed your jump!')
        else:
            print('You had a rough landing. Ambulance is on the way!')


    def _take_turn(self):
        self.guess.make_guess()
        self._game_status = self.guess.get_game_status()

    def _display_terminal_output(self):
        print("")
        self.guess.display_puzzle()
        print("")
        self.picture.draw_jumper(self.guess.get_num_wrong(), self._game_status)
