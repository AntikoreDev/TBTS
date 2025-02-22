import sys

# My other modules
import src.utils as utils
from src.api import API
from src.menu import Menu
from src.commons import *

# Class that holds the game script
class Game():	
	def __init__(self) -> None:
		API.initialize()

	# This is run when the game ends completely
	def stop(self):
		utils.clear()
		
		print(f"Thanks for playing TBTS!\nSee you next time!\n\nMade by AntikoreDev.\nSource available at {GITHUB_REPO} 📦")
		sys.exit(0)

	# This run at the very start of the game
	def start(self):
		print("Loading...")
		menu: Menu = Menu(self)

		while True:
			cb: callable = menu.menu_loop()
			if (cb is not None):
				cb()

	

	

	