board = list(range(1, 10))


def line(board):
    print('_' * 10)
    for i in range(4):
        print('|', board[0+i*3], '|',
              board[1+i*3], '|', board[2+i*3], '|')
        print('_' * 10)


def start_input(player_symbol):
    act = False
    while not act:
        player_answer = input("Where to put" + player_symbol + " ?")
        try:
            player_answer = int(player_answer)
        except:
            print('Are you sure you entered the number?')
            continue
    if player_answer >= 1 and player_answer <= 9:
        if (str(board[player_answer - 1])not in "XO"):
            board[player_answer - 1] = player_symbol
            act = True
        else:
            print("This place is already occupied.")
    else:
        print("Enter  number ftom1 to 9.")
