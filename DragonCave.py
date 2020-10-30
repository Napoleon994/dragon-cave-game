import random
import time

def displayIntro():
	print('You are in a land full of dragons. In front of you,')
	print('you see two caves. In one cave, the dragon is friendly')
	print('and will share his treasure with you. The other dragon')
	print('is greedy and hungry, and will eat you on sight.')
	print()

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber
	print('Do you want to play again? (yes or no)')
	playAgain = input()
