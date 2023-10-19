def main():
    tweet = input("Please enter something to tweet about: ")
    vowels = 'aeiouAEIOU'

    for c in tweet:
        if c in vowels:
            tweet = tweet.replace(c, "")
    print("Output:", tweet)
main()