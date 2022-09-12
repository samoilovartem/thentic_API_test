import requests

from settings import NFT_CONTRACTS_URL, API_KEY, CHAIN_ID, RAPID_API_KEY, RAPID_API_HOST

url = NFT_CONTRACTS_URL

querystring = {"key": API_KEY, "chain_id": CHAIN_ID}

headers = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": RAPID_API_HOST,
}

response = requests.request("GET", url, headers=headers, params=querystring)
all_contracts = response.text


if __name__ == '__main__':
    print(all_contracts)
