import requests

from settings import NEW_NFT_CONTRACT_URL, API_KEY, CHAIN_ID, RAPID_API_KEY, RAPID_API_HOST

url = NEW_NFT_CONTRACT_URL

payload = {
    "key": API_KEY,
    "chain_id": CHAIN_ID,
    "name": "Cool NFT test version 2",
    "short_name": "CNFTt version 2"
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": RAPID_API_HOST,
}

response = requests.request("POST", url, json=payload, headers=headers)
new_contract = response.text


if __name__ == '__main__':
    print(new_contract)
