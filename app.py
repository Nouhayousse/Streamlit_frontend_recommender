import streamlit as st

st.set_page_config(
    page_title="TamTrack",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================================
# HIDE DEFAULT SIDEBAR
# ====================================

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ====================================
# ROUTING
# ====================================

if "access" in st.session_state:

    st.switch_page(
        "pages/home.py"
    )

else:

    st.switch_page(
        "pages/login.py"
    )