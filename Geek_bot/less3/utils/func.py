import requests

def fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        return data.get('image')

def quote():
    url = 'https://animechan.xyz/api/random'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        return data

def emoji():
    url = 'https://emojihub.yurace.pro/api/random'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        return data

if __name__ == '__main__':
    fox()
    quote()
    emoji()