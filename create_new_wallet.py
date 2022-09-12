import requests

from settings import NEW_WALLET_URL, API_KEY, RAPID_API_KEY, RAPID_API_HOST

url = NEW_WALLET_URL

payload = {"key": API_KEY}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": RAPID_API_HOST,
}

response = requests.request("POST", url, json=payload, headers=headers)
new_wallet_data = response.text


if __name__ == '__main__':
    print(new_wallet_data)
