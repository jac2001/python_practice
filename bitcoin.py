import sys
import requests

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py amount")
    
    try:
        #Convert the command-line argument to a float
        bitcoins = float(sys.argv[1])
    except:
        sys.exit("Error: Please provide a number of Bitcoins.")
    
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_rate = data['bpi']['USD']['rate_float']
    except requests.RequestException:
        sys.exit("ErrorL Unable to fetch data from Coindesk API.")
    cost = bitcoins * bitcoin_rate
    
    print(f"${cost:,.4f}")
        
if __name__ == "__main__":
    main()