import requests, random, os, sys, keyboard
from question import Question
from generics import *

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def start():
    print("Loading...")

    questions = get_questions()
    n = 1

    while len(questions):
        play(questions.pop(0), n)
        n += 1

def play(q, n = 1):
    valid, idx = False, -1

    question_info = f"⭐️ Q{n} - {q.category} - {q.difficulty.capitalize()}"
    question_text = f"{random.choice(EMOJIS)} {q.question}"
    correct_idx = q.answers.index(q.correct)

    while not valid:
        show_question(question_info, question_text, q.answers)

        res = input("[A-D]> ")
        idx = get_idx_by_letter(res)

        valid = (idx >= 0)

    show_question(question_info, question_text, q.answers, correct_idx, idx)

    if (correct_idx == idx):
        input(f"✅ {random.choice(CORRECT_RESPONSES)}")
    else:
        input(f"❌ {random.choice(INCORRECT_RESPONSES)}")

    

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

    

def get_questions():
    data = fetch("https://opentdb.com/api.php?amount=15&type=multiple")
    questions = []

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

if (__name__ == "__main__"):
    try:
        start()
    except KeyboardInterrupt:
        clear()
        print("Bye!")
        sys.exit(0)