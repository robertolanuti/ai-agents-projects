import random

def generate_random_numbers(count=3, allow_duplicates=True, range_end=100):
    if allow_duplicates:
        return [random.randint(0, range_end) for _ in range(count)]
    else:
        return random.sample(range(range_end + 1), count)


def main():
    numbers = generate_random_numbers(3, allow_duplicates=True)  # Adjust parameters as needed
    print(f"Generated Numbers: {numbers}")

if __name__ == "__main__":
    main()