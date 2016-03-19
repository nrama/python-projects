"""
A simple Hang Man game
"""
import random
import os
import json


def get_random_word():
    file_directory = 'dictionary.json'
    json_obj = open(file_directory).read()
    dictionary = json.loads(json_obj)

    num_categories = len(dictionary['game_words'])
    chosen_category_index = random.randint(0, num_categories-1)
    num_words = len(dictionary['game_words'][chosen_category_index]['words'])
    chosen_word_index = random.randint(0, num_words-1)
    category = dictionary['game_words'][chosen_category_index]['category']
    word = (dictionary['game_words'][chosen_category_index]['words']
    [chosen_word_index])

    return {'category': category, 'word': word}

def hangman_drawer(num_tries, max_tries):
    """
    print HangMan
    """
    setup_top = " _ _ _"
    setup_side = "|"
    rope_or_body = "|  |"
    head = "|  o"
    left_arm = "| /|"
    right_arm = "| /|\\"
    left_leg = "| /"
    right_leg = "| / \\"

    print setup_top

    if num_tries == 0:
        for i in range(4):
            print setup_side

    elif num_tries == 1:
        print rope_or_body
        for i in range(3):
            print setup_side

    elif num_tries == 2:
        print rope_or_body
        print head
        for i in range(2):
            print setup_side

    elif num_tries == 3:
        print rope_or_body
        print head
        print rope_or_body
        print setup_side

    elif num_tries == 4:
        print rope_or_body
        print head
        print left_arm
        print setup_side

    elif num_tries == 5:
        print rope_or_body
        print head
        print right_arm
        print setup_side

    elif num_tries == 6:
        print rope_or_body
        print head
        print right_arm
        print left_leg

    elif num_tries == 7:
        print rope_or_body
        print head
        print right_arm
        print right_leg

    if num_tries == 7:
        print "                           ", max_tries-num_tries, "try left"

    else:
        print "                           ", max_tries-num_tries, "tries left"

def ask_continue():
    """
    Check user wants to restart game
    """

    response = raw_input("Try Again? (y/n): ")

    if response == "y":
        hangman_game()
    elif response == "n":
        print "Good Bye!"
        exit()
    else:
        ask_continue()

def hangman_game():
    """
    HangMan Logic
    """

    blank = "_"
    guesses = ""
    guess = ""
    tries = 0
    max_tries = 8

    rand_gen = get_random_word()
    word = rand_gen['word']
    category = rand_gen['category']

    while tries < max_tries:
        os.system('cls')
        is_blank_found = False

        hangman_drawer(tries, max_tries)
        print
        print "Category:", category
        print
        print
        print

        if tries > 0:
            print "Incorrect Guesses:",
            for char in guesses:
                if char not in word:
                    print char,
            print
            print

        for char in word:
            if char in guesses:
                print char,
            else:
                is_blank_found = True
                print blank,

        print

        if is_blank_found is False:
            print
            print "Well Done!"
            print
            ask_continue()

        guess = raw_input()
        guesses += guess.lower()

        if guess.lower() not in word:
            tries += 1

    print
    print "Game Over!"
    print "Correct Word Was:", word
    ask_continue()


if __name__ == "__main__":
    hangman_game()
