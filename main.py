from random import choice
import time


def print_board():
    print("\n" * 22)
    print(row1)
    print('- - - - -')
    print(row2)
    print('- - - - -')
    print(row3)


def computer_move(available_options):
    computer_choice = choice(available_options)
    options.remove(computer_choice)
    return computer_choice


def check_winner(row_1, row_2, row_3):
    count = {"x1": 0,
             "o1": 0,
             "x2": 0,
             "o2": 0,
             "x3": 0,
             "o3": 0,
             "xV1": 0,
             "oV1": 0,
             "xV2": 0,
             "oV2": 0,
             "xV3": 0,
             "oV3": 0,
             "ddx": 0,
             "ddo": 0,
             "dux": 0,
             "duo": 0,
             }

    vert_1 = [row_1[0], row_2[0], row_3[0]]
    vert_2 = [row_1[4], row_2[4], row_3[4]]
    vert_3 = [row_1[8], row_2[8], row_3[8]]
    diagonal_down = [row_1[0], row_2[4], row_3[8]]
    diagonal_up = [row_3[0], row_2[4], row_1[8]]
    for char in row_1:
        if char == 'x':
            count['x1'] += 1
        elif char == 'o':
            count['o1'] += 1
    for char in row_2:
        if char == 'x':
            count['x2'] += 1
        elif char == 'o':
            count['o2'] += 1
    for char in row_3:
        if char == 'x':
            count['x3'] += 1
        elif char == 'o':
            count['o3'] += 1
    for char in vert_1:
        if char == 'x':
            count['xV1'] += 1
        elif char == 'o':
            count['oV1'] += 1
    for char in vert_2:
        if char == 'x':
            count['xV2'] += 1
        elif char == 'o':
            count['oV2'] += 1
    for char in vert_3:
        if char == 'x':
            count['xV3'] += 1
        elif char == 'o':
            count['oV3'] += 1
    for char in diagonal_down:
        if char == 'x':
            count['ddx'] += 1
        elif char == 'o':
            count['ddo'] += 1
    for char in diagonal_up:
        if char == 'x':
            count['dux'] += 1
        elif char == 'o':
            count['duo'] += 1
    if 3 in count.values():
        winner_type = [i for i in count if count[i] == 3]
        if "x" in winner_type[0]:
            print("\nYOU WON!!")
            return False
        else:
            print('\nYou Lost!')
            return False
    return True


options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

row1 = '1 | 2 | 3'
row2 = '4 | 5 | 6'
row3 = '7 | 8 | 9'
print_board()
game_on = True
while game_on:
    user_input = input("What is your move?")
    if user_input == "1" or "2" or "3":
        row1 = row1.replace(user_input, 'x')
    if user_input == "4" or "5" or "6":
        row2 = row2.replace(user_input, 'x')
    if user_input == "7" or "8" or "9":
        row3 = row3.replace(user_input, 'x')
    print_board()
    game_on = check_winner(row1, row2,row3)
    if game_on:
        options.remove(user_input)
        time.sleep(2)
        com = computer_move(options)
        if com == "1" or "2" or "3":
            row1 = row1.replace(com, 'o')
        if com == "4" or "5" or "6":
            row2 = row2.replace(com, 'o')
        if com == "7" or "8" or "9":
            row3 = row3.replace(com, 'o')
        print_board()
        check_winner(row1,row2,row3)
