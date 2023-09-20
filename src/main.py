import requests, random, os, sys, time, keyboard, math
from question import Question
from generics import *

# OpenTDB Session Token
token, question_count = "", 0

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def start():
	global token, question_count

	print("Loading...")
	token = get_token()
	question_count = get_question_count()

	menu_loop()

def menu_loop():
	while True:
		menu(question_count)

def menu(count = 0):
	clear()

	print(f"⭐️ TBTS Game - v{VERSION} - Created by AntikoreDev")
	print(f"Includes {count} questions from OpenTDB")
	print()
	print("A) Play Game\nB) Exit")
	print()

	response = input("A-B> ").strip().upper()
	
	if (response == "A"): game()
	elif (response == "B"): 
		clear()
		print("Bye!")
		sys.exit(0)

def game():
	score = 0
	correct = 0
	questions, n = get_questions(), 1

	while len(questions):
		score_received, is_correct = play(questions.pop(0), n)
		
		score += score_received
		correct += 1 if is_correct else 0

		n += 1

	clear()
	print(f"Your score is {score} 💎")
	print(f"✅ {correct} · ❌ {15 - correct}")
	
	time.sleep(3)

	print()
	input("Press Enter to return to Main Menu")

def get_question_count():
	data = fetch("https://opentdb.com/api_count_global.php")
	return data["overall"]["total_num_of_verified_questions"]

def get_token():
	data = fetch("https://opentdb.com/api_token.php?command=request")
	return data["token"]

def halt_or_skip(text):
	print(text)

	check_time = 0.1
	s = 0
	while s < 3:
		time.sleep(check_time)
		s += check_time

		if (keyboard.is_pressed("enter") and s > 0.5):
			return True
	return True

def play(q, n = 1):
	valid, idx = False, -1

	question_info = f"⭐️ Q{n} - {q.category} - {q.difficulty.capitalize()}"
	question_text = f"{random.choice(EMOJIS)} {q.question}"
	correct_idx = q.answers.index(q.correct)
	
	init_score = 30
	init_time = time.time()

	while not valid:
		show_question(question_info, question_text, q.answers)

		res = input("A-D> ")
		idx = get_idx_by_letter(res)

		valid = (idx >= 0)

	show_question(question_info, question_text, q.answers, correct_idx, idx)

	score = max(0, math.ceil(init_score - (time.time() - init_time)) * 100)

	is_correct = correct_idx == idx
	if (is_correct):
		halt_or_skip(f"✅ {random.choice(CORRECT_RESPONSES)} (+{score} 💎)")
	else:
		halt_or_skip(f"❌ {random.choice(INCORRECT_RESPONSES)}")

	return (score if is_correct else 0), is_correct

	

def show_question(info, text, answers, correct = -1, player_answer = -1):
	global letters

	clear()
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

def get_idx_by_letter(letter: str):
	letters = list("ABCD")
	
	try:
		return letters.index(letter.strip().upper())
	except:
		return -1

def reset_token():
	fetch(f"https://opentdb.com/api_token.php?command=reset&token={token}")

def get_questions():
	data = fetch(f"https://opentdb.com/api.php?amount=15&type=multiple&token={token}")
	questions = []

	# If the current session token has been exhausted
	if (data["response_code"] == 4):
		reset_token()
		return get_questions()

	for r in data["results"]:
		answers = list(r["incorrect_answers"])
		answers.append(r["correct_answer"])
		answers.reverse()

		questions.append(Question(r["question"], answers, r["category"], r["difficulty"]))

	return questions

def fetch(url):
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

def test():
	for e in EMOJIS:
		print(e)

if (__name__ == "__main__"):
	try:
		start()
	except KeyboardInterrupt:
		clear()
		print("Bye!")
		sys.exit(0)