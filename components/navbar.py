import streamlit as st


CATEGORIES = [
    "", "technology", "career-business", "education-science",
    "sports-fitness", "arts-culture", "writing", "spirituality",
    "health", "hobbies-passions", "community", "science-and-tech", "charity-and-causes"
]

SOURCES = ["", "meetup", "eventbrite", "other"]


def render_navbar():
    """
    Renders the sticky navbar with logo, search bar, filters, and user menu.
    Returns: (query, category, source, search_clicked, menu_action)
    menu_action can be: None | 'bookmarks' | 'profile' | 'logout'
    """

    # ---- Init state ----
    if "nav_query" not in st.session_state:
        st.session_state.nav_query = ""
    if "nav_category" not in st.session_state:
        st.session_state.nav_category = ""
    if "nav_source" not in st.session_state:
        st.session_state.nav_source = ""
    if "user_menu_open" not in st.session_state:
        st.session_state.user_menu_open = False

    username = st.session_state.get("username", "U")
    avatar_letter = username[0].upper() if username else "U"

    # ---- Navbar HTML ----
    st.markdown(
        f"""
        <div class="tt-navbar">
            <a class="tt-logo" href="#">Tam<span>Track</span></a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---- Controls row (Streamlit native for interactivity) ----
    st.markdown(
        """
        <style>
        /* Compact the navbar controls row */
        div[data-testid="stHorizontalBlock"]:has(> div > div[data-testid="stTextInput"]) {
            background: rgba(13,15,20,0.92);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid #252830;
            padding: 8px 40px 12px 40px;
            margin-top: -4px;
            gap: 10px !important;
        }
        div[data-testid="stHorizontalBlock"]:has(> div > div[data-testid="stTextInput"]) 
            [data-testid="stTextInput"] input {
            border-radius: 50px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    nav_c1, nav_c2, nav_c3, nav_c4, nav_c5 = st.columns([4, 2, 2, 1, 1])

    with nav_c1:
        query = st.text_input(
            "search",
            placeholder="🔍  Search seminars, topics, speakers…",
            value=st.session_state.nav_query,
            label_visibility="collapsed",
            key="navbar_query_input"
        )

    with nav_c2:
        category = st.selectbox(
            "category",
            CATEGORIES,
            label_visibility="collapsed",
            key="navbar_cat_select"
        )

    with nav_c3:
        source = st.selectbox(
            "source",
            SOURCES,
            label_visibility="collapsed",
            key="navbar_src_select"
        )

    with nav_c4:
        search_clicked = st.button(
            "Search",
            type="primary",
            use_container_width=True,
            key="navbar_search_btn"
        )

    with nav_c5:
        user_btn = st.button(
            avatar_letter,
            key="navbar_user_btn",
            use_container_width=True,
            help=f"Logged in as {username}"
        )

        if user_btn:
            st.session_state.user_menu_open = not st.session_state.user_menu_open

    # ---- User dropdown ----
    menu_action = None

    if st.session_state.get("user_menu_open", False):
        st.markdown(
            f"""
            <div class="tt-dropdown">
                <div class="tt-dropdown-item">👤 {username}</div>
                <div class="tt-dropdown-divider"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        m1, m2, m3 = st.columns(3)

        with m1:
            if st.button("🔖 Bookmarks", key="menu_bm", use_container_width=True):
                menu_action = "bookmarks"
                st.session_state.user_menu_open = False

        with m2:
            if st.button("👤 Profile", key="menu_profile", use_container_width=True):
                menu_action = "profile"
                st.session_state.user_menu_open = False

        with m3:
            if st.button("🚪 Logout", key="menu_logout", use_container_width=True):
                menu_action = "logout"
                st.session_state.user_menu_open = False

    # Persist inputs
    if search_clicked:
        st.session_state.nav_query = query
        st.session_state.nav_category = category
        st.session_state.nav_source = source

    return query, category, source, search_clicked, menu_action