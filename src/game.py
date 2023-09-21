import math
import os
import random
import sys
import time

import keyboard
import requests

from .commons import *
from .question import Question

# Class that holds the game script
class Game():
	token: str = "" # OpenTDB Session Token
	question_count: int = 0 # For statistical purposes, OpenTDB question count
	
	def stop(self):
		self.clear()
		print(f"Thanks for playing TBTS!\nSee you next time!\n\nMade by AntikoreDev.\nSource available at {GITHUB_REPO} 📦")
		sys.exit(0)
		
	def clear(self):
		os.system("cls" if os.name == "nt" else "clear")

	def start(self):
		print("Loading...")
		self.token = self.get_token()
		self.question_count = self.get_question_count()

		self.menu_loop()

	def menu_loop(self):
		while True:
			self.menu(self.question_count)

	def menu(self, count = 0):
		self.clear()

		print(f"⭐️ TBTS Game - v{VERSION} - Created by AntikoreDev")
		print(f"Includes {count} questions from OpenTDB")
		print()
		print("A) Classic Mode\nB) Ranked Mode 🚧\nC) Survival Mode 🚧\nD) Exit Game")
		print()

		response: str = input("A-B> ").strip().upper()
		
		if (response == "A"): self.game()
		elif (response == "D"): self.stop()

	def game(self):
		score = 0
		correct = 0
		questions, n = self.get_questions(), 1

		while len(questions):
			score_received, is_correct = self.play(questions.pop(0), n)
			
			score += score_received
			correct += 1 if is_correct else 0

			n += 1

		self.clear()
		print(f"Your score is {score} 💎")
		print(f"✅ {correct} · ❌ {15 - correct}")
		
		time.sleep(3)

		print()
		input("Press Enter to return to Main Menu")

	def get_question_count(self):
		data = self.fetch("https://opentdb.com/api_count_global.php")
		return data["overall"]["total_num_of_verified_questions"]

	def get_token(self):
		data = self.fetch("https://opentdb.com/api_token.php?command=request")
		return data["token"]

	def halt_or_skip(self, text):
		print(text)

		check_time = 0.1
		s = 0
		while s < 3:
			time.sleep(check_time)
			s += check_time

			if (keyboard.is_pressed("enter") and s > 0.5):
				return True
		return True

	def play(self, q, n = 1):
		valid, idx = False, -1

		question_info = f"⭐️ Q{n} - {q.category} - {q.difficulty.capitalize()}"
		question_text = f"{random.choice(EMOJIS)} {q.question}"
		correct_idx = q.answers.index(q.correct)
		
		init_score = 30
		init_time = time.time()

		while not valid:
			self.show_question(question_info, question_text, q.answers)

			res = input("A-D> ")
			idx = self.get_idx_by_letter(res)

			valid = (idx >= 0)

		self.show_question(question_info, question_text, q.answers, correct_idx, idx)

		score = max(0, math.ceil(init_score - (time.time() - init_time)) * 100)

		is_correct = correct_idx == idx
		if (is_correct):
			self.halt_or_skip(f"✅ {random.choice(CORRECT_RESPONSES)} (+{score} 💎)")
		else:
			self.halt_or_skip(f"❌ {random.choice(INCORRECT_RESPONSES)}")

		return (score if is_correct else 0), is_correct

	def show_question(self, info, text, answers, correct = -1, player_answer = -1):
		global letters

		self.clear()

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

	def get_idx_by_letter(self, letter: str):
		letters = list("ABCD")
		
		try:
			return letters.index(letter.strip().upper())
		except:
			return -1

	def reset_token(self):
		self.fetch(f"https://opentdb.com/api_token.php?command=reset&token={self.token}")

	def get_questions(self):
		data: dict = self.fetch(f"https://opentdb.com/api.php?amount=15&type=multiple&token={self.token}")
		questions: list = []

		# If the current session token has been exhausted
		if (data["response_code"] == 4):
			self.reset_token()
			return self.get_questions()

		for r in data["results"]:
			answers = list(r["incorrect_answers"])
			answers.append(r["correct_answer"])
			answers.reverse()

			questions.append(Question(r["question"], answers, r["category"], r["difficulty"]))

		return questions

	def fetch(self, url):
		try:
			response = requests.get(url)
			
			# If response is OK
			if (response.status_code == 200):
				data = response.json()  
				return data
			return None
		
		except Exception as e:
			print("Error:", e)
			return None