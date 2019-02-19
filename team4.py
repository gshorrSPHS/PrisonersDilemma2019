# 1 move is always colude
# 2 move is 
team_name = 'MoRdOmSlAyEr'
team_name = 'wol'
strategy_description = 'collude as much as possible because it does not hurt to and betrey every 3 times.'

def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'b'
  elif (len(my_history)+1) % 3 == 0:
    return 'c' 
  else:
    return 'b'
move()
