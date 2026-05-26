import requests
from services.api import BASE_URL, get_headers


def search_seminars(q="", category="", source=""):

    params = {}

    if q:
        params["q"] = q

    if category:
        params["category"] = category

    if source:
        params["source"] = source

    response = requests.get(
        f"{BASE_URL}/seminars/search/",
        headers=get_headers(),
        params=params
    )

    return response.json()