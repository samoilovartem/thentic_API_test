import requests

from settings import NFT_TRANSFER_URL, API_KEY, CHAIN_ID, NFT_CONTRACT, MY_BSC_TEST_WALLET, \
    MY_WALLET, RAPID_API_KEY, RAPID_API_HOST

url = NFT_TRANSFER_URL

payload = {
    "key": API_KEY,
    "chain_id": CHAIN_ID,
    "contract": NFT_CONTRACT.get('contracts')[0],
    "nft_id": 1,
    "from": MY_BSC_TEST_WALLET,
    "to": MY_WALLET.get('wallet'),
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": RAPID_API_HOST,
}

response = requests.request("POST", url, json=payload, headers=headers)


if __name__ == '__main__':
    print(response.text)
