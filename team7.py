####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Miracle <3 Fortnite'
team_strategy =  'we will get that golden duck despite its astronamical price of $1.29'
strategy_description = 'Lets make this a miracle and do fortnite dances. JK we are gonna collude with Miracle only. JKJK we are gonna betray on the first turn. Override if we are lower in points, then we will always betray. Collude if our points are higher. Override if their history has two consecutive bb then we will betray. Else we will return b.'

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    # collude on the first move:
    if len(my_history) == 0:
      return 'b'
    if my_score < their_score:
      return 'b'
    if their_history[-2:] == 'bb':
      return 'b'
    if my_score > their_score:
      return 'c'
    else:
      return 'b'
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
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
              result='b'):
         print 'Turn 1 test passed'
     # Test 2: if they betrayed last time, i should betray this time
    if test_move(my_history='bcbccbc',
              their_history='cccbbbb', 
              # Note the scores are for testing move()
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=50, 
              their_score=100,
              result='b'):       
      print 'vengeance test successful.'
