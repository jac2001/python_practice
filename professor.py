import random

def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    correct_answers += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Your score: {correct_answers}/10")

def get_level():
    while True:
        try:
            level = int(input("Enter a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
