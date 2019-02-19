
import random 

team_name = 'Team 1'
team_strategy =  'Forgiveness'
strategy_description = 'Once you have punished and your opponent begins to cooperate, begin to cooperate with them again to avoid long-term feuding and patterns of revenge.'
    


def move(my_history, their_history, my_score, their_score):
    
  if len(my_history) == 0:
    return 'c'
  # make sure that there's enough history
  elif len(my_history) >= 1 and their_history[-1] == 'b':
    return 'b'
  elif len(my_history) >= 3 and their_history[-3:] == 'ccc':
    return 'b'
  else:
    return 'c'
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

# 1st move should ALWAYS be c
# If opponent's move is c, then continue to c

# ONLY betray after others betray, then collude again

# If opponent's move is betray, then betray on the next move

# If opponent colludes the first 3 moves, mess with them and betray on the last move

    
def test_move(my_history, their_history, my_score, their_score, result):
    # calls move(my_history, their_history, my_score, their_score)
    # from this module. Prints error if return value != result.
    # Returns True or False, dpending on whether result was as expected.
    
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

if __name__ == '__main__':
     
    # Test 1: Collude on the first move
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Turn 1 test passed'
     # Test 2: if they betrayed me then I betray back 
    if test_move(my_history='c',
              their_history='b',
              my_score=0,
              their_score=0,
              result='b'):
          print 'Turn 2 test passed'
    if test_move(my_history='c',
              their_history='c',
              my_score=0,
              their_score=0,
              result='c'):
      # Test 3: if they start collude, forgive them and collude
      if test_move(my_history='cb',
              their_history='bc',
              my_score=0,
              their_score=0,
              result='c'):
          print 'Turn 3 test passed'
      elif test_move(my_history='cb',
              their_history='cb',
              my_score=0,
              their_score=0,
              result='b'):
          print 'Turn 3 test passed'
    #Test 4: Revenge
    if test_move(my_history='ccb',
              their_history='cbc',
              my_score=0, 
              their_score=0,
              result='c'):       
          print 'All moves in test passed.'
    #Test 4: Pull a fast one
    elif test_move(my_history='ccc',
              their_history='ccc',
              my_score=0,
              their_score=0,
              result='b'):
          print 'Oof. All moves in test passed.'
