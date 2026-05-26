import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000/api"


def refresh_access_token():
    response = requests.post(
        f"{BASE_URL}/token/refresh/",
        json={
            "refresh": st.session_state.get("refresh")
        }
    )

    if response.status_code == 200:
        st.session_state["access"] = response.json()["access"]
        return True

    return False