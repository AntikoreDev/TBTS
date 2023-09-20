import requests
from question import Question

def start():
    print("Loading...")

    questions = get_questions()

    print(questions)
    print(questions[0].question)
    print(questions[0].answers)
    print(questions[0].correct)
    

def get_questions():
    data = fetch("https://opentdb.com/api.php?amount=15&type=multiple")
    questions = []

    for r in data["results"]:
        answers = r["incorrect_answers"]
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
    start()