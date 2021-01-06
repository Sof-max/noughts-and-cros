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


def checking_field(board):
    possible_option = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                       (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)),
    for each in possible_option:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        line(board)
        if counter % 2 == 0:
            start_input("X")
        else:
            start_input("O")
