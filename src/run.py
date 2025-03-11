import math
import random
import time

import src.utils as utils
from src.api import API
from src.commons import *

class Run():
	def __init__(self):
		pass

	# Run the menu constantly until 
	def game(self):
		score: 		int = 0
		correct: 	int = 0
		questions: list = API.get_questions()
		n: 			int	= 1

		while len(questions):
			score_received, is_correct = self.play(questions.pop(0), n, score)
			
			score += score_received
			correct += 1 if is_correct else 0

			n += 1

		utils.clear()
		print(f"Your score is {utils.format_number(score)} 💎")
		print(f"NEW HIGHSCORE!") # TODO: Implement highscore system
		print(f"✅ {correct} · ❌ {ROUND_QUESTION_COUNT - correct}")
		
		time.sleep(3)

		print()
		input("Press Enter to return to Main Menu")

	def play(self, q: dict, n: int = 1, total_score: int = 0) -> tuple:
		valid: 		bool = False
		idx: 		int  = -1
		res:		str  = ""
		is_correct: bool = False

		score: int = 0

		question_info: str 	= f"⭐️ Q{n} · {q.category} · {q.difficulty.capitalize()} · 💎 {utils.format_number(total_score)}"
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
			utils.halt_or_skip(f"✅ {random.choice(CORRECT_RESPONSES)} (+{utils.format_number(score)} 💎)")
		else:
			utils.halt_or_skip(f"❌ {random.choice(INCORRECT_RESPONSES)}")

		return (score if is_correct else 0), is_correct

	
	def show_question(self, info: str, text: str, answers: list, correct: int = -1, player_answer: int = -1) -> None:
		"""
		Summary: Show the question to the player.

		- if both correct and player_answer are -1, it means the question is being shown for the first time
		and no answer has been given yet, thus it must not show "✅" or "❌" emojis.

		- if correct and player_answer are the same, it means the player answered correctly, 
		so it must ONLY show "✅".

		- if correct and player_answer are different, it means the player answered incorrectly,
		so it must show both "✅" and "❌" emojis, for the correct and incorrect answers respectively.

		@param info: The question info
		@param text: The question text
		@param answers: The list of answers
		@param correct: The correct answer index
		@param player_answer: The player's answer index

		@return None
		"""
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