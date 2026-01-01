import pytest
import csv
import pandas as pd
import yaml


def test_quiz_selection():
    # Reads the Quiz names from the csv file and shows each Quiz name.
    table_of_contents = "table_of_contents.csv"
    with open("table_of_contents.csv", "r") as csvfile:
        table_of_contents_reader = pd.read_csv(csvfile, usecols=["Quiz Content"])
        for row in table_of_contents_reader:
            print(row)
    assert type(row) == str

def test_tank_appearance_quiz_answers():
    # Reads the correct answers of the Tank Appearance Match Quiz from the csv file and store them in variables.
    # The Tank Role Match Quiz works under the same logic.
    tank_quiz_answers = "tank_quiz_answers.csv"
    with open(tank_quiz_answers, "r") as csvfile:
        tank_appearance_quiz_answers_reader = pd.read_csv(csvfile, usecols=["Pic ID", "Tank Name"])
    tank_appearance_quiz_answers_dictionary = tank_appearance_quiz_answers_reader.to_dict() # Modifies the dataframe to the dict type.
    assert tank_appearance_quiz_answers_dictionary["Pic ID"][0] == 1 and tank_appearance_quiz_answers_dictionary["Tank Name"][0] == "KV-2"

def test_tank_role_match_quiz_answers():
    # Reads the correct answers of the Tank Role Match Quiz from the csv file and store them in variables.
    # Uses the same logic as Tank Appearance Match Quiz.
    tank_quiz_answers = "tank_quiz_answers.csv"
    with open(tank_quiz_answers, "r") as csvfile:
        tank_appearance_quiz_answers_reader = pd.read_csv(csvfile, usecols=["Tank Name", "Tank Class"])
    tank_appearance_quiz_answers_dictionary = tank_appearance_quiz_answers_reader.to_dict() # Modifies the dataframe to the dict type.
    assert tank_appearance_quiz_answers_dictionary["Tank Name"][0] == "KV-2" and tank_appearance_quiz_answers_dictionary["Tank Class"][0] == "HT"
