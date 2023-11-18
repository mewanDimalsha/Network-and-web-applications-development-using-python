from urllib import request

response = request.urlopen("http://eng.pdn.ac.lk")

headers = response.headers.items()
# print("Headers:")
# for header, value in headers:
#     print(f"{header}: {value}")


server_info = response.headers.get("Server")
os_info = response.headers.get("X-Powered-By")

print("\nServer Information:", server_info)
print("Operating System:", os_info)
