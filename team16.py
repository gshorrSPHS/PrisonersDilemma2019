team_name = 'Tyson Dino Chicken Nuggets'
team_strategy =  'Betray, then do whatever they did last'
strategy_description = 'Copycat'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
      return 'b'
    else:
      if their_history[len(their_history)-1] == 'b':
        return 'b'
      else:
        return 'c'
