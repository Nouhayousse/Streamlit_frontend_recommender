import streamlit as st

from services.bookmark_service import (
    get_bookmarks,
    delete_bookmark
)

from components.seminar_card import render_seminar_card


# =========================
# AUTH CHECK
# =========================

if "access" not in st.session_state:
    st.warning("Please login")
    st.stop()


st.title("📌 My Bookmarks")

# =========================
# LOAD DATA
# =========================

bookmarks = get_bookmarks()


if not bookmarks:
    st.info("No bookmarks yet")
    st.stop()


# =========================
# DISPLAY
# =========================

for idx, seminar in enumerate(bookmarks):

    st.image(seminar["image"])
    st.subheader(seminar["title"])
    st.write(f"📂 {seminar['category']}")
    st.write(f"📅 Bookmarked: {seminar['bookmarked_at']}")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "Open",
            seminar["url"]
        )

    with col2:

        if st.button(
            "🗑 Remove",
            key=f"delete_bookmark_{seminar['id']}_{hash(seminar['bookmarked_at'])}"
        ):

            delete_bookmark(seminar["id"])
            st.success("Removed")

            st.rerun()