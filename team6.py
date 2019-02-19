team_name = 'screw everyone'
team_strategy =  'look at the ratio'
strategy_description = 'by betraying you earn more points or loses less points than by colluding. We will set up ratio of c/b and if the ratio is smaller than 1/2, we will betray. If the ratio is bigger than 1/2, we will collude.'
    

def move(my_history, their_history, my_score, their_score):
  c, b = 0, 0
  for letter in their_history:
    if "c" in letter:
      c = c+1
    if "b" in letter:
      b = b+1

  if len(my_history) == 0:
    return 'b'
  if len(my_history) >= 1:
    if their_score >= -300:
      if b == 0:
        return 'b'
      elif float(c) / b <= 0.5:
        return 'b'
      elif float(c) / b >= 0.5:
        return 'c'
    if their_score <= -300:
      return 'b'
  return 'b'
