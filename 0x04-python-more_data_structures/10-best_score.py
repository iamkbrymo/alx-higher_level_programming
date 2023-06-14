#!/usr/bin/python3

def best_score(a_dictionary):
    score = 0
    for k, v in a_dictionary.item():
        if v > score:
            score = v
    return score
