from urllib import request

response = request.urlopen("http://eng.pdn.ac.lk")

response_code = response.getcode()
print("Response Code:", response_code)

headers = response.headers.items()
print("Headers:")
for header, value in headers:
    print(f"{header}: {value}")


server_info = response.headers.get("Server")
os_info = response.headers.get("X-Powered-By")

print("\nServer Information:", server_info)
print("Operating System:", os_info)

body_size = len(response.read())
print("Body Size:", body_size)

body = response.read()

print("Type of body:", type(body))

body = response.read()

response.close()

try:
    unknown_response = request.urlopen("http://eng.pdn.ac.lk/unknown")
    unknown_body = unknown_response.read()
    unknown_response.close()
    print("Body of http://eng.pdn.ac.lk/unknown:", unknown_body.decode("utf-8"))
except Exception as e:
    print("Error:", e)

try:
    unknown_domain_response = request.urlopen("http://unknown.pdn.ac.lk")
    unknown_domain_body = unknown_domain_response.read()
    unknown_domain_response.close()
    print("Body of http://unknown.pdn.ac.lk:", unknown_domain_body.decode("utf-8"))
except Exception as e:
    print("Error:", e)

wiki_response = request.urlopen("https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")
wiki_body = wiki_response.read()
wiki_response.close()
print("Body of Wikipedia page:", wiki_body.decode("utf-8"))