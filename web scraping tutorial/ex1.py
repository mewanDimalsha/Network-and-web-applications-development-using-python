import requests

url = "http://eng.pdn.ac.lk"
res = requests.get(url)

print(res.status_code)
print(res.text)