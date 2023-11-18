from urllib import request

response = request.urlopen("http://eng.pdn.ac.lk")

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