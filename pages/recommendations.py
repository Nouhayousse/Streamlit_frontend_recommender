import streamlit as st

from components.navbar import (
    render_navbar
)

from components.seminar_card import (
    render_seminar_card
)

from services.recommendation_service import (
    get_recommendations
)

from services.search_service import search_seminars
from services.seminar_service import (
    get_all_seminars
)
from components.onboarding_interests import (
    render_onboarding
)




def merge_unique(old, new):

    seen = {s["id"] for s in old}

    for item in new:
        if item["id"] not in seen:
            old.append(item)
            seen.add(item["id"])

    return old
# =====================================
# AUTH
# =====================================




if "access" not in st.session_state:

    st.warning("Please login")

    st.stop()


if "page_all" not in st.session_state:
    st.session_state.page_all = 1

if "all_seminars" not in st.session_state:
    st.session_state.all_seminars = []  



if "search_mode" not in st.session_state:
    st.session_state.search_mode = False

if "search_results" not in st.session_state:
    st.session_state.search_results = []      

# =====================================
# NAVBAR
# =====================================

render_navbar()


st.title("🏠 Seminars")

col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

with col1:
    query = st.text_input("Search seminars")

with col2:
    category = st.selectbox(
        "Category",
        ["", "technology","career-business","education-science","sports-fitness","arts-culture","writing","spirituality","health","hobbies-passions","community","science-and-tech","charity-and-causes"]
    )

with col3:
    source = st.selectbox(
        "Source",
        ["", "meetup", "eventbrite", "other"]
    )

with col4:
    search_btn = st.button("🔍")



if search_btn:

    response = search_seminars(
        q=query,
        category=category,
        source=source
    )

    st.session_state.search_results = response.get("results", [])
    st.session_state.search_mode = True    




if st.session_state.search_mode:

    st.subheader("🔍 Search Results")

    if st.button("⬅ Back to Home"):

        st.session_state.search_mode = False
        st.session_state.search_results = []
        st.rerun()

    for idx, seminar in enumerate(st.session_state.search_results):

        render_seminar_card(
            seminar,
            idx,
            "search"
        )

    st.stop()    

# =====================================
# PAGE TITLE
# =====================================

st.title("🔥 Recommended For You")

# =====================================
# RECOMMENDATIONS
# =====================================

recommendations = get_recommendations()

# results = recommendations.get(
#     "results",
#     []
# )

# for idx, seminar in enumerate(results[:20]):

#     render_seminar_card(seminar, idx)


recommendations = get_recommendations()

# =====================================
# ONBOARDING
# =====================================

if recommendations.get("type") == "ONBOARDING_INTERESTS":

    render_onboarding(
        recommendations.get(
            "interests",
            []
        )
    )

    st.stop()

# =====================================
# NORMAL RECOMMENDATIONS
# =====================================

results = recommendations.get(
    "results",
    []
)

for idx, seminar in enumerate(results[:20]):

    render_seminar_card(
        seminar,
        idx,
        "recommendations"
    )

# =====================================
# BROWSE ALL
# =====================================

st.title("🌍 Browse All")

response = get_all_seminars(st.session_state.page_all)

new_results = response.get("results", [])

st.session_state.all_seminars = merge_unique(
    st.session_state.all_seminars,
    new_results
)

next_page = response.get("next")





for idx, seminar in enumerate(st.session_state.all_seminars):
   
    render_seminar_card(seminar, idx,"browse_all")

if next_page :

    if st.button("Load More"):

        st.session_state.page_all += 1
        st.rerun()



       
        