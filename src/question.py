import html
import random

# Class that holds data for a particular question
class Question():
	question: str = "" # The question text
	answers: list = [] # The list of answers

	correct: str = "" # The correct answer as an string
	category: str = "" # The category of the question 
	difficulty: str = "" # The difficulty of the question

	def __init__(self, question: str = "", answers: list = [], category: str = "", difficulty: str = ""):
		self.question = self.parse_html(question)
		self.category = self.parse_html(category)
		self.difficulty = self.parse_html(difficulty)

		self.answers = self.parse_html(answers)
		self.correct = self.answers[0]
		
		random.shuffle(self.answers)

	# Parse the HTMLified string
	def parse_html(self, data: str = "") -> str | list:

		if (isinstance(data, list)):
			new_data = []

			for text in data:
				new_data.append(self.parse_html(text.strip()))

			return new_data

		return html.unescape(data)