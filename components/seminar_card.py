import streamlit as st
from services.api import auth_post

def _init():
    if "bookmarked" not in st.session_state:
        st.session_state.bookmarked = set()


def render_seminar_card(seminar, idx, section):

    _init()

    sid = seminar.get("id", idx)
    title = seminar.get("title", "Untitled Seminar")
    category = seminar.get("category", "")
    date = str(seminar.get("start_date", ""))[:10]
    image = seminar.get("image") or ""
    url = seminar.get("url", "#")

    is_bm = sid in st.session_state.bookmarked

    st.markdown(
        f"""
        <div class="tt-card-fixed">

            <div class="tt-card-img-wrap">
                <img src="{image}" class="tt-card-img" />
            </div>

            <div class="tt-card-content">

                <div class="tt-card-title">
                    {title[:60]}
                </div>

                <div class="tt-card-meta">
                    📂 {category[:20]} <br/>
                    📅 {date}
                </div>

                <div class="tt-card-actions">
                    <button class="btn">⭐</button>
                    <a href="{url}" target="_blank">
                        <button class="btn primary">Open</button>
                    </a>
                </div>

            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⭐", key=f"{section}_bm_{sid}_{idx}"):
            auth_post("/interactions/track/", {
                "seminar_id": sid,
                "event_type": "bookmark"
            })
            st.session_state.bookmarked.add(sid)
            st.rerun()