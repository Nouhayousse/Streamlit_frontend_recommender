import streamlit as st


def render_search_bar():

    col1, col2, col3, col4 = st.columns(
        [4,2,2,1]
    )

    with col1:

        query = st.text_input(
            "",
            placeholder="Search seminars..."
        )

    with col2:

        category = st.selectbox(
            "",
            [
                "",
                "technology",
                "business",
                "health",
                "science",
                "sports"
            ]
        )

    with col3:

        source = st.selectbox(
            "",
            [
                "",
                "meetup",
                "eventbrite"
            ]
        )

    with col4:

        search_clicked = st.button(
            "🔍",
            use_container_width=True
        )

    return (
        query,
        category,
        source,
        search_clicked
    )