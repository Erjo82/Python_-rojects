import random
up = '⬆️⬆️⬆️'
down = '⬇️⬇️⬇️'
random_number = random.randrange(1, 101)
difference = 0
counter = 0

print('Измислих си число от 1 до 100')
while True:
    number = input('Предположи число: ')
    if number == 'stop':
        break
    elif number == 'joker':
        print(random_number)
        continue

    guess_number = int(number)
    difference = abs(random_number - guess_number)
    counter += 1
    if guess_number > random_number:  # -------- АКО Е ПО-ГОЛЯМО -------------
        if difference < 6:
            print(f'Горещо, надоло {down}')
        elif difference < 11:
            print(f'Топло, надоло {down}')
        elif difference < 21:
            print(f'Студено, надоло {down}')
        else:
            print(f'Много студено, надоло {down}')

    elif guess_number < random_number:  # ---------- АКО Е ПО-МАЛКО -------------
        if difference < 6:
            print(f'Горещо, нагоре {up}')
        elif difference < 11:
            print(f'Топло, нагоре {up}')
        elif difference < 21:
            print(f'Студено, нагоре {up}')
        else:
            print(f'Много судено, нагоре {up}')

    elif guess_number == random_number:
        print(f'БРАВО, Ти УСПЯ след {counter} опита')
        y_n = input('Ще играeш ли отново y/n :')
        if y_n == 'y' or y_n == 'Y' or y_n == 'yes' or y_n == 'ъ':
            random_number = random.randrange(1, 101)
            difference = 0
            counter = 0
            print('Измислих си число от 1 до 100')
        else:
            break
