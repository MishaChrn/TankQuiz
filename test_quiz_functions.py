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
    tank_appearance_quiz_answers = "tank_quiz_answers.csv"
    with open(tank_appearance_quiz_answers, "r") as csvfile:
        tank_appearance_quiz_answers_reader = pd.read_csv(csvfile, usecols=["Pic ID", "Tank Name"])
        for row in tank_appearance_quiz_answers_reader:
            print(str(row)) # Change this line to store the match answers in dictionary.
    assert type(str(row)) == str
