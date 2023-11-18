from urllib import request

tamil_name = "உதய"
tamil_query = "https://www.duckduckgo.com/?q={tamil_name}"

sinhala_name = "උතය"
sinhala_query = "https://www.duckduckgo.com/?q={sinhala_name}"

with request.urlopen(tamil_query) as tamil_query_result:
    tamil_body = tamil_query_result.read()

with request.urlopen(sinhala_query) as sinhala_query_result:
    sinhala_body = sinhala_query_result.read()

print("Tamil Search Results for {tamil_name}:")
print(tamil_body)

print("\nSinhala Search Results for {sinhala_name}:")
print(sinhala_body)
