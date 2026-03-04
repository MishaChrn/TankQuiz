import csv
import yaml
import pandas as pd


def quiz_selection():
    # Reads the Quiz names from the csv file and shows each Quiz name with its row ID.
    table_of_contents = "table_of_contents.csv"
    with open("table_of_contents.csv", "r") as csvfile:
        table_of_contents_reader = pd.read_csv(csvfile)
    table_of_contents_to_dict = table_of_contents_reader.to_dict(orient="records")
    for row in range(len(table_of_contents_to_dict)):
        print(f"{table_of_contents_to_dict[row]["ID"]}. {table_of_contents_to_dict[row]["Quiz Content"]}: {table_of_contents_to_dict[row]["Quiz Description"]}")

def select_quiz_to_start(player_input):
    # Picks out proper column values from the table_of_content csv file, depending on user's input.
    tank_quiz_answers = "tank_quiz_answers.csv"
    question_compositions = {1: ["Pic ID", "Tank Name"], 2: ["Tank Name", "Tank Class"], 3: ["Tank Name", "Game Play"], 4: ["Pic ID", "Tank Name", "Tank Class", "Trivia"]}
    with open(tank_quiz_answers, "r") as csvfile:
        tank_quiz_answers_reader = pd.read_csv(csvfile, usecols=question_compositions[player_input])
    tank_quiz_answers_dictionary = tank_quiz_answers_reader.to_dict(orient='index') # Modifies the dataframe to the dict type.
    # Creates a random tank quiz question.
    random_question_key_set = set() # Initialize an empty set.
    for question_key in tank_quiz_answers_dictionary:
        # Stores each dictionary key in a set.
        random_question_key_set.add(question_key)
# show question_key as a quiz and pop it from the set, input players answer, check if it's correct

def check_correct_answer(tank_quiz_answers_dictionary, random_question_key_set, player_answer):
    # Pops a random element from the random_question_key_set and stores it in a random_quiz_value.
    random_quiz_value = random_question_key_set.pop()
    # Applies the random_quiz_variable to tank_quiz_answers_dictionary and identifies the corresponding question answers.
    correct_answers = tank_quiz_answers_dictionary[random_quiz_value]
# check if player_answer==tank_quiz_answers_dictionary[random_quiz_value]["Tank Name"]


"""
flow:
quiz_selection() -OK

input("Select a quiz: ")

create_random_tank_appearance_quiz()

input("Answer: ")

check_player_answer(player_answer, expected_answer)
"""

"""
pictures and trivias referenced Wikipedia
game play definitions referenced Blitz Hangar
"""
