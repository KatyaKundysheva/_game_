import random
k = random.randint(4, 30)
while k > 1:
    print('в куче', k, 'камней')
    kol = int(input('сколько вы хотите забрать камней? (1, 2 или 3)\n'))
    if kol <= 0 or kol >=4:
        print('вы играете не по правилам')
        exit()
    k -= kol
    print('в куче осталось', k, 'камней')
    if k == 1:
        print('вы победили')
        exit()
    print('теперь ход мой')
    if k == 4:
        kol = 3
    if k == 3:
        kol = 2
    if k == 2:
        kol = 1
    if k > 4:
        kol = random.randint(1, 3)
    k -= kol
    if k == 1:
        print('победа за мной')
        exit()
