import random 

team_name = 'Mickey\'s gang'
team_strategy =  'heads collude, tails betray'
strategy_description = 'The world is cruel. And the only morality in a cruel world is chance.'
    
def move(my_history, their_history, my_score, their_score):
  col = 0
  bet = 0
  for letter in their_history:
    if letter == 'c':
      col = col+1
    if letter == 'b':
      bet = bet+1
  if len(their_history) >= 10:
    if float(col)/float(len(their_history))*100 >= 70.0:
      return 'b'
    if float(bet)/float(len(their_history))*100 >= 70.0:
      return 'b'

  if len(their_history) == 0:
    print "option 3"
    return 'b'
  if len(their_history) == 1:
    if their_history == 'c':
      return 'c' 
    else:
      return 'b'
      
  if len(their_history) >= 3:
    if their_history[-3:] == 'ccc':
      return 'b'
    elif their_history[-3:] == 'bbb':
      return 'c'

  if len(their_history) >= 2:
    if their_history[-2:] == 'bc' or their_history[-2:] == 'cb':
      return 'c'
    elif their_history[-1:] == 'c':
      return 'c'  
    elif their_history[-1:] == 'b':
      return 'b'
