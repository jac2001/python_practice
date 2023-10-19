   
def main():
    time = input("Enter the time (in 24-hour format HH:MM): ")

    # Convert the time to hours as a float
    hours_float = convert(time)
    
    # Check the time range for meals
    if 7 <= hours_float <= 8:
        print("It's breakfast time!")
    elif 12 <= hours_float <= 13:
        print("It's lunch time!")
    elif 18 <= hours_float <= 19:
        print("It's dinner time!")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    hours_float = hours + minutes / 60
    return hours_float
    


if __name__ == "__main__":
    main()