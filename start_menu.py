import os #система
import time #время
import random #рандомные числа
#импорт
def begin(consolSize):
    os.system("mode con cols=170 lines=43")
    ver0 = str('0.1')
    ver1 = "python editon"
    verInfo = str("[ver: " + ver0 + " " + ver1 + "]")
    print('Pocket Stalker'.center(consolSize, '_'))
    print(verInfo.center(consolSize, '░'))
def loading(loadset):
    for i in range(27):
        if loadset == 0:
            r = random.random() * 7
            time.sleep(r/150)
        else:
            time.sleep(loadset/75)
        print('▓', flush = True, end = '')
    time.sleep(0.10)
    print(" ", end = '\r')
def start(consolSize):
    begin(consolSize)
    print(''.center(consolSize - 110), end='')
    print('загрузка: ', end = '')
    loading(0)
    print("добро пожаловать в карманный сталкер! в этой игре вам нужно будет попадать в разные ситуации и не забывать следить за своими жизненными показателями!\nначнём?\n0 - нет\n1 - да")
    # КОНЕЦ НАЧАЛЬНОГО ОКНА И НАЧАЛО ВОПРОСА С ОТВЕТОМ
    ans = -1
    while ans < 0 or ans > 1:
      ans = int(input("ответ: "))
      if ans == 0 or ans == 1:
            break
      else:
            print("м?")
    if ans == 1:
       print('погнали!\n[вы идёте по Чернобыльской пустоши...]')
    else:
        print("как хочешь :Р\nавтозавершение игры:")
        loading(2)
        exit()
