import requests
import sys

APIKey = str("5e724259539eeb5f7b1a2162fc845b83283161397e60aa924447b699cca4b5c0")

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + APIKey)
o = response.json()

BCPrice = o["data"]["priceUsd"]
total = n * float(BCPrice)
print(f"${total:,.4f}")
