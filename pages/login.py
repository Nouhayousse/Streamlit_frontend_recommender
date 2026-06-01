import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/api"

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Login - TamTrack",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================================
# HIDE SIDEBAR
# ====================================

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display:none;
    }

    .main-title {
        text-align:center;
        font-size:48px;
        font-weight:bold;
        margin-bottom:10px;
    }

    .subtitle {
        text-align:center;
        color:gray;
        margin-bottom:40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ====================================
# CENTER LAYOUT
# ====================================

left, center, right = st.columns([1,2,1])

with center:

    st.markdown(
        "<div class='main-title'>🎓 TamTrack</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Discover the best seminars worldwide</div>",
        unsafe_allow_html=True
    )

    # ====================================
    # LOGIN FORM
    # ====================================

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    # ====================================
    # LOGIN BUTTON
    # ====================================

    if st.button(
        "Login",
        use_container_width=True,
        type="primary"
    ):

        response = requests.post(
            f"{BASE_URL}/token/",
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:

            data = response.json()
            st.session_state["username"] = username

            st.session_state["access"] = data["access"]

            st.session_state["refresh"] = data["refresh"]

            st.success("Login successful")

            st.switch_page(
                "pages/home.py"
            )

        else:

            st.error(
                "Invalid username or password"
            )

    st.divider()

    st.write(
        "Don't have an account?"
    )

    if st.button(
        "Create Account",
        use_container_width=True
    ):

        st.switch_page(
            "pages/register.py"
        )