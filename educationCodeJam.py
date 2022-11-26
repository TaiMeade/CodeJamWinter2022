"""

Tai Meade
11/20/2022
Educational CodeJam for Fall/Winter 2022

"""

import streamlit as st
import extremeRPS as RPS25
import RPS101
import qrCode
import images

st.set_page_config("Education", "images/books.png", "wide")

st.sidebar.title("Options:")
page = st.sidebar.selectbox("Select Page: ", ['Home','Probability Fun','qRCode Creator/Checker'])



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
        st.image("images/education_word_collage.png", use_column_width="always")

elif page == 'Probability Fun':

    gameType = st.sidebar.selectbox("Modes:",['RPS 25', 'RPS 101'])

    if gameType == 'RPS 25':
        RPS25.main()
    elif gameType == 'RPS 101':
        RPS101.main()
    else:
        st.write("ERROR")

elif page == 'qRCode Creator/Checker':
    
    st.title("qRCode Demonstration")
    st.write("---")

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("Goal:")
        st.write("Demonstrate how teachers/professors could use QR Codes to take/track attendance.")
        st.write("---")
        st.write("NOTE: By default this program is setup to save files directly to the computer's desktop.")
        st.write("This program/tool allows the user (teachers generally) to create a .txt file with the names of all their students. Then, the user can create QR Codes for each name in that .txt file. The third tab is used to compare the qrCodes in a particular file to the 'students.txt' to determine who was there, and who was absent. Ideally, all you'd have to do is store photos of the qrCodes.")
        with st.expander("Potential Use Case:"):
            st.write("Teacher creates a .txt file with names of all students. Then uses that .txt file to create QR Codes for all students. Gives them ID's or a piece of paper with the QR Code on it, then takes photos of each one every day of class using a dummy phone/camera. Finally, uses the Attendance Checker to compare the file with the photos of QR Codes from that day of class to the initial students.txt file that has the names of all students.")
    
    with col2:
        qrCode.main()