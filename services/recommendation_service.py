import requests

from services.api import (
    BASE_URL,
    auth_get,
    get_headers
)


def get_recommendations():

    response = auth_get(
        f"/recommendations/"
    )

    if response.status_code != 200:
        print("Failed to fetch recommendations:", response.status_code, response.text)
        return []

    return response.json()