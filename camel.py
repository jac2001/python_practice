

def main():
    camel_case = str(input("camelCase: "))
    print("snake_case: ", end = "")
    for i in camel_case:
        if i.isupper():
            print("_" + i.lower(), end="")
        else:
            print(i, end="")
    print()
    
    
main()





