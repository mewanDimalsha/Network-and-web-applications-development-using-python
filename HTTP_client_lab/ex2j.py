from urllib import request, parse

search_query = "Rocco's basilisk"
url = f"https://www.duckduckgo.com/?q={parse.quote(search_query)}"

with request.urlopen(url) as query:
    headers = query.headers.items()
    body = query.read()

print(headers)
print(body.decode('utf-8'))
