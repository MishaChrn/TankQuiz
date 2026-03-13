import pytest
import csv
import pandas as pd
import yaml
import random


def test_quiz_selection():
    # Reads the Quiz names from the csv file and shows each Quiz name.
    table_of_contents = "table_of_contents.csv"
    with open("table_of_contents.csv", "r") as csvfile:
        table_of_contents_reader = pd.read_csv(csvfile)
    table_of_contents_to_dict = table_of_contents_reader.to_dict(orient="records")
    assert table_of_contents_to_dict[0]["ID"] == 1
    assert table_of_contents_to_dict[0]["Quiz Content"] == "Quiz 1"
    assert table_of_contents_to_dict[0]["Quiz Description"] == "Tank Appearance Match"

@pytest.mark.parametrize(
    "random_question_key_set, expected_value",
    [([{"Pic ID": "ussr_kv_2", "Tank Name": "KV-2"}, {"Pic ID": "usa_m4a3e8", "Tank Name": "M4A3E8"}, {"Pic ID": "ussr_is_3", "Tank Name": "IS-3"}, {"Pic ID": "germany_leopard_1", "Tank Name": "Leopard 1"}],
    ["ussr_kv_2", "usa_m4a3e8", "ussr_is_3", "germany_leopard_1"])]
)
def test_show_quiz(random_question_key_set, expected_value):
    # Pops a stored question_key and stores it in a new variable.
    random_quiz_value = random_question_key_set.pop()
    assert expected_value.count(random_quiz_value["Pic ID"]) == 1

@pytest.mark.parametrize(
    "random_quiz_value, player_answer, player_input",
    [({"Pic ID": "ussr_kv_2", "Tank Name": "KV-2"}, "KV-2", 1)]
    # Add more variations for player_input == from 2 to 3
)
def test_check_correct_answer(random_quiz_value, player_answer, player_input):
    question_compositions = {1: ["Pic ID", "Tank Name"], 2: ["Tank Name", "Tank Class"], 3: ["Tank Name", "Game Play"],
                             4: ["Pic ID", "Tank Name", "Tank Class", "Trivia"]}
    # Applies the random_quiz_value to tank_quiz_answers_dictionary and identifies the corresponding question answers.
    if player_input == 1:
        correct_answer = random_quiz_value["Tank Name"]
    elif player_input == 2:
        correct_answer = random_quiz_value["Tank Class"]
    elif player_input == 3:
        correct_answer = random_quiz_value["Game Play"]
    else:
        pass

@pytest.mark.parametrize("player_input, expected_answers", [
    (1, [{"Pic ID": "ussr_kv_2", "Tank Name": "KV-2"}, {"Pic ID": "usa_m4a3e8", "Tank Name": "M4A3E8"}, {"Pic ID": "ussr_is_3", "Tank Name": "IS-3"}, {"Pic ID": "germany_leopard_1", "Tank Name": "Leopard 1"}]),
    (2, [{"Tank Name": "KV-2", "Tank Class": "HT"}, {"Tank Name": "M4A3E8", "Tank Class": "MT"}, {"Tank Name": "IS-3", "Tank Class": "HT"}, {"Tank Name": "Leopard 1", "Tank Class": "MT"}]),
    (3, [{"Tank Name": "KV-2", "Game Play": "Peek-A-Boo, Hit & Run, Circle Of Death, 1 vs 1 brawl."}, {"Tank Name": "M4A3E8", "Game Play": "Peek-A-Boo, Long range sniping, Circle Of Death."}, {"Tank Name": "IS-3", "Game Play": "Long range sniping."}, {"Tank Name": "Leopard 1", "Game Play": "Peek-A-Boo, Hit & Run, Circle Of Death, 1 vs 1 brawl."}]),
    (4, [{"Pic ID": "ussr_kv_2", "Tank Name": "KV-2", "Tank Class": "HT", "Trivia": "A heavy 52 ton assault tank with the M-10 152 mm howitzer, the KV-2 was produced at the same time as the KV-1. Due to the size of its heavy turret and gun, the KV-2 was slower and had a much higher profile than the KV-1. Those captured and used by the German Army were known as (Sturm)Panzerkampfwagen KW-II 754(r)."}, {"Pic ID": "usa_m4a3e8", "Tank Name": "M4A3E8", "Tank Class": "MT", }, {"Pic ID": "ussr_is_3", "Tank Name": "IS-3", "Tank Class": "HT", "Trivia": "The IS-3 (also known as Object 703) is a Soviet heavy tank developed in late 1944. Its semi-hemispherical cast turret (resembling that of an upturned soup bowl) became the hallmark of post-war Soviet tanks. Its pike nose design would also be mirrored by other tanks of the IS tank family such as the IS-7 and T-10. Produced too late to see combat in World War II, the IS-3 participated in the Berlin Victory Parade of 1945, the Soviet invasion of Hungary, the Six-Day War, Yom Kippur War, and one was used during the early stages of the Russo-Ukrainian War."}, {"Pic ID": "germany_leopard_1", "Tank Name": "Leopard 1", "Tank Class": "MT", "Trivia": "The Kampfpanzer Leopard, subsequently Leopard 1 following the introduction of the successive Leopard 2, is a main battle tank designed by Porsche and manufactured by Krauss-Maffei in West Germany, first entering service in 1965. Developed in an era when HEAT warheads were thought to make conventional heavy armour of limited value, the Leopard design focused on effective firepower and mobility instead of heavy protection."}])
])
def test_select_quiz_to_start(player_input, expected_answers):
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
    # Pops a random element from the random_question_key_set and stores it in a random_quiz_value.
    random_quiz_value = random_question_key_set.pop()
    # Applies the random_quiz_variable to tank_quiz_answers_dictionary and identifies the corresponding question answers.
    correct_answers = tank_quiz_answers_dictionary[random_quiz_value]
    assert correct_answers in expected_answers

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

@pytest.mark.parametrize("player_answer, expected_answer", [("KV-2", "KV-2"), ("Maus", "KV-2")])
def test_check_player_answer(player_answer, expected_answer):
    # Lets you know if your answer is correct.
    point_earned = 0
    answers_dictionary = {"ussr_kv_2": {"Tank Name": "KV-2", "Tank Class": "HT"}}
    expected_answer = answers_dictionary["ussr_kv_2"]["Tank Name"]
    message_correct = f"Yes! It's {expected_answer}!"
    message_wrong = f"No. It's {expected_answer}."
    if player_answer == expected_answer: # If your answer is correct, it increases the point_earned and shows message_correct.
        point_earned += 1
        print(message_correct)
        assert point_earned == 1
    else: # If your answer is wrong, it doesn't increase the point_earned and shows message_wrong.
        point_earned += 0
        assert point_earned == 0

def test_call_a_random_tank_pic_and_name():
    # Call a correct set of the Pic ID and tank name randomly.
    quiz_quiestions_dictionary = {
        "ussr_kv_2": {"Tank Name": "KV-2", "Tank Class": "HT"},
        "usa_m4a3e8": {"Tank Name": "M4A3E8", "Tank Class": "MT"}
    } # Sample dictionary with tank Pic IDs and correct value sets. This part should be generated by reading the tank_quiz_answers.csv.
    random_target_key = random.choice(list(quiz_quiestions_dictionary.keys())) # Stores a randomly called key.
    random_quiz_question = quiz_quiestions_dictionary[random_target_key] # Accesses the value set associated to the randomly called key.
    assert quiz_quiestions_dictionary[random_target_key]["Tank Name"] == "KV-2" or quiz_quiestions_dictionary[random_target_key]["Tank Name"] == "M4A3E8"
    assert quiz_quiestions_dictionary[random_target_key]["Tank Name"] != "Maus"

@pytest.mark.parametrize("question_dictionary", [{"pic_1": {"Tank Name": "Pic 1 Tank", "Tank Class": "Pic 1 Class"}, "pic_2": {"Tank Name": "Pic 2 Tank", "Tank Class": "Pic 2 Class"}, "pic_3": {"Tank Name": "Pic 3 Tank", "Tank Class": "Pic 3 Class"}, "pic_4": {"Tank Name": "Pic 4 Tank", "Tank Class": "Pic 4 Class"}, "pic_5": {"Tank Name": "Pic 5 Tank", "Tank Class": "Pic 5 Class"}}]) # Sample quiz question sets for test purpose.
def test_create_random_tank_appearance_quiz(question_dictionary):
    # Creates a random tank appearance quiz question.
    random_question_key_set = set() # Initialize an empty set.
    for question_key in question_dictionary:
        # Stores each dictionary key in a set.
        random_question_key_set.add(question_key) # Stores keys in a set. Set elements never duplicate and have no indices.
    for set_element in random_question_key_set:
        print(f"This is {set_element}.")
    assert set_element in question_dictionary

