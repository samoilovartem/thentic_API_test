import requests

from settings import NFT_MINT_URL, API_KEY, MY_BSC_TEST_WALLET, CHAIN_ID, \
    NFT_CONTRACT, RAPID_API_KEY, RAPID_API_HOST

url = NFT_MINT_URL

payload = {
    "key": API_KEY,
    "chain_id": CHAIN_ID,
    "contract": NFT_CONTRACT.get('contracts')[1],
    "nft_id": 1,
    "nft_data": "Second test NFT",
    "to": MY_BSC_TEST_WALLET
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": RAPID_API_HOST,
}

response = requests.request("POST", url, json=payload, headers=headers)


if __name__ == '__main__':
    print(response.text)
