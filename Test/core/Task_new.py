import itertools

DEFAULT_SIGN = '_'


def get_player(current_player):
    if current_player == 'X':
        print 'Player 1, your sign is %s: ' % current_player
    else:
        print 'Player 2, your sign is %s: ' % current_player


def get_field(board, current_player):
    while True:
        try:
            row = int(raw_input("Horisontal Row: ")) - 1
            column = int(raw_input("Vertical Col: ")) - 1
            if row in range(0, 3) and column in range(0, 3):
                while board[row][column] == DEFAULT_SIGN:
                        field = board[row][column] = current_player
                        return field
                else:
                    print "Incorrect choice, please try again..."
            else:
                print "There is no such row or column, please try again"
        except(ValueError, NameError, KeyboardInterrupt, UnboundLocalError, TypeError):
            print "You can not input characters or white space"


def print_board(board):
    for row in board:
        print " ".join(row)


def print_winner(current_player):
    if current_player == 'X':
        print 'Player 1, WON!!!!!!'

    else:
        print 'Player 2, WON!!!!!!'


def get_winner(board, current_player, attempts):
    new_board = []
    for a in board:
        new_board.extend(a)

    '''Combinations to WIN below'''
    combinations = [new_board[0:3], new_board[3:6], new_board[6:9], new_board[0:7:3], new_board[1:8:3],
                    new_board[2:9:3], new_board[::4], new_board[2:8:2]]

    for combination in combinations:
        if len(set(combination)) == 1 and current_player in combination:
            return print_winner(current_player), exit(0)
            if len(set(combination)) >= 2 and DEFAULT_SIGN not in combination:
                while attempts == 8:
                    print 'There is no combinations to WIN'
                    return exit(0)


def main():
    sign = ('X', 'O')
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
    attempts = 0
    for current_player in itertools.cycle(sign):
        get_player(current_player)
        get_field(board, current_player)
        print_board(board)
        attempts += 1
        while attempts >= 5:
            get_winner(board, current_player, attempts)
            break


if __name__ == '__main__':
    main()








