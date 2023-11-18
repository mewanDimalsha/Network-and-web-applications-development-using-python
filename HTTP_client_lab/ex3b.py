import requests

def last_modified(url: str) -> str:
    try:

        response = requests.head(url)
        response.raise_for_status() 
        last_modified_header = response.headers.get('Last-Modified')

        return last_modified_header

    except requests.exceptions.RequestException as e:
        print(f"Error getting Last-Modified header: {e}")
        return None

url = "http://www.example.com"
last_modified_header = last_modified(url)

if last_modified_header is not None:
    print(f"Last-Modified Header: {last_modified_header}")
else:
    print("Last-Modified header not found.")
