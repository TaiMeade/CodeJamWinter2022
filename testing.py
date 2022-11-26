import os
import cv2
# desktopPath = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'))

# newFolder = os.path.join(desktopPath, "qrCodes")
# os.mkdir(newFolder)

# directory = 'files'
 
# # iterate over files in
# # that directory
# folderName = input("Please enter the folder that your QR Codes are stored in: ")

# desktopPath = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop')) # Creds to StackOverflow

# directory = f"{desktopPath}/{folderName}"

# for filename in os.listdir(desktopPath + "\qrCodes"):
#     f = os.path.join(directory, filename)
#     if os.path.isfile(f):
#         d = cv2.QRCodeDetector()
#         value, points, straightQRCode = d.detectAndDecode(cv2.imread(f))
#         print(value)
        
#print(desktopPath)

#-----------------------------------------------------------------------------------------------------------------------


# importing the csv module
# import csv
 
# # field names
# fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# # data rows of csv file
# rows = [ ['Nikhil', 'COE', '2', '9.0'],
#         ['Sanchit', 'COE', '2', '9.1'],
#         ['Aditya', 'IT', '2', '9.3'],
#         ['Sagar', 'SE', '1', '9.5'],
#         ['Prateek', 'MCE', '3', '7.8'],
#         ['Sahil', 'EP', '2', '9.1']]
 
# # name of csv file
# filename = "university_records.csv"
 
# # writing to csv file
# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
     
#     # writing the fields
#     csvwriter.writerow(fields)
     
#     # writing the data rows
#     csvwriter.writerows(rows)


#-----------------------------------------------------------------------------------------------------------------------


# # Makes QR Code for this youtube video.
# import qrcode
# import cv2

# test = qrcode.make("https://www.youtube.com/watch?v=SrZuwM705yE")
# test.save("youtube.jpg")


#-----------------------------------------------------------------------------------------------------------------------


# import requests
# import streamlit as st
# import random

# # Getting JSON based on user inputs and converting to all needed parts
# def getTrivia(categoryType,difficultyLevel,multipleOrTF):

#     listOfCategories = ['Any','General Knowledge','Entertainment: Books','Entertainment: Film','Entertainment: Music','Entertainment: Musicals and Theatres','Entertainment: Television','Entertainment: Video Games','Entertainment: Board Games','Science and Nature','Science: Computers','Science: Math','Mythology','Sports','Geography','History','Politics','Art','Celebrities','Animals','Vehicles','Entertainment: Comics','Science: Gadgets','Entertainment: Japanese Anime/Manga','Entertainment: Cartoon and Animations']

#     # Convert to proper format
#     if difficultyLevel != 'Any':
#         difficultyLevel = difficultyLevel.lower()

#     if multipleOrTF == 'Any':
#         multipleOrTF = 'Any'
#     elif multipleOrTF == 'Multiple Choice':
#         multipleOrTF = 'multiple'
#     elif multipleOrTF == 'True or False':
#         multipleOrTF = 'boolean'
#     else:
#         multipleOrTF = 'ERROR'

#     if categoryType == 'Any' and difficultyLevel == 'Any' and multipleOrTF == 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1")

#     elif categoryType != 'Any' and difficultyLevel == 'Any' and multipleOrTF == 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}")

#     elif categoryType != 'Any' and difficultyLevel != 'Any' and multipleOrTF == 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}&difficulty={difficultyLevel.lower()}")

#     elif categoryType != 'Any' and difficultyLevel != 'Any' and multipleOrTF != 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}&difficulty={difficultyLevel.lower()}&type={multipleOrTF}")

#     elif categoryType == 'Any' and difficultyLevel != 'Any' and multipleOrTF == 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&difficulty={difficultyLevel.lower()}")

#     elif categoryType == 'Any' and difficultyLevel != 'Any' and multipleOrTF != 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&difficulty={difficultyLevel.lower()}&type={multipleOrTF}")

#     elif categoryType != 'Any' and difficultyLevel == 'Any' and multipleOrTF != 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}&type={multipleOrTF}")

#     elif categoryType == 'Any' and difficultyLevel == 'Any' and multipleOrTF != 'Any':
#         triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&type={multipleOrTF}")

#     else:
#         #pass
#         triviaJSON = "ERROR"
#         return triviaJSON

#     triviaJSON = triviaJSON.json()

#     return triviaJSON

# def translateToUseable(triviaJSON):
#     triviaJSONresults = triviaJSON['results']
#     triviaJSONresults = triviaJSONresults[0]
#     category = triviaJSONresults['category']
#     typeOfQuestion = triviaJSONresults['type']
#     difficulty = triviaJSONresults['difficulty']
#     question = triviaJSONresults['question']
#     correctAnswer = triviaJSONresults['correct_answer']
#     incorrectAnswers = triviaJSONresults['incorrect_answers']
#     incorrectAnswers.append(correctAnswer)
#     allAnswers = incorrectAnswers
    
#     return category,typeOfQuestion,difficulty,question,correctAnswer,allAnswers

# def main():

#     categoryType = st.sidebar.selectbox("Category:", ['Any','General Knowledge','Entertainment: Books','Entertainment: Film','Entertainment: Music','Entertainment: Musicals and Theatres','Entertainment: Television','Entertainment: Video Games','Entertainment: Board Games','Science and Nature','Science: Computers','Science: Math','Mythology','Sports','Geography','History','Politics','Art','Celebrities','Animals','Vehicles','Entertainment: Comics','Science: Gadgets','Entertainment: Japanese Anime/Manga','Entertainment: Cartoon and Animations'])
#     difficultyLevel = st.sidebar.selectbox('Difficulty:', ['Any','Easy','Medium','Hard'])
#     multipleOrTF = st.sidebar.selectbox('Type:', ['Any','Multiple Choice','True or False'])

#     if 'triviaJSON' not in st.session_state:
#         st.session_state.triviaJSON = getTrivia(categoryType,difficultyLevel,multipleOrTF)
    
#     if 'category' not in st.session_state:
#         st.session_state.category = ""
    
#     if 'typeOfQuestion' not in st.session_state:
#         st.session_state.typeOfQuestion = ""

#     if 'difficulty' not in st.session_state:
#         st.session_state.difficulty = ""

#     if 'question' not in st.session_state:
#         st.session_state.question = ""
    
#     if 'correctAnswer' not in st.session_state:
#         st.session_state.correctAnswer = ""

#     if 'allAnswers' not in st.session_state:
#         st.session_state.allAnswers = []

#         st.session_state.category,st.session_state.typeOfQuestion,st.session_state.difficulty,st.session_state.question,st.session_state.correctAnswer,st.session_state.allAnswers = translateToUseable(st.session_state.triviaJSON)

#     if st.button("New Question"):
#         # Gets a new question
#         st.session_state.triviaJSON = getTrivia(categoryType,difficultyLevel,multipleOrTF)

#         st.session_state.category,st.session_state.typeOfQuestion,st.session_state.difficulty,st.session_state.question,st.session_state.correctAnswer,st.session_state.allAnswers = translateToUseable(st.session_state.triviaJSON)

#     # NOTE: USING st.write MAKES IT WORK for fixing things like '&quot;' not being '"'...
#     st.write(st.session_state.category)
#     st.write(st.session_state.typeOfQuestion)
#     st.write(st.session_state.difficulty)
#     st.write(st.session_state.question)

#     # Puts them into random order
#     st.write(st.session_state.allAnswers)
#     random.shuffle(st.session_state.allAnswers)
#     answerChoices = []
#     for i in range(len(st.session_state.allAnswers)):
#         answer = f"{chr(i+65)}. {st.session_state.allAnswers[i]}"
#         answerChoices.append(answer)
#         st.write(answer)

#     st.write(answerChoices)

#     with st.form("Form"):
#         userAnswer = st.text_input("A, B, C, or D")            

#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             for answer in answerChoices:
#                 if answer.startswith(userAnswer):
#                     userActualAnswer = answer
#             if userActualAnswer[3:] == st.session_state.correctAnswer:
#                 st.subheader("CORRECT")
#             else:
#                 st.subheader("INCORRECT")
                

# if __name__ == '__main__':
#     main()


#------------------------------------------------------------------------------------------------------------------
# This section was for testing how to fix the HTML entities showing up in selectbox


# import html

# allAnswers = ['Galois&#039; Continued Fractions','Galois Theory','Abelian Integration','Galois&#039; Method for PDE&#039;s']

# print(allAnswers)

# i = 0
# for j in range(len(allAnswers)):
#     allAnswers[j] = html.unescape(allAnswers[j])
#     i += 1

# print(allAnswers)