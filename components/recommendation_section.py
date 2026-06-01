import streamlit as st


def render_recommendation_section(results):
    """
    Renders the 'Recommended For You' horizontal scroll row.
    Cards are rendered as pure HTML inside a scrollable flex container.
    Interactive bookmark/view/register buttons use st.link_button.
    """
    from services.api import auth_post

    if not results:
        st.markdown(
            """
            <div class="tt-scroll-section" style="padding-top:40px;">
                <div class="tt-empty-state">
                    <div class="tt-empty-icon">✨</div>
                    <div class="tt-empty-title">No recommendations yet</div>
                    <p>Start exploring seminars to get personalized picks.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        return

    if "bookmarked" not in st.session_state:
        st.session_state.bookmarked = set()

    # ---- Section Header ----
    st.markdown(
        """
        <div class="tt-scroll-section" style="padding-top:48px; padding-bottom:0;">
            <div class="tt-section-header">
                <div>
                    <div class="tt-section-title">🔥 Recommended <em style="color:var(--accent);font-style:normal;">For You</em></div>
                    <div class="tt-section-sub">Curated picks based on your interests</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---- Build horizontal scroll HTML ----
    CATEGORY_ICONS = {
        "technology": "💻", "career-business": "💼", "education-science": "🎓",
        "sports-fitness": "🏃", "arts-culture": "🎨", "writing": "✍️",
        "spirituality": "🧘", "health": "🏥", "hobbies-passions": "❤️",
        "community": "🤝", "science-and-tech": "🔬", "charity-and-causes": "🌍",
    }
    PLACEHOLDERS = ["🎓", "💡", "🚀", "🌟", "📚", "🎯", "💼", "🔬"]

    cards_html = ""
    for idx, s in enumerate(results[:12]):
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
        source_str = f'<span style="font-size:10px;color:var(--text-dim);">via {source}</span>' if source else ""

        if image:
            img_block = (
                f'<img src="{image}" class="tt-card-img" '
                f'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />'
                f'<div class="tt-card-img-placeholder" style="display:none">{placeholder}</div>'
            )
        else:
            img_block = f'<div class="tt-card-img-placeholder">{placeholder}</div>'

        bm_style = (
            "background:rgba(232,184,109,0.08);border:1px solid var(--accent);color:var(--accent);"
            if is_bm else
            "background:var(--bg-card2);border:1px solid var(--border-light);color:var(--text-muted);"
        )
        bm_label = "★ Saved" if is_bm else "☆ Save"

        cards_html += f"""
        <div class="tt-card">
            {img_block}
            <div class="tt-card-body">
                <div style="display:flex;align-items:center;justify-content:space-between;">
                    <span class="tt-card-badge">{cat_icon} {cat_label}</span>
                    {source_str}
                </div>
                <div class="tt-card-title">{title}</div>
                <div class="tt-card-meta">📅 {date}</div>
            </div>
            <div class="tt-card-actions">
                <a href="#" style="flex:1;text-decoration:none;" title="Bookmark (use button below)">
                    <button class="tt-btn"
                            style="width:100%;{bm_style}font-family:'DM Sans',sans-serif;font-size:12px;font-weight:600;cursor:pointer;border-radius:8px;padding:8px 0;">
                        {bm_label}
                    </button>
                </a>
                <a href="{url}" target="_blank" style="flex:1;text-decoration:none;">
                    <button class="tt-btn tt-btn-primary" style="width:100%;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:600;cursor:pointer;border-radius:8px;padding:8px 0;">
                        Register →
                    </button>
                </a>
            </div>
        </div>
        """

    scroll_html = f"""
    <div class="tt-scroll-section" style="padding-top:16px; padding-bottom:8px;">
        <div class="tt-hscroll">
            {cards_html}
        </div>
    </div>
    """

    st.markdown(scroll_html, unsafe_allow_html=True)

    # ---- Invisible Streamlit bookmark buttons ----
    # Render them in a hidden expander so they work without showing
    with st.expander("⭐ Bookmark actions", expanded=False):
        st.caption("Use these to bookmark from the cards above:")
        bm_cols = st.columns(min(len(results[:12]), 6))
        for idx, s in enumerate(results[:12]):
            sid = s.get("id", idx)
            title = s.get("title", "?")[:20]
            col_idx = idx % 6
            with bm_cols[col_idx]:
                is_bm = sid in st.session_state.bookmarked
                lbl = f"★ {title}" if is_bm else f"☆ {title}"
                if st.button(lbl, key=f"rec_bm_{sid}_{idx}"):
                    auth_post("/interactions/track/", {
                        "seminar_id": sid, "event_type": "bookmark"
                    })
                    st.session_state.bookmarked.add(sid)
                    st.toast("✓ Bookmarked!")
                    st.rerun()