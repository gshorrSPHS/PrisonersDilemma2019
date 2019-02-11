def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    for i in range(len(my_history)):
      if my_history[i] == 'b' or their_history[i] == 'b':
        return 'b'
      else:
        return 'c'
