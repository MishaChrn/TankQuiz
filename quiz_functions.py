import csv
import yaml
import pandas as pd


def quiz_selection():
    # Reads the Quiz names from the csv file and shows each Quiz name.
    table_of_contents = "table_of_contents.csv"
    with open("table_of_contents.csv", "r") as csvfile:
        table_of_contents_reader = pd.read_csv(csvfile, usecols=["Quiz Content"])
        for row in table_of_contents_reader["Quiz Content"]:
            print(row)



"""
flow:
quiz_selection()

input("Select a quiz: ")

create_random_tank_appearance_quiz()

input("Answer: ")

check_player_answer(player_answer, expected_answer)
"""

"""
pictures and trivias referenced Wikipedia
game play definitions referenced Blitz Hangar
"""
