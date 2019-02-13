team_name = 'Mediators'
team_strategy =  'Collude on first few turns, then betray. Reset cycle at a hundred turns.'
strategy_description = 'You cannot strike it rich by being nice. Sometimes you have to leave some knives in some backs.'
    


def move(my_history, their_history, my_score, their_score):
  if len(my_history) <= 10:
    return 'c'
  elif len(my_history) >= 11 and len(my_history) < 100:
    return 'b'
  elif len(my_history) >= 100 and len(my_history) <= 110:
    return 'c'
  elif len(my_history) > 110:
    return 'b'
