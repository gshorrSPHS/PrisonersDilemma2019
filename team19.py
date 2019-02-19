import random

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'b'
    else:
        choices = ['c', 'c', 'c', 'b', 'b', 'b', 'c', 'b', 'c', 'b', 'b']
        return random.choice(choices)
