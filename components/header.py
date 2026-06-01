


from streamlit import st


col1,col2,col3 = st.columns([1,5,1])

with col1:
    st.image("assets/logo.png", width=80)

with col2:
    query = st.text_input(
        "",
        placeholder="Search seminars..."
    )

#with col3:
    #user_menu()