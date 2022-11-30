"""

Tai Meade
11/20/2022
Educational CodeJam for Fall/Winter 2022

"""

import streamlit as st
import extremeRPS as RPS25
import RPS101
import qrCode
import trivia
import typeSpeedTesting
import images

st.set_page_config("Education", "images/books.png", "wide")

st.sidebar.title("Options:")
page = st.sidebar.selectbox("Select Page: ", ['Home','Probability Fun','qRCode Creator/Checker', 'Trivia Game', 'TypeSpeedTester'])



# Home Page
if page == 'Home':
    
    col1,col2 = st.columns(2)

    with col1:
        st.title("Education CodeJam")
        st.subheader("Created By: Tai Meade")
        st.write("---")
        st.subheader("Goals:")
        st.write("* Showcase a toolbox of programs to help the user leave this program smarter than they were before encountering it!")
        st.write("* Help the user have fun while learning!")
        st.write("* QR Code page/program is intended to help educators track attendance...it is currently a basic proof of concept, rather than a ready to deploy idea, but it is fun!")
        st.write("---")

    with col2:
        st.write("")
        st.image("images/education_word_collage.png", use_column_width="always")



# RPS 25 and 101 Page
elif page == 'Probability Fun':

    gameType = st.sidebar.selectbox("Modes:",['RPS 25', 'RPS 101'])

    if gameType == 'RPS 25':
        RPS25.main()
    elif gameType == 'RPS 101':
        RPS101.main()
    else:
        st.write("ERROR")



# qrCode Section/Page
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
            st.write("* NOTE: This is a WIP...the most likely use would be to alter the Attendance Checker to compare two text files, and create a separate app for a phone/camera that stores data within a .txt file for comparison later.")
            st.write("* This is mostly for proof of concept!")
            st.write("Teacher creates a .txt file with names of all students. Then uses that .txt file to create QR Codes for all students. Gives them ID's or a piece of paper with the QR Code on it, then takes photos of each one every day of class using a dummy phone/camera. Finally, uses the Attendance Checker to compare the file with the photos of QR Codes from that day of class to the initial students.txt file that has the names of all students.")
    
    with col2:
        qrCode.main()



# Trivia Game Page
elif page == 'Trivia Game':
    
    trivia.main()



# TypeSpeedTester Page
elif page == 'TypeSpeedTester':

    typeSpeedTesting.main()