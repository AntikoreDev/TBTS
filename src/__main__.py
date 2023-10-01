from src.game import Game

# This function defines the game object and initializes it
def main():
	game = Game() # Instantiate a game object
	
	try:
		game.start()

	# Whenever the user interrupts the terminal with Ctrl+C or similar, stop the game without raising an error
	except KeyboardInterrupt:
		game.stop()