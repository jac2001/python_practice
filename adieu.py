import inflect


def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input("Enter a name (Ctrl-D to stop): ")
            names.append(name)
    except EOFError:
        
        if len(names) == 1:
            farewell = f'Adieu, adieu, to {names[0]}'
        else:
            #join all the names except the last one with commas
            all_but_last = ', '.join(names[:-1])
            farewell = f'Adieu, adieu, to {all_but_last} and {names[-1]}'
        print("\n" + farewell)
if __name__ == '__main__':
    main()