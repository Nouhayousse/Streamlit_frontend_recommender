import streamlit as st

def render_footer():

    st.divider()

    c1,c2,c3 = st.columns(3)

    with c1:
        st.write("TamTrack © 2026")

    with c2:
        st.write("About")
        st.write("Contact")
        st.write("Privacy")

    with c3:
        st.write("Instagram")
        st.write("Facebook")
        st.write("LinkedIn")