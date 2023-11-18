from urllib import request

response = request.urlopen("http://eng.pdn.ac.lk")

body_size = len(response.read())
print("Body Size:", body_size)
