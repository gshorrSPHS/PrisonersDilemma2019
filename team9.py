from __future__ import print_function
import replit 
replit.clear()

# c = collude
# B = betray 

team_name = 'jESsMIrDeR'
team_strategy =  "We betray the first time just for fun :). If they betray us, we'll betray them. If they collude the last time, we'll still betray them :)) If they collude more than half the time, we'll also collude."
strategy_description = 'jess likes betraying. so does mir.'


def counting_c(their_history):
  c=0
  for letter in their_history:
    if letter == "c":
      c= c + 1
    else:
      c = c + 0
  return c  


# Test 1: Betray on the First Move 
def move (my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return "b" # return instead of print
  elif int(counting_c(their_history)) > len(their_history)/2:
    return 'c'
  else:
    return "b"
