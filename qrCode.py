"""

Tai Meade
This is intended to allow a user to enter a list of names (separated by commas) to generate QR codes for students...the goal of the program is to make taking attendance easier for teachers.

"""

# Module used to create QR codes
import qrcode
# Module for decoding/getting value from QR code
import cv2
# Module for creating UI
import streamlit as st
# Other modules
import os
#import csv

def qrCreator():

    needTXT = st.checkbox("Do you already have a .txt file on your desktop containing all students?")

    names = st.text_input("Please enter your list of names (separated by commas): ")

    desktopPath = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop')) # Creds to StackOverflow

    newFolder = os.path.join(desktopPath, "qrCodes")
    if names != "":
        try:
            os.mkdir(newFolder)
        except FileExistsError as e:
            pass

        nameList = names.split(",")

        # Converts the list (nameList) into a list of lists (listOfNameList) so csvwriter writes it properly.
        # listOfNameList = []
        # for name in nameList:
        #     name = name.split(',')
            
        #     listOfNameList.append(name)
            
        # Create CSV file with student names to compare to later.
        if needTXT == False:
            with open(desktopPath + "/students.txt", 'w') as txtFile:
                for i, name in enumerate(nameList):
                    name = name.strip()
                    if i != (len(nameList)-1):
                        txtFile.write(name + ',')
                    else:
                        txtFile.write(name)
        
        for name in nameList:
            name = name.strip()
            st.write(name) # <------  what is being stored in qr code
            img = qrcode.make(name[0:])
            if name[-1] == ",":
                img.save(f"{desktopPath}/qrCodes/{name[0:-1]}.jpg")
            else:
                img.save(f"{desktopPath}/qrCodes/{name}.jpg")


tab1,tab2,tab3 = st.tabs(['QR Creator','QR Checker','Attendance Checker'])

# Create QR Codes
with tab1:
    qrCreator()

# QR Value Getter
with tab2:
    folderName = st.text_input("Please enter the folder that your QR Codes are stored in: ")

    desktopPath = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop')) # Creds to StackOverflow

    directory = f"{desktopPath}/{folderName}"

    # Gets values from qrCodes
    if folderName != "":
        try:
            qrValues = []
            for qr in os.listdir(desktopPath + "/" + folderName):
                f = os.path.join(directory, qr)
                if os.path.isfile(f):
                    d = cv2.QRCodeDetector()
                    value, points, straightQRCode = d.detectAndDecode(cv2.imread(f))
                    qrValues.append(value)
                    st.write(value)
            st.write(qrValues)
        except Exception:
            st.write("That file could not be found.")

# Compare QR Codes (students in class) to .txt file that user has containing all students
with tab3:

    attendanceHere = []
    attendanceAbsent = []

    # Attendance Checker
    with open(desktopPath + "/students.txt", 'r') as txtFile:
            # Turns contents from attendance sheet/file into list for comparing
            content = txtFile.read()
            contentList = content.split(",")
            contentListStripped = []
            for name in contentList:
                name = name.strip()
                contentListStripped.append(name)
            #print(contentListStripped)
            try:
                for i in range(len(contentList)):
                    if qrValues[i] in contentListStripped:
                        attendanceHere.append(qrValues[i])
                        contentListStripped.remove(qrValues[i])
                        #print(contentListStripped)
                #print(contentListStripped)
            except IndexError:
                pass

            # Sets list of people who weren't absent/don't have a QR Code right now...
            for name in contentListStripped:
                    attendanceAbsent.append(name)

    readyOrNot = st.text_input("Ready to check attendance (y/n)?").lower()
    
    if readyOrNot == "":
        st.write("")
    elif readyOrNot == 'y':
        col1,col2 = st.columns(2)
        with col1:
            st.write("Present in class:")
            for line in attendanceHere:
                st.write(line)
        with col2:
            st.write("Absent")
            for line in attendanceAbsent:
                st.write(line)

    elif readyOrNot == 'n':
        st.write("Come back when you're ready!")
    else:
        st.write("Then why are you here?")


    