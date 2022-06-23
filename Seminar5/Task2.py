# Вы когда-нибудь играли в игру "Крестики-нолики"?
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

import random


# выводит на экран иснтрукцию для игрока
def show_instruction():
    print(
'''
-------> Игра "Крестики-нолики" <-------

С Вами  будет сражаться компьютер.
Введите цифру от 1 до 9, чтобы сделать свой ход.
Цифры соответсвуют полям игровой доски:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
'''
        )


# отвечает за выбор символа, каким будет играть игрок
def input_player_symbol():
    symbol = ''
    while not (symbol == 'Х' or symbol == 'О'):
        print('Выберете, каким знаком Вы будете играть? (Х или О)')
        symbol = input().upper()
        if symbol == 'Х':
            return ['Х', 'О'] # первым элемент возвращаемого списка - знак игрока.
        else:
            return ['О', 'Х']


# за кем первый ход - рандом
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Игрок'


# отвечает за показ игровой доски
def show_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]) 


# отвечает за ход игрока
def get_player_move(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('Ваш ход (1 - 9):')
        move = input()
    return int(move)


# проверка возможности хода, возвращает True, если ячейка свободна
def is_space_free(board, move):
    return board[move] == ' '
 

# делает копию игровой доски, т.к. в дальнейшем будут вноситься в нее изменения
def get_board_copy(board):
    copy_board = []
    for i in board:
        copy_board.append(i)
    return copy_board


# ход
def make_move(board, symbol, move):
    board[move] = symbol


# учитывает позицию на доске и текущий ход игрока. Возвращает True, если игрок выиграл
def is_winner(board, symbol):
    return ((board[1] == symbol and board[2] == symbol and board[3] == symbol) or # верхняя строка
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or # средняя строка
    (board[7] == symbol and board[8] == symbol and board[9] == symbol) or # нижняя строка
    (board[1] == symbol and board[4] == symbol and board[7] == symbol) or # левая графа
    (board[2] == symbol and board[5] == symbol and board[8] == symbol) or # средняя графа
    (board[3] == symbol and board[6] == symbol and board[9] == symbol) or # правая графа
    (board[1] == symbol and board[5] == symbol and board[9] == symbol) or # диагональ
    (board[3] == symbol and board[5] == symbol and board[7] == symbol)) # диагональ


# возвращает случайный ход из полученного списка возможных ходов
def choose_random_move(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None


# отвечает за ход компьютера - иммитация "думающего" компьютера
def get_computer_move(board_copy, computer_symbol):
    if computer_symbol == 'Х':
        player_symbol = 'О'
    else:
        player_symbol = 'Х'
 
    # it's magic! - алгоритм победы
    # определяет возможность победы на следующем ходу
    for i in range(1, 10):
        copy = get_board_copy(board_copy)
        if is_space_free(copy, i):
            make_move(copy, computer_symbol, i)
            if is_winner(copy, computer_symbol):
                return i
 
    # проверяет, может ли игрок выиграть на следющем ходу, чтобы опередить его
    for i in range(1, 10):
        copy = get_board_copy(board_copy)
        if is_space_free(copy, i):
            make_move(copy, player_symbol, i)
            if is_winner(copy, player_symbol):
                 return i
 
    # занимает один из углов, если он свободен
    move = choose_random_move(board_copy, [1, 3, 7, 9])
    if move != None:
        return move
 
    # занимает центр, если он свободен
    if is_space_free(board_copy, 5):
        return 5
 
    # занимает одну из оставшихся клеток
    return choose_random_move(board_copy, [2, 4, 6, 8])


# проверяет заполненность доски, если пустых клеток не осталось - возвращает True
def check_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


# дает возможность повторить игру
def start_again():
    print('Сыграть еще раз? (да или нет)')
    return input().lower().startswith('д')


show_instruction()

while True:
    # обнуляем доску
    play_board = [' '] * 10
    player_symbol, computer_symbol = input_player_symbol()
    queue = who_goes_first()
    print (f'Первым ходит {queue} \n')
    game_is_playing = True
 
    while game_is_playing:
        if queue == 'Игрок': # ход игрока           
            show_board(play_board)
            move = get_player_move(play_board)
            make_move(play_board, player_symbol, move)
            if is_winner(play_board, player_symbol):
                show_board(play_board)
                print ('Поздравляем, Вы, победили!')
                game_is_playing = False
            else:
                if check_board_full(play_board):
                    show_board(play_board)
                    print('Ничья, победила дружба!')
                    break
                else:
                    queue = 'Компьютер'
 
        else: # ход компьютера          
            move = get_computer_move(play_board, computer_symbol)
            make_move(play_board, computer_symbol, move)
            if is_winner(play_board, computer_symbol):
                show_board(play_board)
                print('Вы проиграли!')
                game_is_playing = False
            else:
                if check_board_full(play_board):
                    show_board(play_board)
                    print('Ничья, победила дружба!')
                    break
                else:
                    queue = 'Игрок'
 
    if not start_again(): # выход
        break