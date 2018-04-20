row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

print(row1)
print(row2)
print(row3)

win = False
player1_played = False
player2_played = True
exhaust_board = 0

def board(row1, row2, row3):
    print_row(row1)
    print_row(row2)
    print_row(row3)

def print_row(row):
    for item in row:
        print(str(item) + '  ', end='')
    print('\n')

def check_winner(row1, row2, row3, player):
    global win
    if row1[0] == row2[0] and row2[0] == row3[0]:
        print(f'{player} wins')
        win = True
    elif row1[1] == row2[1] and row2[1] == row3[1]:
        print(f'{player} wins')
        win = True
    elif row1[2] == row2[2] and row2[2] == row3[2]:
        print(f'{player} wins')
        win = True

    if row1[0] == row1[1] and row1[1] == row1[2]:
        print(f'{player} wins')
        win = True
    elif row2[0] == row2[1] and row2[1] == row2[2]:
        print(f'{player} wins')
        win = True
    elif row3[0] == row3[1] and row3[1] == row3[2]:
        print(f'{player} wins')
        win = True

    if row1[0] == row2[1] and row2[1] == row3[2]:
        print(f'{player} wins')
        win = True
    elif row1[2] == row2[1] and row2[1] == row3[0]:
        print(f'{player} wins')
        win = True


def play(player):
    try:
        global exhaust_board
        position = int(input('select position to play: '))

        if player == 'player1':
            card_number = 'X'
        else:
            card_number = 'O'

        card = input(f'Please type {card_number} to play: ')

        if player == 'player1' and card != 'X':
            print('Invalid input')
            play(player)
        elif player == 'player2' and card != 'O':
            print('Invalid input')
            play(player)
        else:
            if position in row1:
                exhaust_board += 1
                index = row1.index(position)
                row1[index] = card

                board(row1, row2, row3)
                check_winner(row1, row2, row3, player)
            elif position in row2:
                exhaust_board += 1
                index = row2.index(position)
                row2[index] = card

                board(row1, row2, row3)
                check_winner(row1, row2, row3, player)
            else:
                exhaust_board += 1
                index = row3.index(position)
                row3[index] = card

                board(row1, row2, row3)
                check_winner(row1, row2, row3, player)
    except ValueError:
        print("please select a number in the board")
        play(player)

while not win:
    if exhaust_board == 9 and win == False:
        print('Draw')

    if not player1_played:
        print('Player1 your turn')
        play('player1')
        player1_played = True
        player2_played = False
    else:
        print('Player2 your turn')
        play('player2')
        player1_played = False
        player2_played = True



