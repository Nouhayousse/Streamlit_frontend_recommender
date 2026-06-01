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

query, category, source, search_clicked, menu_action = render_navbar()

if search_clicked:

    response = search_seminars(
        q=query,
        category=category,
        source=source
    )

    st.session_state.search_results = response.get("results", [])
    st.session_state.search_mode = True




if menu_action == "bookmarks":
    st.switch_page("pages/bookmarks.py")

elif menu_action == "profile":
    st.switch_page("pages/profile.py")

elif menu_action == "logout":
    st.session_state.clear()
    st.switch_page("pages/login.py")
   
#st.title("🏠 Seminars")

#col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

# with col1:
#     query = st.text_input("Search seminars")

# with col2:
#     category = st.selectbox(
#         "Category",
#         ["", "technology","career-business","education-science","sports-fitness","arts-culture","writing","spirituality","health","hobbies-passions","community","science-and-tech","charity-and-causes"]
#     )

# with col3:
#     source = st.selectbox(
#         "Source",
#         ["", "meetup", "eventbrite", "other"]
#     )

# with col4:
#     search_btn = st.button("🔍")



# if search_btn:

#     response = search_seminars(
#         q=query,
#         category=category,
#         source=source
#     )

#     st.session_state.search_results = response.get("results", [])
#     st.session_state.search_mode = True    




if st.session_state.search_mode:

    st.markdown("## 🔍 Search Results")
    st.caption("Filter your seminars by keywords, category and source")

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

#st.title("🔥 Recommended For You")

# =====================================
# RECOMMENDATIONS
# =====================================

#recommendations = get_recommendations()

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
st.subheader("🔥 Recommended For You")

#st.markdown('<div class="scroll-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="hscroll">', unsafe_allow_html=True)


for idx, seminar in enumerate(results[:10]):

        render_seminar_card(seminar, idx, "rec")

st.markdown("</div>", unsafe_allow_html=True)


    


# BROWSE ALL
# =====================================

st.subheader("🌍 Browse All Seminars")

response = get_all_seminars(st.session_state.page_all)

new_results = response.get("results", [])

st.session_state.all_seminars = merge_unique(
    st.session_state.all_seminars,
    new_results
)

next_page = response.get("next")

# GRID 3 columns
cols = st.columns(3, gap="medium")

for idx, seminar in enumerate(st.session_state.all_seminars):

    with cols[idx % 3]:

        render_seminar_card(
            seminar,
            idx,
            "browse_all"
        )






if next_page:

    if st.button("⬇ Load More", use_container_width=True):

        st.session_state.page_all += 1
        st.rerun()



     



from components.footer import render_footer

render_footer()        