import random

   
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) == 0:
      return 'c'
    elif 'bbb' in their_history:
      return 'b'
    elif 'ccc' in their_history:
      return 'c'
    elif their_history[-1] == 'c':
      if random.randint(1,2) == 1:
        return 'b'
      else:
        return 'c'
    else:
      return 'b'
