import src.utils as utils
from src.commons import *
from src.question import Question

"""
API class with functions regarding requests to the OTDB
"""
class API():
	__api_token: str = ""
	__available_questions: int = 0

	@staticmethod
	def initialize():
		API.__available_questions = API.__get_question_count()
		API.__api_token = API.get_token()

	# Reset API's token
	@staticmethod
	def reset_token() -> None:
		utils.fetch(f"https://opentdb.com/api_token.php?command=reset&token={API.__api_token}")

	# Get a new API token
	@staticmethod
	def get_token() -> str:
		data: dict = utils.fetch("https://opentdb.com/api_token.php?command=request")
		return data["token"]
	
	# Get a list of questions
	@staticmethod
	def get_questions() -> list:

		# Get a bunch of questions from the API and create an array of questions
		data: dict = utils.fetch(f"https://opentdb.com/api.php?amount={ROUND_QUESTION_COUNT}&type=multiple&token={API.__api_token}")
		questions: list = []

		# If the current session token has been exhausted
		if (data["response_code"] == 4):
			API.reset_token()
			return API.get_questions()

		# Receive a bunch of questions
		for r in data["results"]:
			answers = list(r["incorrect_answers"])
			answers.append(r["correct_answer"])
			answers.reverse()

			questions.append(Question(r["question"], answers, r["category"], r["difficulty"]))

		return questions
	
	# Get the total verified questions from the API
	@staticmethod
	def __get_question_count() -> int:
		data: dict = utils.fetch("https://opentdb.com/api_count_global.php")
		return data["overall"]["total_num_of_verified_questions"]
	
	# Return the API's total available question and expose them to the rest of the classes
	@staticmethod
	def get_question_count():
		return API.__available_questions