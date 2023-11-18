from urllib import request

response = request.urlopen("http://eng.pdn.ac.lk")

response_code = response.getcode()
print("Response Code:", response_code)
