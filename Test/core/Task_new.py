import itertools


sign = ('X', 'O')
default_sign = '_'
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]


def get_player():
    if current_player == 'X':
        print 'Player 1, your sign is %s: ' % current_player
    else:
        print 'Player 2, your sign is %s: ' % current_player


def get_field():
    try:
        row = int(raw_input("Horisontal Row: ")) - 1
        column = int(raw_input("Vertical Col: ")) - 1
        if row in range(0, 3) and column in range(0, 3):
            if board[row][column] == default_sign:
                field = board[row][column] = current_player
                return field
            else:
                print "Incorrect choice, please try again..."
                get_field()
        else:
            print "There is no such row or column, please try again"
            get_field()
    except(ValueError, NameError, KeyboardInterrupt, UnboundLocalError, TypeError):
        print "You can not input characters or white space"
        get_field()


def print_board():
    for row in board:
        print " ".join(row)


for current_player in itertools.cycle(sign):
    get_player()
    selected_field = get_field()
    print_board()


