from quiz_functions import quiz_selection

"""
This is a tank quiz app.
What can you do with this app:
1. Choose a quiz category to challenge in the table of contents.
2. Tank Appearance Match: See a picture of a tank and choose a correct tank name and its nation.
3. Tank Role Match: See a tank name and choose a correct tank class.
4. Tank Gameplay Match: See a tank name and choose a correct gameplay description.
5. Tank Trivia: Choose a tank to read about its history.
"""


if __name__ == "__main__":
    try:
        quiz_selection()
    except Exception as e:
        print(e)