import requests
from typing import List

def ddg_query(search_term: str, nr_results: int) -> List[str]:
    api_url = "https://api.duckduckgo.com/"
    params = {
        'q': search_term,
        'format': 'json',
        'no_redirect': '1',  
        't': 'your_app_name'  
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  
        results = response.json()
        urls = [result['url'] for result in results['Results'][:nr_results]]

        return urls

    except requests.exceptions.RequestException as e:
        print(f"Error during DDG query: {e}")
        return []

search_term = "University of Peradeniya"
nr_results = 1
result_urls = ddg_query(search_term, nr_results)
print(result_urls)
