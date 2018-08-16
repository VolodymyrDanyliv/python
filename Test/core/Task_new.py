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


for current_player in itertools.cycle(sign):
    get_player()
    selected_field = get_field(board)
    print_board()



