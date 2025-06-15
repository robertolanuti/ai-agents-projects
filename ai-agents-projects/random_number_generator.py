import random

def generate_random_numbers(count=3, allow_duplicates=True, range_end=100):
    """
    Generate a list of random numbers.
    
    Args:
        count (int): Number of random numbers to generate.
        allow_duplicates (bool): Whether to allow duplicate numbers.
        range_end (int): The upper limit for random number generation.

    Returns:
        list: A list of random numbers.
    """
    if count < 1:
        raise ValueError("Count must be at least 1")
    if not allow_duplicates and count > range_end + 1:
        raise ValueError("Count exceeds range if duplicates are not allowed")

    if allow_duplicates:
        return [random.randint(0, range_end) for _ in range(count)]
    else:
        return random.sample(range(range_end + 1), count)

def main():
    count = 3  # Set desired count here
    allow_duplicates = True  # Set desired duplication behavior here
    numbers = generate_random_numbers(count, allow_duplicates)
    print(f"Generated Numbers: {numbers}")

if __name__ == "__main__":
    main()