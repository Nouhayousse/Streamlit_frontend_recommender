import streamlit as st
import requests
import webbrowser

from services.api import auth_post

BASE_URL = "http://127.0.0.1:8000/api"


def render_seminar_card(seminar, idx,section):

    image = seminar.get("image")

    st.image(
        image,
        use_container_width=True
    )

    st.subheader(seminar["title"])

    st.write(
        f"📂 {seminar['category']}"
    )
    st.write(
        f"📅 {seminar['start_date']}"
    )

    col1, col2, col3 = st.columns(3)

    # ==========================
    # BOOKMARK
    # ==========================

    with col1:

        if st.button(
            "⭐ Bookmark",
            key=f"{section}_bookmark_{seminar['id']}_{idx}"
        ):

            auth_post(
                f"/interactions/track/",
                data={
                    "seminar_id": seminar["id"],
                    "event_type": "bookmark"
                }
            )

            st.success("Bookmarked")

    # ==========================
    # OPEN SEMINAR
    # ==========================

    with col2:

            if st.button(
                "👁 Open",
                key=f"{section}_view_{seminar['id']}_{idx}"
            ):

                # TRACK VIEW
                auth_post(
                    "/interactions/track/",
                    data={
                        "seminar_id": seminar["id"],
                        "event_type": "view"
                    }
                )

                # OPEN URL
                webbrowser.open_new_tab(
                    seminar["url"]
                )


    with col3:

        if st.button(
            "📝 Register",
            key=f"{section}_register_{seminar['id']}_{idx}"
        ):

            # TRACK REGISTER
            auth_post(
                "/interactions/track/",
                data={
                    "seminar_id": seminar["id"],
                    "event_type": "register"
                }
            )

            # REDIRECT
            webbrowser.open_new_tab(
                seminar["url"]
            )

    st.divider()