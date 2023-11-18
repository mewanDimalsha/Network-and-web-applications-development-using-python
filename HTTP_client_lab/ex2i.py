from urllib import request, parse

search_query = "University of Peradeniya"
url = f"https://www.duckduckgo.com/?q={parse.quote(search_query)}&format=json&pretty=1"

with request.urlopen(url) as query:
    headers = query.headers.items()
    body = query.read()

print(headers)
print(body.decode('utf-8'))
