"""

Tai Meade
Use open trivia API to get a random trivia question...allow user to select correct answer

"""

import requests
import streamlit as st
import random

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
    incorrectAnswers = triviaJSONresults['incorrect_answers']
    incorrectAnswers.append(correctAnswer)
    allAnswers = incorrectAnswers
    
    return category,typeOfQuestion,difficulty,question,correctAnswer,allAnswers

def main():

    categoryType = st.sidebar.selectbox("Category:", ['Any','General Knowledge','Entertainment: Books','Entertainment: Film','Entertainment: Music','Entertainment: Musicals and Theatres','Entertainment: Television','Entertainment: Video Games','Entertainment: Board Games','Science and Nature','Science: Computers','Science: Math','Mythology','Sports','Geography','History','Politics','Art','Celebrities','Animals','Vehicles','Entertainment: Comics','Science: Gadgets','Entertainment: Japanese Anime/Manga','Entertainment: Cartoon and Animations'])
    difficultyLevel = st.sidebar.selectbox('Difficulty:', ['Any','Easy','Medium','Hard'])
    multipleOrTF = st.sidebar.selectbox('Type:', ['Any','Multiple Choice','True or False'])

    if 'triviaJSON' not in st.session_state:
        st.session_state.triviaJSON = getTrivia(categoryType,difficultyLevel,multipleOrTF)

    if st.button("New Question"):
            # Gets a new question
            st.session_state.triviaJSON = getTrivia(categoryType,difficultyLevel,multipleOrTF)

    category,typeOfQuestion,difficulty,question,correctAnswer,allAnswers = translateToUseable(st.session_state.triviaJSON)

    # NOTE: USING st.write MAKES IT WORK for fixing things like '&quot;' not being '"'...
    st.write(category)
    st.write(typeOfQuestion)
    st.write(difficulty)
    st.write(question)
    st.write(allAnswers)


if __name__ == '__main__':
    main()