from urllib import request

response = request.urlopen("http://eng.pdn.ac.lk")

body = response.read()

print("Type of body:", type(body))

# body = response.read()

response.close()
