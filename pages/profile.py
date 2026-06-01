import streamlit as st

st.title("👤 My Profile")

st.write(
    "Username:",
    st.session_state.get("username")
)