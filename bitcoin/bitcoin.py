# CS50P Week 4
# This program fetches the current price of Bitcoin using the CoinCap API (v3)
# and calculates the total value in USD based
# on a user-provided amount of Bitcoin.
# The amount must be passed as a command-line argument.
# If the input is invalid or if the API request fails,
# the program exits with an error message.

import requests
import sys


def main():
    bitcoin_nprice = check_nbitcoin_price()
    print(bitcoin_nprice)


def get_number_bitcoin():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
        return n
    except ValueError:
        sys.exit("Command-line argument is not a number")


api_key = "d4082ae3991c804337237e2f95c6e01d469a40bcd8d6524e13fdc70c229ade9e"


def check_bitcoin_price(api_key):
    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        sys.exit("Error for fetching bitcoin actual price")


def check_nbitcoin_price():
    n = get_number_bitcoin()
    response = check_bitcoin_price(api_key)
    price = float(response["data"]["priceUsd"])
    total = n * price
    return f"${total:,.4f}"


if __name__ == "__main__":
    main()
