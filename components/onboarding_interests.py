import streamlit as st

from services.interest_service import (
    save_interests
)


def render_onboarding(interests):

    st.title("🎯 Choose Your Interests")

    st.write(
        "Select topics you are interested in "
        "to personalize recommendations."
    )

    selected_ids = []

    for interest in interests:

        checked = st.checkbox(
            interest["name"],
            key=f"interest_{interest['id']}"
        )

        if checked:
            selected_ids.append(
                interest["id"]
            )

    if st.button("Save Interests"):

        save_interests(selected_ids)

        st.success(
            "Interests saved"
        )

        st.rerun()