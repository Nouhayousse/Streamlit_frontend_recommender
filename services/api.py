import requests
import streamlit as st

from services.auth_service import refresh_access_token

BASE_URL = "http://127.0.0.1:8000/api"


def get_headers():
   
    return { "Authorization": f"Bearer {st.session_state['access']}" }


def auth_get(endpoint):
    url = f"{BASE_URL}{endpoint}"

    response = requests.get(url, headers=get_headers())

    if response.status_code == 401:
        if refresh_access_token():
            response = requests.get(url, headers=get_headers())

    return response


def auth_post(endpoint, data=None):
    url = f"{BASE_URL}{endpoint}"

    response = requests.post(url, json=data, headers=get_headers())

    if response.status_code == 401:
        if refresh_access_token():
            response = requests.post(url, json=data, headers=get_headers())

    return response