import json
import random
import os

men = [
	'''
	 ╔══════╗
	 ║
	 ║
	 ║
	 ║
	═╩═
	''',
	'''
	 ╔══════╗
	 ║     ( )
	 ║
	 ║
	 ║
	═╩═
	''',
	'''
	 ╔══════╗
	 ║     ( )
	 ║      |
	 ║      |
	 ║
	═╩═
	''',
	'''
	 ╔══════╗
	 ║     ( )
	 ║      |
	 ║      |
	 ║     /
	═╩═
	''',
	'''
	 ╔══════╗
	 ║     ( )
	 ║     \\|
	 ║      |
	 ║     /
	═╩═
	''',
	'''
	 ╔══════╗
	 ║     ( )
	 ║     \\|
	 ║      |
	 ║     / \\
	═╩═
	''',
	'''
	 ╔══════╗
	 ║     (x)
	 ║     \\|/
	 ║      |
	 ║     / \\
	═╩═
	'''
]

def searchString(character, string):
	return [i for i, c in enumerate(string) if c == character]

def fetchWord():
	with open("./words.json", "r") as file:
		words = json.load(file)
	
	return words[int(random.uniform(0, len(words) - 1))]

def gameLoop():
	won = False
	tries = 0
	word = fetchWord()
	guessedWord = ['_' for i in range(len(word))]
	letters = "abcdefghijklmnopqrstuvwxyz"
	incorrectGuesses = []

	TOP_LEFT = '╔'
	TOP_RIGHT = '╗'
	BOTTOM_LEFT = '╚'
	BOTTOM_RIGHT = '╝'
	HORIZONTAL = '═'
	VERTICAL = '║'
	LTR_SEPARATOR = '╠'
	RTL_SEPARATOR = '╣'
	TTB_SEPARATOR = '╦'
	BTT_SEPARATOR = '╩'
	CNT_SEPARATOR = '╬'
	SPACE = ' '
	BOX_SIZE = 45

	while not won and tries <= 7:
		os.system('cls' if os.name == 'nt' else 'clear')

		print(TOP_LEFT + "".join([HORIZONTAL for i in range(BOX_SIZE - 2)]) + TOP_RIGHT)
		print(VERTICAL + "".join([SPACE for i in range(int(BOX_SIZE / 3 - 3))]) + 'Welcome to Hangman!' + "".join([SPACE for i in range(int(BOX_SIZE / 3 - 3))]) + VERTICAL)
		print(BOTTOM_LEFT + "".join([HORIZONTAL for i in range(BOX_SIZE - 2)]) + BOTTOM_RIGHT)

		print(men[tries])

		displayGuessedWord = " ".join(guessedWord)
		print(f'You\'ve Guessed: \n{displayGuessedWord}\n')
	
		print(f'You can\'t use:\n{" ".join(incorrectGuesses)}\nbecause you\'ve proven them to be not in the word!\n')

		if "".join(guessedWord) == word:
			print('Congratulations! You Win!')
			if input('Would you like to retry the game? (y/n): ') == 'y':
				gameLoop()
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
				print('Thank you so much for playing Hangman!')
				exit()

		input1 = input('Your Guess: ')

		if input1 == 'dev_showWord':
			print(word)
			input()
			continue

		if len(input1) > 1:
			print('Guess must not be more than one letter at a time.')
			input()
			continue

		if searchString(input1, letters) == []:
			print('Guess must be a letter in the English Alphabet.')
			input()
			continue

		if searchString(input1, word):
			indices = searchString(input1, word)
			
			print('Congrats! You got it right!')

			for i in range(len(indices)):
				guessedWord[indices[i]] = input1
			
			input()
			continue

		if searchString(input1, incorrectGuesses):
			print('You can\'t use a letter you\'ve guessed before!')
			input()
			continue

		print('Sorry, That letter isn\'t in the word!')
		
		incorrectGuesses.append(input1)

		tries += 1

		input()
		continue
	
	print(f'You Lost! Better Luck next time!\nThe word was: {word}')
	
	if input('Would you like to retry the game? (y/n): ') == 'y':
		gameLoop()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Thank you so much for playing Hangman!')
		exit()