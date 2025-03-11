import src.utils as utils

from src.api import API
from src.commons import *
from src.run import Run

class Selection():
	def __init__(self, name: str = "", callback: callable = None, available: bool = True):
		self.available = available
		self.name = name or "NO NAME"
		self.callback = callback if callback is not None else lambda: None
		
class Menu():
	def __init__(self, game_context = None):
		self.selection = [
			Selection("Classic Mode", self.start_classic),
			Selection("Ranked Mode", available = False),
			Selection("Survival Mode", available = False),
			Selection("Settings", available = False),
			Selection("Exit Game", self.end)
		]

		self.context = game_context

	def start_classic(self):
		return Run().game()
	
	def end(self):
		return self.context.stop()

	def menu_loop(self):
		_, last_letter = self.get_selection_data()

		while True:
			self.show_menu(API.get_question_count())

			response: str = input(f"A-{last_letter}> ").strip().upper()
			if (response):		
				cb: callable = self.parse_response(response)
				break

		return cb

	def parse_response(self, response: str) -> callable:
		idx = utils.get_idx_by_letter(response, SELECTION_LETTERS)

		if (idx == -1):
			return None
		
		if (idx >= len(self.selection)):
			return None

		if (not self.selection[idx].available):
			return None

		return self.selection[idx].callback

	def show_menu(self, count: int = 0):
		utils.clear()

		print(f"⭐️ TBTS Game - {VERSION} - Created by AntikoreDev")
		print(f"Includes {utils.format_number(count)} questions from OpenTDB")
		print()
		print(self.get_selection_string())
		print()
	
	def get_selection_data(self) -> tuple:
		count = len(self.selection)
		last_letter = SELECTION_LETTERS[count - 1]

		return count, last_letter

	def get_selection_string(self) -> str:
		selection_list: list = []
		for i, sel in enumerate(self.selection):
			selection_list.append(
				f"{SELECTION_LETTERS[i]}) {sel.name} {"" if sel.available else "🚧"}"
			)

		return "\n".join(selection_list)