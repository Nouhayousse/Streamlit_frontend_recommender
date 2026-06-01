import streamlit as st
from services.api import auth_post


CATEGORY_ICONS = {
    "technology": "💻", "career-business": "💼", "education-science": "🎓",
    "sports-fitness": "🏃", "arts-culture": "🎨", "writing": "✍️",
    "spirituality": "🧘", "health": "🏥", "hobbies-passions": "❤️",
    "community": "🤝", "science-and-tech": "🔬", "charity-and-causes": "🌍",
}
PLACEHOLDERS = ["🎓", "💡", "🚀", "🌟", "📚", "🎯", "💼", "🔬"]


def render_browse_section(all_seminars, has_next, on_load_more):
    """
    Renders the 'Browse All Seminars' grid section.
    all_seminars: list of seminar dicts
    has_next: bool — whether there's a next page
    on_load_more: callback called when user clicks Load More
    """
    if "bookmarked" not in st.session_state:
        st.session_state.bookmarked = set()

    # ---- Section header ----
    st.markdown(
        """
        <div class="tt-divider"></div>
        <div class="tt-browse-section" style="padding-bottom:8px;">
            <div class="tt-section-header">
                <div>
                    <div class="tt-section-title">🌍 Browse <em style="color:var(--accent);font-style:normal;">All Seminars</em></div>
                    <div class="tt-section-sub">Explore every seminar available on the platform</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---- 4-column grid ----
    if not all_seminars:
        st.markdown(
            """
            <div class="tt-empty-state">
                <div class="tt-empty-icon">🗂️</div>
                <div class="tt-empty-title">No seminars found</div>
                <p>Check back later for new events.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    # Grid: 4 columns
    cols = st.columns(4, gap="medium")

    for idx, s in enumerate(all_seminars):
        col = cols[idx % 4]
        sid = s.get("id", idx)
        title = s.get("title", "Untitled")
        category = s.get("category", "")
        date = str(s.get("start_date", ""))[:10] or "Date TBD"
        image = s.get("image") or ""
        url = s.get("url", "#")
        source = s.get("source", "")
        cat_icon = CATEGORY_ICONS.get(category, "📌")
        cat_label = category.replace("-", " ").title() if category else "Seminar"
        placeholder = PLACEHOLDERS[idx % len(PLACEHOLDERS)]
        is_bm = sid in st.session_state.bookmarked

        with col:
            # Card HTML
            if image:
                img_block = (
                    f'<img src="{image}" class="tt-card-img" style="height:140px;" '
                    f'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />'
                    f'<div class="tt-card-img-placeholder" style="height:140px;display:none">{placeholder}</div>'
                )
            else:
                img_block = f'<div class="tt-card-img-placeholder" style="height:140px;">{placeholder}</div>'

            source_str = f'<span style="font-size:10px;color:var(--text-dim);">via {source}</span>' if source else ""

            st.markdown(
                f"""
                <div class="tt-card" style="width:100%;min-width:unset;height:auto;min-height:320px;">
                    {img_block}
                    <div class="tt-card-body">
                        <div style="display:flex;align-items:center;justify-content:space-between;gap:4px;">
                            <span class="tt-card-badge">{cat_icon} {cat_label}</span>
                            {source_str}
                        </div>
                        <div class="tt-card-title" style="font-size:14px;">{title}</div>
                        <div class="tt-card-meta">📅 {date}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Action buttons under each card
            bm_label = "★ Saved" if is_bm else "☆ Save"
            bc1, bc2 = st.columns(2)

            with bc1:
                if st.button(
                    bm_label,
                    key=f"browse_bm_{sid}_{idx}",
                    use_container_width=True
                ):
                    auth_post("/interactions/track/", {
                        "seminar_id": sid,
                        "event_type": "bookmark"
                    })
                    st.session_state.bookmarked.add(sid)
                    st.toast("✓ Bookmarked!")
                    st.rerun()

            with bc2:
                st.link_button(
                    "Register →",
                    url,
                    use_container_width=True,
                    type="primary"
                )

            st.markdown("<div style='margin-bottom:8px'></div>", unsafe_allow_html=True)

    # ---- Load More ----
    if has_next:
        st.markdown("<div class='tt-load-more-wrap'>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        _, center_col, _ = st.columns([2, 1, 2])
        with center_col:
            if st.button(
                "Load More Seminars",
                use_container_width=True,
                key="browse_load_more"
            ):
                on_load_more()
    else:
        st.markdown(
            """
            <div style="text-align:center;padding:32px;color:var(--text-dim);font-size:13px;">
                ✓ You've seen all available seminars
            </div>
            """,
            unsafe_allow_html=True
        )