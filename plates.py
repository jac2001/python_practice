def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Check length
    if len(s) < 2 or len(s) > 6:
        return False
    
    #Ensure the first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
      # After the first two characters, if there are any letters, they should not be followed by numbers
    for i in range(2, len(s)):
        if s[i].isalpha():
            if i > 2 and s[i-1].isdigit():
                return False
        elif s[i].isdigit():
            #Ensure the first number is not 0
            if i == 2 and s[i] == "0":
                return False
            
        else:
            return False
    return True

main()