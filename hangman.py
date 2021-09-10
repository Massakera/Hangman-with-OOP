# Hangman Game 
# Game made using OOP progamming 

# Import
import random

# Board 
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:


	# Construct method
	def __init__(self, word):	
		self.word = word
		self.missed_letters = []
		self.guessed_letters = []
		
	# Letter guess method
	def guess(self, letter):
		if letter in self.word and letter not in self.guessed_letters:
			self.guessed_letters.append(letter)
		elif letter not in self.word and letter not in self.missed_letters:
			self.missed_letters.append(letter)
		else:
			return False
		return True
		
	# Endgame method
	def hangman_over(self):
		return self.hangman_won() or (len(self.missed_letters) == 6)
		
	# Win check method
	def hangman_won(self):
		if '_' not in self.hide_word():
			return True
		return False
		
	# Hide letters method
	def hide_word(self):
		rtn = ''
		for letter in self.word:
			if letter not in self.guessed_letters:
				rtn += '_'
			else:
				rtn += letter
		return rtn
		
	# Game status method
	def print_game_status(self):
		print (board[len(self.missed_letters)])
		print ('\nWord: ' + self.hide_word())
		print ('\nWrong letters: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Correct letters: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()

# Query of words in the document
def rand_word():
        with open("words.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()

# Main method
def main():

	# Object
	game = Hangman(rand_word())

	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\nGuess a letter: ')
		game.guess(user_input)

	# Verify the game status
	game.print_game_status()	

	# Messages of the game
	if game.hangman_won():
		print ('\nCongratulations! You won!!')
	else:
		print ('\nGame over! You lost.')
		print ('The correct word was ' + game.word)
		
	print ('\nIt was a good game!\n')

# Execute the game		
if __name__ == "__main__":
	main()