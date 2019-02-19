import random 

team_name = 'AsianNation2.0'
team_strategy =  'random first move then plays what its opponent played the previous move'
strategy_description = 'cuz why not'

def move(my_history, their_history, my_score, their_score):
  try:
    return their_history[-1]
  except IndexError:
    return 'c'
  

move('bcc', 'bbc', -34, -56)
