import random
import time

class TypingSpeedTest:
    def __init__(self, word_list_file='words.txt'):
        self.words = self.load_words(word_list_file)

    def load_words(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            print("Word list file not found. Using default words.")
            return ["python", "development", "typing", "speed", "test", "random", "word", "input", "check", "correctness"]

    def start_test(self):
        while True:
            self.current_word = random.choice(self.words)
            print(f"Type the following word: {self.current_word}")
            input("Press Enter when you are ready...")
            start_time = time.time()
            user_input = input("Your input: ")

            if self.check_input(user_input):
                end_time = time.time()
                typing_time = end_time - start_time
                print(f"Well done! Your typing time: {typing_time:.2f} seconds")
                break
            else:
                print("Input was incorrect. Please try again.")

    def check_input(self, user_input):
        return user_input.strip() == self.current_word

if __name__ == '__main__':
    test = TypingSpeedTest('words.txt')
    test.start_test()