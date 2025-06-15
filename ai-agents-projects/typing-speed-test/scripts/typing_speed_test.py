import random
import time

class TypingSpeedTest:
    def __init__(self):
        self.words = self.load_words()
        self.current_word = random.choice(self.words)

    def load_words(self):
        # In a real scenario, this could load from a file. For now, using a sample list.
        return ["python", "development", "typing", "speed", "test", "random", "word", "input", "check", "correctness"]

    def start_test(self):
        print(f"Type the following word: {self.current_word}")
        input("Press Enter when you are ready...")
        start_time = time.time()
        user_input = input("Your input: ")

        if self.check_input(user_input):
            end_time = time.time()
            typing_time = end_time - start_time
            print(f"Well done! Your typing time: {typing_time:.2f} seconds")
        else:
            print("Input was incorrect. Please try again.")
            self.start_test()

    def check_input(self, user_input):
        return user_input.strip() == self.current_word

if __name__ == '__main__':
    test = TypingSpeedTest()
    test.start_test()
