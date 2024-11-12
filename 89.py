import requests
r=requests.get("https://www.google.com")
print(r.text)
# requests.post(url,headers=headers,data=date)