import math
import random
import sys
import time

# My other modules
import src.utils as utils
from src.api import API
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

		self.menu_loop()

	# Run the menu constantly until 
	def menu_loop(self):
		while True:
			self.menu(API.get_question_count())

	def menu(self, count: int = 0):
		utils.clear()

		print(f"⭐️ TBTS Game - {VERSION} - Created by AntikoreDev")
		print(f"Includes {count} questions from OpenTDB")
		print()
		print("A) Classic Mode\nB) Ranked Mode 🚧\nC) Survival Mode 🚧\nD) Exit Game")
		print()

		response: str = input("A-D> ").strip().upper()
		
		if (response == "A"): 
			self.game()
		elif (response == "D"): 
			self.stop()

	def game(self):
		score: 		int = 0
		correct: 	int = 0
		questions: list = API.get_questions()
		n: 			int	= 1

		while len(questions):
			score_received, is_correct = self.play(questions.pop(0), n)
			
			score += score_received
			correct += 1 if is_correct else 0

			n += 1

		utils.clear()
		print(f"Your score is {score} 💎")
		print(f"✅ {correct} · ❌ {ROUND_QUESTION_COUNT - correct}")
		
		time.sleep(3)

		print()
		input("Press Enter to return to Main Menu")

	def play(self, q: dict, n: int = 1) -> [int, bool]:
		valid: 		bool = False
		idx: 		int  = -1
		res:		str  = ""
		is_correct: bool = False

		score: int = 0

		question_info: str 	= f"⭐️ Q{n} - {q.category} - {q.difficulty.capitalize()}"
		question_text: str 	= f"{random.choice(EMOJIS)} {q.question}"
		correct_idx: int 	= q.answers.index(q.correct)
		
		init_score: float = 30
		init_time: float = time.time()

		while not valid:
			self.show_question(question_info, question_text, q.answers)

			res = input("A-D> ") # Get the player's response
			idx = utils.get_idx_by_letter(res) # Convert the player response into index

			valid = (idx >= 0) # Check if its a valid response whenever its larger than 0

		# Show the question again, this time passing the index that has been sent and the correct index for comparison
		self.show_question(question_info, question_text, q.answers, correct_idx, idx)

		
		score = max(0, math.ceil(init_score - (time.time() - init_time)) * 100) # Calculate the total score based on time spent to answer
		is_correct = (correct_idx == idx)

		if (is_correct):
			utils.halt_or_skip(f"✅ {random.choice(CORRECT_RESPONSES)} (+{score} 💎)")
		else:
			utils.halt_or_skip(f"❌ {random.choice(INCORRECT_RESPONSES)}")

		return (score if is_correct else 0), is_correct

	# Show the question at the game
	def show_question(self, info: str, text: str, answers: list, correct: int = -1, player_answer: int = -1) -> None:
		utils.clear()

		print(info)
		print(text)
		print("")

		for i, opt in enumerate(answers):
			print(f"{ANSWER_LETTERS[i]}) {opt}", end = "")

			if (player_answer == -1):
				print("")
			elif (i == correct):
				print(" ✅")
			elif (i == player_answer):
				print(" ❌")
			else:
				print("")
			
		print("")

	

	