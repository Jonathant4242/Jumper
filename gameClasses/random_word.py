import random

class Random_word:
	"""The responsibility of the Random_word class is to generate a random word for use in the game.
	Arguments: 
		Self (Random_word): an instance of Random_word. """
	
	def __init__(self):
		self.word = ''
	
	def generate_word(self):
		"""This method generates a random word for the game. It uses the file prophets.txt as its word bank
		
		Returns:
			word: a random word for use in the Jumper game"""
		
		with open("gameClasses\prophets.txt", "r") as _file:
			_allText = _file.read()
			_words = list(map(str, _allText.split()))
			self.word = random.choice(_words)
			return self.word
			
			
#test code:
#random_word = Random_word()
#word = random_word.generate_word()
#print(word)