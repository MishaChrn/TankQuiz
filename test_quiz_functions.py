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
    assert tank_appearance_quiz_answers_dictionary["Pic ID"][0] == "ussr_kv_2" and tank_appearance_quiz_answers_dictionary["Tank Name"][0] == "KV-2"

def test_tank_role_match_quiz_answers():
    # Reads the correct answers of the Tank Role Match Quiz from the csv file and store them in variables.
    # Uses the same logic as Tank Appearance Match Quiz.
    tank_quiz_answers = "tank_quiz_answers.csv"
    with open(tank_quiz_answers, "r") as csvfile:
        tank_appearance_quiz_answers_reader = pd.read_csv(csvfile, usecols=["Tank Name", "Tank Class"])
    tank_appearance_quiz_answers_dictionary = tank_appearance_quiz_answers_reader.to_dict() # Modifies the dataframe to the dict type.
    assert tank_appearance_quiz_answers_dictionary["Tank Name"][0] == "KV-2" and tank_appearance_quiz_answers_dictionary["Tank Class"][0] == "HT"

def test_read_all_quiz_answers():
    # Reads all answer sets and store them in a dictionary.
    tank_quiz_answers = "tank_quiz_answers.csv"
    with open(tank_quiz_answers, "r") as csvfile:
        tank_appearance_quiz_answers_reader = pd.read_csv(csvfile).set_index("Pic ID") # Uses 'Pic ID' column as an index.
    all_tank_quiz_answers_dictionary = tank_appearance_quiz_answers_reader.to_dict(orient='index') # Modifies the dataframe to the dict type by each row, using the column name as each key.
    assert all_tank_quiz_answers_dictionary["ussr_kv_2"]["Tank Name"] == "KV-2"

def test_check_answer_correct(correct_answer, expected_answer):
    # Lets you know if your answer is correct.
    if correct_answer == expected_answer: # If your answer is correct, it returns True.
        assert True
    else:
        assert False # If your answer is wrong, it returns False.

def test_check_answer_wrong(answer, expected_answer):
    # Lets you know if your answer is correct.
    if wrong_answer == expected_answer: # If your answer is correct, it returns True.
        assert True
    else:
        assert False # If your answer is wrong, it returns False.

# How to use parameters?
# @pytest.fixture can work to set test parameters?

"""
一行一意になるはずなので、
ひょっとして一度に全部呼び出してからマッチングの場合ごとに正誤判定させる方が早くて楽？
df.to_dict(orient='dict')
# {'Name': {0: 'Alice', 1: 'Bob', 2: 'Charlie'}, 'Age': {0: 25, 1: 30, 2: 28}, 'City': {0: 'New York', 1: 'London', 2: 'Paris'}}

df.to_dict(orient='list')
# {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 28], 'City': ['New York', 'London', 'Paris']}

df.to_dict(orient='records')
# [{'Name': 'Alice', 'Age': 25, 'City': 'New York'}, {'Name': 'Bob', 'Age': 30, 'City': 'London'}, {'Name': 'Charlie', 'Age': 28, 'City': 'Paris'}]

df.to_dict(orient='index')
# {0: {'Name': 'Alice', 'Age': 25, 'City': 'New York'}, 1: {'Name': 'Bob', 'Age': 30, 'City': 'London'}, 2: {'Name': 'Charlie', 'Age': 28, 'City': 'Paris'}}
"""