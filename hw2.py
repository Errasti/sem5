from random import randint


def heads_or_tails():
    user_choice = input("Орёл или решка?\n").lower()
    if user_choice != 'орёл' and user_choice != 'решка':
        print("Некорректный ввод, введите значение заново")
        return heads_or_tails()
    winner = ""
    chance = randint(0, 1)
    if chance == 0:
        winner = "решка"
    else:
        winner = "орёл"
    if user_choice == winner:
        return True
    else:
        return False


def game_mode():
    user_mode = int(input("Для одиночной игры введите '0', для игры с другом '1' \n"))
    if user_mode == 1:
        print("Вы выбрали игру с другом")
        return game_vs_friend(user_settings[0], user_settings[1], user_settings[2])
    elif user_mode == 0:
        print("Вы выбрали одиночную игру")
        return game_vs_bot(user_settings[0], user_settings[1], user_settings[2])
    elif user_mode != 0 and user_mode != 1:
        print("Некорректный ввод данных, повторите попытку")
        return game_mode()


def game_settings():
    settings = []
    candy_amount = int(input("Введите общее количество конфет: "))
    max_candy_grab = int(input("Введите максимальное количество конфет за ход: "))
    attempts = int(input("Введите количество попыток хода: "))
    settings = [candy_amount, max_candy_grab, attempts]
    return settings


def game_vs_friend(candy_amount, max_candy_grab, attempts):
    if heads_or_tails():
        print("По итогам жеребьевки первый ход за вами")
        user_turn = 0
    else:
        print("По итогам жеребьевки первый ход за противником")
        user_turn = 1
    while candy_amount > 0:
        user_grab = int(input("Сколько конфет берем? \n"))
        if user_grab > max_candy_grab or user_grab > candy_amount or user_grab == 0:
            print(f'Вы взяли слишком много или слишком мало. Всего:{candy_amount},'
                  f' за ход можно взять:{max_candy_grab} и не меньше "1" конфеты')
            while attempts > 0:
                if max_candy_grab >= user_grab <= candy_amount and user_grab != 0:
                    break
                print(f'Попробуйте еще раз, у вас {attempts} попытки')
                user_grab = int(input("Сколько конфет берем?\n"))
                attempts -= 1
            else:
                return print(f'Попытки кончились. Игра окончена')
        candy_amount -= user_grab
        if candy_amount > 0:
            print(f'Осталось {candy_amount} конфет')
        else:
            print("Конфеты кончились!")
            if user_turn % 2 == 0:
                return print("Вы выйграли!")
            else:
                return print("Победил ваш друг!")
        user_turn += 1


def game_vs_bot(candy_amount, max_candy_grab, attempts):
    if heads_or_tails():
        print("По итогам жеребьевки первый ход за вами")
        user_turn = 0
    else:
        print("По итогам жеребьевки первый ход за противником")
        user_turn = 1
    while candy_amount > 0:
        if user_turn % 2 == 1:
            candy_grab = candy_amount % max_candy_grab + 1
            if candy_grab > candy_amount:
                candy_grab = candy_amount
            elif max_candy_grab > candy_amount:
                candy_grab = candy_amount
            print(f'Компьютер забирает {candy_grab} конфет')
            candy_amount -= candy_grab
            print(f'Осталось {candy_amount} конфет')
            if candy_amount == 0:
                return print("Game over! Победил компьютер!")
        else:
            user_grab = int(input("Сколько конфет берем? \n"))
            if user_grab > max_candy_grab or user_grab > candy_amount or user_grab == 0:
                print(f'Вы взяли слишком много, или слишком мало. Всего:{candy_amount},'
                      f' за ход можно взять:{max_candy_grab} и не меньше "1" конфеты')
                while attempts > 0:
                    if max_candy_grab >= user_grab <= max_candy_grab and user_grab != 0:
                        break
                    print(f'Попробуйте еще раз, у вас {attempts} попытки')
                    user_grab = int(input("Сколько конфет берем?\n"))
                    attempts -= 1
                else:
                    return print(f'Попытки кончились. Игра окончена')
            candy_amount -= user_grab
            if candy_amount > 0:
                print(f'Осталось {candy_amount} конфет')
            else:
                print("Конфеты кончились!")
                if user_turn % 2 == 0:
                    return print("Вы выйграли!")
        user_turn += 1


user_settings = game_settings()
game_mode()

