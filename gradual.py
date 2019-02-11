def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    enemybetrayals = 0
    ourbetrayals = 0
    c = 0
    count = 0
    for i in range(len(their_history)):
      if their_history[i] == 'b':
        enemybetrayals = enemybetrayals + 1

    if len(my_history) == 0:
      return 'c'
    elif len(my_history) == 1:
      return 'c'
    else:
      if my_history[len(my_history)-1] == 'c':
        if my_history[len(my_history)-2] == 'c':
          while c == 0:
            count = count + 1
            if my_history[len(my_history)-count] == 'b':
              ourbetrayals = ourbetrayals + 1
            else:
              c=1
          if ourbetrayals != enemybetrayals:
            return 'b'
          else:
            return 'c'
        else:
          return 'c'
  
