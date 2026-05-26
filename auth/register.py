import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/api"

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Register - TamTrack",
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
        "<div class='main-title'>📝 Create Account</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Join TamTrack today</div>",
        unsafe_allow_html=True
    )

    # ====================================
    # REGISTER FORM
    # ====================================

    username = st.text_input(
        "Username"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    # ====================================
    # REGISTER BUTTON
    # ====================================

    if st.button(
        "Create Account",
        use_container_width=True,
        type="primary"
    ):

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
                "auth/login.py"
            )

        else:

            st.error(
                response.json()
            )

    st.divider()

    st.write(
        "Already have an account?"
    )

    if st.button(
        "Back to Login",
        use_container_width=True
    ):

        st.switch_page(
            "auth/login.py"
        )