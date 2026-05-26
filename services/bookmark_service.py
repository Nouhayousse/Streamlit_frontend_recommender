import requests
import streamlit as st
from services.api import BASE_URL, get_headers


def get_bookmarks():

    response = requests.get(
        f"{BASE_URL}/interactions/bookmark/",
        headers=get_headers()
    )

    return response.json()


def delete_bookmark(seminar_id):

    response = requests.delete(
        f"{BASE_URL}/interactions/bookmark/",
        headers=get_headers(),
        json={
            "seminar_id": seminar_id
        }
    )

    return response.json()