def main():
    grocery_list = []
    count_of_items = {}
    while True:
        try: 
            #Prompt the user for an item
            items = input("")
            items = items.upper()
            grocery_list.append(items)
        except EOFError: 
            for item in grocery_list:
                if item in count_of_items:
                    count_of_items[item] += 1
                else:
                    count_of_items[item] = 1
            for item in count_of_items:
                print(str(count_of_items[item]) + " " + item)
                    
                
            break
        else:
            continue
    
if __name__ == "__main__":
    main()