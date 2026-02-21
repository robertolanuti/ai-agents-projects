import random

# Function to generate three random numbers
def generate_random_numbers():
    return [random.randint(0, 100) for _ in range(3)]

if __name__ == '__main__':
    random_numbers = generate_random_numbers()
    print(f"Three random numbers: {random_numbers[0]}, {random_numbers[1]}, {random_numbers[2]}")