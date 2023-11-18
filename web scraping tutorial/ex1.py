import requests

res = requests.get("http://eng.pdn.ac.lk")

print(res.status_code)
print(res.text)