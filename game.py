import random
def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid number.")
    
    target_number = random.randint(1,level)
    
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                print('Please enter a positive integer')
                continue
            if guess < target_number:
                print('Too small!')
            elif guess > target_number:
                print('Too large!')
            else:
                print("Just right!")
                break
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()