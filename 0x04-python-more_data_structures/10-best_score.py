#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    highest_value = float('-inf')
    score = ''
    for key, value in a_dictionary.items():
        if value > highest_value:
            highest_value = value
            score = key

    return score
