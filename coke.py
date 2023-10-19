def main():
    cost = 50
    amount_paid = 0
    print(f"Amount due: {cost} cents")
    while amount_paid < cost:
        coin = int(input("Insert a coin (25, 10, or 5 cents): "))
        if coin in [25, 10,5]:
            amount_paid += coin
            if amount_paid < cost:
                print(f"Amount due: {cost - amount_paid} cents")
            else:
                print(f"Change owed: {amount_paid - cost} cost")
        else:
            print("INVALID COIN. PLEASE ENTER A VALID COIN")
if __name__ == "__main__":
    main()