import streamlit as st


def profile_view():

    st.title("👤 My Profile")

    st.write(
        f"Username: {st.session_state['username']}"
    )

    if st.button("⬅ Back Home"):

        st.session_state.page = "home"
        st.rerun()