"""

Tai Meade
Use open trivia API to get a random trivia question...allow user to select correct answer

"""

import requests
import streamlit as st
import random
import soundFX
import html
from playsound import playsound

# Getting JSON based on user inputs and converting to all needed parts
def getTrivia(categoryType,difficultyLevel,multipleOrTF):

    listOfCategories = ['Any','General Knowledge','Entertainment: Books','Entertainment: Film','Entertainment: Music','Entertainment: Musicals and Theatres','Entertainment: Television','Entertainment: Video Games','Entertainment: Board Games','Science and Nature','Science: Computers','Science: Math','Mythology','Sports','Geography','History','Politics','Art','Celebrities','Animals','Vehicles','Entertainment: Comics','Science: Gadgets','Entertainment: Japanese Anime/Manga','Entertainment: Cartoon and Animations']

    # Convert to proper format
    if difficultyLevel != 'Any':
        difficultyLevel = difficultyLevel.lower()

    if multipleOrTF == 'Any':
        multipleOrTF = 'Any'
    elif multipleOrTF == 'Multiple Choice':
        multipleOrTF = 'multiple'
    elif multipleOrTF == 'True or False':
        multipleOrTF = 'boolean'
    else:
        multipleOrTF = 'ERROR'

    if categoryType == 'Any' and difficultyLevel == 'Any' and multipleOrTF == 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1")

    elif categoryType != 'Any' and difficultyLevel == 'Any' and multipleOrTF == 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}")

    elif categoryType != 'Any' and difficultyLevel != 'Any' and multipleOrTF == 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}&difficulty={difficultyLevel.lower()}")

    elif categoryType != 'Any' and difficultyLevel != 'Any' and multipleOrTF != 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}&difficulty={difficultyLevel.lower()}&type={multipleOrTF}")

    elif categoryType == 'Any' and difficultyLevel != 'Any' and multipleOrTF == 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&difficulty={difficultyLevel.lower()}")

    elif categoryType == 'Any' and difficultyLevel != 'Any' and multipleOrTF != 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&difficulty={difficultyLevel.lower()}&type={multipleOrTF}")

    elif categoryType != 'Any' and difficultyLevel == 'Any' and multipleOrTF != 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&category={(listOfCategories.index(categoryType)) + 8}&type={multipleOrTF}")

    elif categoryType == 'Any' and difficultyLevel == 'Any' and multipleOrTF != 'Any':
        triviaJSON = requests.get(f"https://opentdb.com/api.php?amount=1&type={multipleOrTF}")

    else:
        #pass
        triviaJSON = "ERROR"
        return triviaJSON

    triviaJSON = triviaJSON.json()

    return triviaJSON

def translateToUseable(triviaJSON):
    triviaJSONresults = triviaJSON['results']
    triviaJSONresults = triviaJSONresults[0]
    category = triviaJSONresults['category']
    typeOfQuestion = triviaJSONresults['type']
    difficulty = triviaJSONresults['difficulty']
    question = triviaJSONresults['question']
    correctAnswer = triviaJSONresults['correct_answer']
    correctAnswer = [correctAnswer]
    incorrectAnswers = triviaJSONresults['incorrect_answers']
    allAnswers = incorrectAnswers + correctAnswer

    # Fixes things that should appear as symbols/characters but were HTML entities
    i = 0
    for j in range(len(allAnswers)):
        allAnswers[j] = html.unescape(allAnswers[j])
        i += 1
    # Does same thing for variable correct answer
    i = 0
    for j in range(len(correctAnswer)):
        correctAnswer[j] = html.unescape(correctAnswer[j])
        i += 1

    return category,typeOfQuestion,difficulty,question,correctAnswer,allAnswers

def main():

    st.title("Trivia Game :question: :grey_question:")

    # Goal
    st.subheader("Goal:")
    st.write("This program/page uses an API to get trivia questions that can be separated via the options on the left. This program is meant to help the teacher learn more about a little bit of everything, or something more specific if they want to. This can also be used to test your knowledge! In general, it is meant to help educate the user, while helping them have fun!")
    
    # Notes
    with st.expander("Notes:"):
        st.write("* You get unlimited tried on each question, so don't worry if you get it wrong!")
        st.write("* There is a slight delay for answers to submit...just a heads up!")
        st.write("* Have fun!")
        
    st.write("---")

    try:
        categoryType = st.sidebar.selectbox("Category:", ['Any','General Knowledge','Entertainment: Books','Entertainment: Film','Entertainment: Music','Entertainment: Musicals and Theatres','Entertainment: Television','Entertainment: Video Games','Entertainment: Board Games','Science and Nature','Science: Computers','Science: Math','Mythology','Sports','Geography','History','Politics','Art','Celebrities','Animals','Vehicles','Entertainment: Comics','Science: Gadgets','Entertainment: Japanese Anime/Manga','Entertainment: Cartoon and Animations'])
        difficultyLevel = st.sidebar.selectbox('Difficulty:', ['Any','Easy','Medium','Hard'])
        multipleOrTF = st.sidebar.selectbox('Type:', ['Any','Multiple Choice','True or False'])

        try:
            if 'triviaJSON' not in st.session_state:
                st.session_state.triviaJSON = ""

            if 'category' not in st.session_state:
                st.session_state.category = ""
            
            if 'typeOfQuestion' not in st.session_state:
                st.session_state.typeOfQuestion = ""

            if 'difficulty' not in st.session_state:
                st.session_state.difficulty = ""

            if 'question' not in st.session_state:
                st.session_state.question = ""
            
            if 'correctAnswer' not in st.session_state:
                st.session_state.correctAnswer = ""

            if 'allAnswers' not in st.session_state:
                st.session_state.allAnswers = []

            if st.button("New Question"):
                # Gets a new question
                st.session_state.triviaJSON = getTrivia(categoryType,difficultyLevel,multipleOrTF)

                st.session_state.category,st.session_state.typeOfQuestion,st.session_state.difficulty,st.session_state.question,st.session_state.correctAnswer,st.session_state.allAnswers = translateToUseable(st.session_state.triviaJSON)

                if ['shuffledAnswers'] not in st.session_state:
                    st.session_state.shuffledAnswers = random.sample(st.session_state.allAnswers, len(st.session_state.allAnswers))

                st.session_state.answer = ""

            # NOTE: USING st.write MAKES IT WORK for fixing things like '&quot;' not being '"'...API I used has weird formatting
            st.write("---")
            st.write(f"Category: ***{st.session_state.category}***")
            st.write(f"Difficulty: **{st.session_state.difficulty.title()}**")
            st.write("---")
            st.write("**Question:**")
            st.write(st.session_state.question)


            
            # Currently has an issue that it does not convert HTML code to normal text...not sure how to fix
            if 'answer' not in st.session_state:
                st.session_state.answer = st.selectbox("filler",[""] + st.session_state.shuffledAnswers, key=0, label_visibility="hidden")
            st.session_state.answer = st.selectbox("filler",[""] + st.session_state.shuffledAnswers, key=1, label_visibility="hidden")





            # st.session_state.answer = st.radio(question,allAnswers, key=1)
            if st.session_state.answer != "":
                if st.session_state.answer == st.session_state.correctAnswer[0]:
                    st.subheader(":thumbsup: CORRECT :thumbsup:")
                    playsound("soundFX/tada-fanfare-a-6313.mp3")
                else:
                    st.subheader(":thumbsdown: INCORRECT :thumbsdown:")
                    playsound("soundFX/wrong.mp3")
        except Exception as e:
            #st.write(e)
            pass
    except Exception:
        pass

                

if __name__ == '__main__':
    main()