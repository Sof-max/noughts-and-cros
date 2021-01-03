board = list(range(1, 10))


def line(board):
    print('_' * 10)
    for i in range(4):
        print('|', board[0+i*3], '|',
              board[1+i*3], '|', board[2+i*3], '|')
        print('_' * 10)

