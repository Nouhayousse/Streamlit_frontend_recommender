import requests
import streamlit as st
from services.api import (
    BASE_URL,
    get_headers,
    auth_get
)


def get_all_seminars(page=1):

    

    response = auth_get(
        f"/seminars/?page={page}"
    )

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    return response.json()