import itertools


sign = ('X', 'O')
default_sign = '_'
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]
attempts = 0


def get_player():
    if current_player == 'X':
        print 'Player 1, your sign is %s: ' % current_player
    else:
        print 'Player 2, your sign is %s: ' % current_player


def get_field(board):
    while True:
        try:
            row = int(raw_input("Horisontal Row: ")) - 1
            column = int(raw_input("Vertical Col: ")) - 1
            if row in range(0, 3) and column in range(0, 3):
                while board[row][column] == default_sign:
                        field = board[row][column] = current_player
                        return field
                else:
                    print "Incorrect choice, please try again..."
            else:
                print "There is no such row or column, please try again"
        except(ValueError, NameError, KeyboardInterrupt, UnboundLocalError, TypeError):
            print "You can not input characters or white space"


def print_board():
    for row in board:
        print " ".join(row)


def print_winner(current_player):  #Should be static
    if current_player == 'X':
        print 'Player 1, WON!!!!!!'

    else:
        print 'Player 2, WON!!!!!!'


def get_board(board):  #Should be static
    new_board = []
    for a in board:
        new_board.extend(a)
    return new_board


def get_winner(new_board, current_player):
    combinations = [new_board[0:3], new_board[3:6], new_board[6:9], new_board[0:7:3], new_board[1:8:3],
                    new_board[2:9:3], new_board[::4], new_board[2:8:2]]
    #count = 0
    for combination in combinations:
        if len(set(combination)) == 1 and combination.__contains__(current_player):
            return print_winner(current_player), exit(0)
    # if attempts == 8:
    #     print 'There is no way to WIN, just one choice'
    # elif attempts == 9:
    #     print 'The END'
    #     return exit(0)
        elif len(set(combination)) >= 2 and not combination.__contains__(default_sign):
            #count += 1
            while attempts == 8:
                print 'There is no combinations to WIN'
                return exit(0)


for current_player in itertools.cycle(sign):
    get_player()
    get_field(board)
    print_board()
    new_board = get_board(board)
    attempts += 1
    while attempts >= 5:
        get_winner(new_board, current_player)
        break








