import random

team_name = 'The Mighty Morphin\' Power rangers'
team_strat = 'random choice, geared towards betrayl.'
strat_description = 'I wholeheartedly don\'t care. But, that being said, I\'d rather it was you than me.'


def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'b'
    else:
        choices = ['c', 'c', 'c', 'b', 'b', 'b', 'c', 'b', 'c', 'b', 'b']
        return random.choice(choices)
