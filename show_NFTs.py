import requests

from settings import NFT_URLS, API_KEY, CHAIN_ID, RAPID_API_KEY, RAPID_API_HOST

url = NFT_URLS

querystring = {"key": API_KEY, "chain_id": CHAIN_ID}

headers = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": RAPID_API_HOST,
}

response = requests.request("GET", url, headers=headers, params=querystring)
all_NFTs = response.text


if __name__ == '__main__':
    print(all_NFTs)
    # 0xb1b6502f84b2700bd5a6c26751f703446e2b4c76, 0x04fb07e282b4f8a8b6e9e13ca6514cc95e7f89af
