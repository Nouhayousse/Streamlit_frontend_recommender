import streamlit as st


def login_view():

    st.title("🔐 Welcome to TamTrack")

    st.subheader(
        "Discover personalized seminars"
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        # auth logic

        st.session_state.page = "home"
        st.rerun()

    st.write("Don't have an account?")

    if st.button("Create account"):

        st.session_state.page = "register"
        st.rerun()