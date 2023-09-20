import random, html

# Class that holds data for a particular question
class Question():
    question = ""
    answers = []
    correct = ""
    category = ""
    difficulty = ""

    def __init__(self, question = "", answers = [], category = "", difficulty = ""):
        self.question = self.parse_html(question)
        self.category = self.parse_html(category)
        self.difficulty = self.parse_html(difficulty)

        

        self.answers = self.parse_html(answers)
        self.correct = answers[0]
        
        random.shuffle(self.answers)

    def parse_html(self, data = "") -> any:

        if (isinstance(data, list)):
            new_data = []

            for text in data:
                new_data.append(self.parse_html(text))

            return new_data

        text = html.unescape(data)
        return text