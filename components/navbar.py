import streamlit as st


def render_navbar():

    col1, col2 = st.columns([8, 1])

    with col1:
        st.title("🎓 TamTrack")

    with col2:

        with st.popover("👤"):

            if st.button("Profile"):

                st.session_state.page = "profile"
                st.rerun()

            if st.button("Bookmarks"):

                st.session_state.page = "bookmarks"
                st.rerun()

            if st.button("Logout"):

                st.session_state.clear()

                st.session_state.page = "login"

                st.rerun()