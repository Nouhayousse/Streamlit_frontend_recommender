import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/api"

st.title("🔐 Login")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    response = requests.post(
        f"{BASE_URL}/token/",
        json={
            "username": username,
            "password": password
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.session_state["access"] = data["access"]

        st.session_state["refresh"] = data["refresh"]

        st.success("Login successful")

        st.switch_page(
            "pages/recommendations.py"
        )

    else:

        st.error("Invalid credentials")