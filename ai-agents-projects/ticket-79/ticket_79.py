import random
import time

class QuizGame:
    def __init__(self, questions, time_limit=300):
        self.questions = questions
        self.time_limit = time_limit
        self.score = 0

    def start_game(self):
        print("Welcome to the Italy Quiz Game!")
        print(f"You have {self.time_limit // 60} minutes to answer {len(self.questions)} questions.")
        start_time = time.time()

        for question in self.questions:
            if time.time() - start_time > self.time_limit:
                print("Time is up!")
                break

            print(f"{question['question']}")
            for idx, option in enumerate(question['options']):
                print(f"{idx + 1}. {option}")
            answer = int(input("Your answer (1-4): ")) - 1

            if answer == question['answer']: 
                self.score += 1
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer was: {question['options'][question['answer']]}")

        print(f"Your final score is: {self.score}/{len(self.questions)}")


# Sample questions for the quiz
questions = [
    {'question': 'What is the capital of Italy?', 'options': ['Rome', 'Milan', 'Naples', 'Florence'], 'answer': 0},
    {'question': 'Which of the following is a famous Italian dish?', 'options': ['Sushi', 'Tacos', 'Pizza', 'Burgers'], 'answer': 2},
    {'question': 'What is the currency used in Italy?', 'options': ['Dollar', 'Euro', 'Lira', 'Pound'], 'answer': 1},
    {'question': 'Who painted the Mona Lisa?', 'options': ['Vincent Van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Michelangelo'], 'answer': 2},
    {'question': 'Which ancient civilization was based in Italy?', 'options': ['Greece', 'Egypt', 'Rome', 'India'], 'answer': 2},
    {'question': 'What is Italy known for in terms of fashion?', 'options': ['Casual wear', 'Haute couture', 'Street fashion', 'Sportswear'], 'answer': 1},
    {'question': 'What is the national sport of Italy?', 'options': ['Soccer', 'Rugby', 'Cycling', 'Baseball'], 'answer': 0},
    {'question': 'Which Italian city is known for its canals?', 'options': ['Rome', 'Venice', 'Milan', 'Turin'], 'answer': 1},
    {'question': 'Italy shares its northern border with which country?', 'options': ['France', 'Germany', 'Austria', 'Switzerland'], 'answer': 2},
    {'question': 'What is the famous amphitheater in Rome called?', 'options': ['The Colosseum', 'The Forum', 'The Pantheon', 'The Vatican'], 'answer': 0},
]

# Initialize and start the quiz game
if __name__ == '__main__':
    game = QuizGame(questions)
    game.start_game()