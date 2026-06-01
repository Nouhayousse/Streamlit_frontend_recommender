

from streamlit import logout, st


if st.button("👤"):

    st.session_state.show_menu = (
        not st.session_state.show_menu
    )


    if st.session_state.show_menu:

        if st.button("Bookmarks"):
            st.switch_page("pages/bookmarks.py")

        if st.button("Profile"):
            st.switch_page("pages/profile.py")

        if st.button("Logout"):
            logout()


