import streamlit as st


def render_navbar():

    st.sidebar.title("TamTrack")

    if "username" in st.session_state:

        st.sidebar.success(
            f"👤 {st.session_state['username']}"
        )

    st.sidebar.page_link(
        "pages/recommendations.py",
        label="🏠 Home"
    )

    st.sidebar.page_link(
        "pages/search.py",
        label="🔍 Search"
    )

    st.sidebar.page_link(
        "pages/bookmarks.py",
        label="⭐ Bookmarks"
    )

    if st.sidebar.button("Logout"):

        st.session_state.clear()

        st.switch_page("pages/login.py")