import random 

team_name = 'no high fructose corn syrup'
team_strategy =  'betray is collude is above 50 percent and collude is collude is below 50 percent. betray every fifth turn no matter what.'
strategy_description = 'we do not know what we are doing.'
    


def move(my_history, their_history, my_score, their_score):
  c = 0
  b = 0
  choices = ['c', 'b']

  for letter in their_history:
    if letter == "c":
      c = c + 1
# counting the number of c's
    elif letter == "b":
      b = b + 1
# conting the number of b's
  if len(their_history) == 0:
      return "b"
# betray on the first move
  elif len(their_history) % 5 == 0:
    return "b"
# returns betray every five turns
  elif b > c:
    return "c"
# returns b is b is greater
  elif c > b:
    return "b"
# returns c is c is greater
  else:
    return random.choice(choices)




def test_move(my_history, their_history, my_score, their_score, result):
    # '''calls move(my_history, their_history, my_score, their_score)
    # from this module. Prints error if return value != result.
    # Returns True or False, dpending on whether result was as expected.
    # '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False
# test one : collude on the first move
if test_move(my_history='',
            their_history='', 
            my_score=0,
            their_score=0,
            result='b'):
         print 'Turn 1 test passed'

if test_move(my_history='bcbcc',
              their_history='cccbc', 
              # Note the scores are for testing move()
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b'):       
      print 'vengeance test successful.'
  

  
