import emoji
def main():
    
    
    input_emoji = input("Input: ")

    input_emoji = emoji.emojize(input_emoji)

    print("Output: ", input_emoji)  
main()