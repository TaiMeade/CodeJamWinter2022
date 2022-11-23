"""

Tai Meade
11/20/2022
Educational CodeJam for Fall/Winter 2022

"""

import streamlit as st
import extremeRPS as RPS25
import RPS101

st.set_page_config("Education", "books.png", "wide")

st.sidebar.title("Options:")
page = st.sidebar.selectbox("Select Page: ", ['Home','Probability Fun'])



if page == 'Home':
    col1,col2 = st.columns(2)
    with col1:
        st.title("Education CodeJam")
        st.subheader("Created By: Tai Meade")
        st.write("---")
        st.subheader("Goals:")
        st.write("* Showcase a toolbox of lessons (using games) and tools for educators.")
        st.write("* Help user have fun while learning!")
        st.write("---")
    with col2:
        st.write("")
        st.image("education_word_collage.png", use_column_width="always")

elif page == 'Probability Fun':

    gameType = st.sidebar.selectbox(['RPS 25', 'RPS 101'])

    if gameType == 'RPS 25':
        RPS25.main()
    elif gameType == 'RPS 101':
        RPS101.main()
    else:
        st.write("ERROR")