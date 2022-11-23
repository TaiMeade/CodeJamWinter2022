"""

Tai Meade
Use open trivia API to get a random trivia question...allow user to select correct answer

"""

import requests
import streamlit as st
import random

# Getting JSON and converting to all needed parts
def getTrivia():
    triviaJSON = requests.get("https://opentdb.com/api.php?amount=1")
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

triviaJSON = getTrivia()
category,typeOfQuestion,difficulty,question,correctAnswer,allAnswers = translateToUseable(triviaJSON)

# NOTE: USING st.write MAKES IT WORK for fixing things like '&quot;' not being '"'...
st.write(category)
st.write(typeOfQuestion)
st.write(difficulty)
st.write(question)
st.write(allAnswers)