def pattern(frame):
    length = len(frame)
    print('*********')
    for i in range(length):
        print('*',frame[i], '*')
    print('*********')


frame = ['Hello','World','in','a','frame']
pattern(frame)