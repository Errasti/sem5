def draw_desk(desk):
    print('-------------')
    for i in range(3):
        print(f'|{desk[0+i*3]}|{desk[1+i*3]}|{desk[2+i*3]}|')
    print('-------------')


def player_move(player_token):
    ok = False
    while not ok:
        player_answer = int(input(f'Куда поставим {player_token}: '))
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                ok = True
            else:
                print("Эта клетка занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 :  ")


def check_win(desk):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if desk[each[0]] == desk[each[1]] == desk[each[2]]:
            return desk[each[0]]
    return False


def main(desk):
    count = 0
    win = False
    while not win:
        draw_desk(desk)
        if count % 2 == 0:
            player_move("X")
        else:
            player_move("O")
        count += 1
        if count > 4:
            tmp = check_win(desk)
            if tmp:
                print(f'{tmp} выиграл!')
                win = True
                break
        if count == 9:
            print("Ничья!")
            break
    draw_desk(desk)


board = list(range(1, 10))
main(board)
