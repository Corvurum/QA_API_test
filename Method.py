import requests

payload = {"login":"secret_login", "password":"secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookiev = response1.cookies.get('auth_cookie')

cookies = {}
if cookiev is not None:
    cookies.update({'auth_cookie': cookiev})
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)