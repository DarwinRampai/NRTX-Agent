from typing import Any, Dict
import requests

class WebSearcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.example.com/search"  # Replace with actual search API URL

    def search(self, query: str) -> Dict[str, Any]:
        params = {
            'q': query,
            'api_key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Search failed", "status_code": response.status_code}

def perform_search(query: str, api_key: str) -> Dict[str, Any]:
    searcher = WebSearcher(api_key)
    return searcher.search(query)