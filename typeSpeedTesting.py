"""

Tai Meade
CSC 221
Create a game that allows a user to practice their typing speed by typing a paragraph while being timed

"""

# import time
import random
import datetime
import streamlit as st

# Gets the word or sentence randomly that the user will need to type
def getThingToType():
    thingsToType = {
                        "sentence":[
                                    "The brown cow decided to jump over the moon, shortly after the werewolf chased it for nearly 12 miles.",
                                    "There was a random person named Jerry Jougenhopper that created the art of persuasion. Yes, this sentence is fictional.",
                                    "Many people believe that the Marvel Cinematic Universe's movies are significantly better than the DC Universe movies. These people are right.",
                                    "Back in high school, I used to go to Chemistry class and learn about Chemistry. For some reason, I would then go to my Gym class and learn about how to take a dodgeball to the face without crying...",
                                    "I used to be one of the cool kids in high school. Now, I'm just a guy who used to be a cool kid in high school.",
                                    "I love playing video games. I always have and I always will. I'm not addicted to anything, you are.",
                                    "These sentences are getting dumber by the minute. Thank you for playing my TypeSpeedTester though!",
                                    "Sometimes you need to be tested so good luck typing supercalifragilisticexpialidocious quickly and accurately!",
                                    "This sentence is going to be extremely long because I feel that your words per minute have been inflated, and along with them, your confidence. You must be reminded that typing is not meant to be fun or easy.",
                                    "Beach-combing replaced wine tasting as his new obsession. Thigh-high in the water, the fisherman's hope for dinner soon turned to despair.",
                                    "While all her friends were positive that Mary had a sixth sense, she knew she actually had a seventh sense.",
                                    "Giving directions that the mountains are to the west only works when you can see them.",
                                    "If eating three-egg omelets causes weight-gain, budgie eggs are a good substitute.",
                                    "It was a slippery slope and he was willing to slide all the way to the deepest depths.",
                                    "Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn't and they don't recommend anyone else do it either.",
                                    "Sometimes it is better to just walk away from things and go back to them later when you're in a better frame of mind.",
                                    "The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it.",
                                    "You should never take advice from someone who thinks red paint dries quicker than blue paint.",
                                    "I'm worried by the fact that my daughter looks to the local carpet seller as a role model.",
                                    "Most shark attacks occur about 10 feet from the beach since that's where the people are.",
                                    "When I was younger, I used to play baseball. I remember hitting my first and only home run. One of the most exhilarating experiences of my life.",
                                    "I hope everyone is enjoying my TypeSpeedTester, I truly enjoyed creating this!",
                                    "Maybe one day when Mary gets married, we can finally meet her boyfriend...well husband technically.",
                                    "Sally sells seashells down by the seashore.",
                                    "I'm not the pheasant plucker, I'm the pheasant plucker's son. I'm only plucking pheasants until the pheasant plucker comes.",
                                    "This past weekend, I went a Carolina Panthers game and when I got back to where I parked, my car was gone. Turns out I got towed!",
                                    "Sometimes coding can be difficult, frustrating, or even downright infuriating. However, almost nothing beats the feeling of finally getting your program you so much blood, sweat, and tears into to work."
                        ]
    }

    wordOrSentence = random.choice(thingsToType['sentence'])

    return wordOrSentence



def main():
    
    st.title("TypeSpeedTester")

    st.subheader("Goal:")

    st.write("This program/page is designed to help the user practice their typing speed. Once the 'New Game' button is clicked, a background timer will begin and track how long it takes you to complete it. It will use this number, along with the length of the sentence to calculate your letters typed per second, and of course your words per minute. Good luck, and have fun!")
    st.write("Note: There a limited number of random sentences, also please read the Rules/Tips below :arrow_down: :arrow_down: :arrow_down:")
    st.write("---")

    with st.expander("RULES/TIPS:"):
        st.text("""
                1.  All entries must match EXACTLY to the passage/word you are given.\n
                2.  All sentences are separated with a single space.\n
                3.  The WPM is calculated according to the universal formula: ((charactersTyped/5) / minutesTaken)\n
                4.  I STRONGLY suggest deleting your input before beginning a new game...otherwise it will force you to delete your previous answer.
        """)

    if 'goalToType' not in st.session_state:
        st.session_state.goalToType = ""

    if st.button("New Game"):

        # Starts New Game
        st.session_state.goalToType = getThingToType()

        # Start time
        st.session_state.startTime = datetime.datetime.utcnow()

    

    col1, col2 = st.columns(2)

    # Starts game if button has been pressed...thanks to session state it will also not refresh page unless button is pressed (by default it refreshes everytime that the user types something into the text input box)
    if st.session_state.goalToType != '':

        try:
            # Centers the "New Game" button once it has been pressed
            st.markdown(
                    """
                    <style>
                    .css-1uqmt5j {
                    margin-left: 46.5%;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            with col1:
                st.write("---")
                st.write(f"Your goal is to type:")
                st.write(st.session_state.goalToType)
                st.write("---")
            
                userInput = ""

                userInput = st.text_input("TYPE AS FAST AS POSSIBLE:")

            with col2:
                # Centers results and the user's goal to type...increases readability
                st.write("---")
                st.subheader("RESULTS:")
                st.markdown(
                    """
                    <style>
                    .css-keje6w {
                    text-align: center;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                if userInput == st.session_state.goalToType:
                    endTime = datetime.datetime.utcnow()
                    timeTaken = ((endTime - st.session_state.startTime).total_seconds())
                    minutesTaken = timeTaken / 60
                        
                elif userInput == "":
                    pass

                elif userInput != st.session_state.goalToType:
                    st.write("That was incorrect. I'm sorry, but you have failed this test.  Get better at typing lol.")
                    
            
                st.write(f"It took you {timeTaken:.2f} seconds to complete this.")

                # Simple letters/characters per second calculation
                lettersPerSecond = len(st.session_state.goalToType) / timeTaken

                # Formula for WPM according to Google
                wordsPerMinute = (len(st.session_state.goalToType) / 5) / minutesTaken

                st.write(f"That's approximately {lettersPerSecond:.2f} letters per second!")
                st.write(f"That's approximately {wordsPerMinute:.2f} words per minute!")
        
        except Exception as e:
            pass

if __name__ == '__main__':
    
    main()