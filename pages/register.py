import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/api"

st.title("📝 Register")

username = st.text_input("Username")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Create Account"):

    response = requests.post(
        f"{BASE_URL}/users/register/",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )

    if response.status_code == 201:

        st.success(
            "Account created successfully"
        )

        st.switch_page(
            "pages/login.py"
        )

    else:

        st.error(response.json())