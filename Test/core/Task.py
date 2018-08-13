
new_field = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
sign = ''
default_sign = '_'
turn = 0

attempt_player_1 = 1
attempt_player_2 = 1

diagonal_1 = ['1', '2', '3']
diagonal_2 = ['1', '2', '3']


while turn <= 1000:
    turn += 1
    if turn % 2:
        sign = 'X'
        print "Player one: Your sign is: %s Attempht %s" % (sign, attempt_player_1)
        try:
            row = int(raw_input("Horisontal Row: ")) - 1
            column = int(raw_input("Vertical Col: ")) - 1
            if row in range(0, 3) and column in range(0, 3):
                print
            else:
                '''Get attemphtion again'''
                turn += 1
                print "There is no such row or column, please try again"
        except(ValueError, NameError, KeyboardInterrupt):
            print "You can not input characters or white space"
            exit(0)

    else:
        sign = 'O'
        print "Player two: ", "Your sign is O", "Attempht %s" % attempt_player_2
        try:
            row = int(raw_input("Horisontal Row: ")) - 1
            column = int(raw_input("Vertical Col: ")) - 1
            if row in range(0, 3) and column in range(0, 3):
                print
            else:
                '''Get attemphtion again'''
                turn += 1
                print "There is no such row or column, please try again "
        except(ValueError, NameError, KeyboardInterrupt):
            print "You can not input characters or white space"
            exit(0)

    '''Getting row'''

    a = 0
    while a < 3:
        if a == row:
            '''Getting column'''
            for v in range(len(new_field[a])):
                if v == column:
                    if new_field[a][v] == default_sign:
                        new_field[a][v] = sign

                        '''Check minimal combination to WIN'''
                        if attempt_player_1 >= 3:
                            '''Verification ROWS'''
                            if len(set(new_field[row])) == 1 and sign == 'X':
                                print "Player_1 WINNER"
                            elif len(set(new_field[row])) == 1 and sign == 'O':
                                print "Player_2 WINNER"
                        else:
                            pass
                        '''Verification COLUMNS'''  "Add appemhpt"
                        column_1 = set()

                        for el in new_field:
                            column_1.add(el[v])

                        if a == 0:
                            if v == 0:
                                diagonal_1[v] = new_field[a][v]
                                print "Diag 1 = ", diagonal_1
                            elif v == 2:
                                diagonal_2[v] = new_field[a][v]
                                print "Diag 2 = ", diagonal_2
                        elif a == 1:
                            if v == 1:
                                diagonal_1[v] = new_field[a][v]
                                print "Diag 1 = ", diagonal_1
                                diagonal_2[v] = new_field[a][v] # ???
                                print "Diag 2 = ", diagonal_2
                        elif a == 2:
                            if v == 2:
                                diagonal_1[v] = new_field[a][v]
                                print "Diag 1 = ", diagonal_1
                            elif v == 0:
                                diagonal_2[v] = new_field[a][v]
                                print "Diag 2 = ", diagonal_2
                            else:
                                pass

                        if len(set(diagonal_1)) == 1 and sign == 'X':
                            print "Player_1 WINNER"
                        elif len(set(diagonal_2)) == 1 and sign == 'O':
                            print "Player_2 WINNER"

                        if len(column_1) == 1 and sign == 'X':
                            print "Player_1 WINNER"
                        elif len(column_1) == 1 and sign == 'O':
                            print "Player_2 WINNER"
                        else:
                            pass


                        '''Attemphts counter'''
                        if sign == "X":
                            attempt_player_1 += 1
                        else:
                            attempt_player_2 += 1
                        break

                    else:
                        '''Return again to attempht'''
                        if sign == 'X':
                            turn += 1
                            print "Incorrect choice, try again..."
                        else:
                            turn += 1
                            print "Incorrect choice, try again..."
        a += 1
    for row in new_field:
        print " ".join(row)