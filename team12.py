import random 

team_name = 'Bird'
team_strategy =  "Birds"
strategy_description = 'Collude for the first two times no matter what. Then always betray in every 3 turns. If the score difrence is greater than -2000 always betray. If they collude more than 3/5 of the time always betray after 10th turn. Else collude'

def move(mh, th, ms, ts):

  tc,tb,ms,ts=0,0,0,0
 
  for letter in th:
    if letter == "c":
      tc +=1
  cbr = tc/len(th)

  if len(mh) > 3:
    return 'c'
  if len(mh) > 4:  
    return 'b'  
  elif mh[-3:] == 'bcc' :
    return 'b'
  if [ms-ts] < (-2000):
    return 'b'
  if cbr > .6 and len(mh) > 9:
    return 'b'
  else:
    return 'c'
