from time import sleep
import random as ran
import colorama
from colorama import Fore
import os
import msvcrt as m


colorama.init()

# print('no color', Fore.RED, 'red', '\033[39m', 'bru')

# exit()


x1 = None
x2 = None
x3 = None
x4 = None
x4 = None
x5 = None
x6 = None
x7 = None

rewards = ['apple', 'sticker', 'bannana', 'soda can', 'tree', 'mouse',
           'rabbit', 'cat', 'cable', 'keyboard', 'PC', 'USB cable',
           'person', 'wedding', 'disease', 'woman', 'sister', 'brother', 'dog',
           'oven', 'orphanage', 'bread', 'ball', 'villager', 'bubble bath', 'axolatal',
           'injury', 'cousin', 'conversation', 'pizza', 'product', 'device', 'child',
           'coin', 'penny', 'government', 'salad', 'pizza role', 'map', 'growth', 'speaker',
           'guitar', 'instrument', 'steak', 'vehicle', 'chocolate', 'ladder', 'school']

speed = 1


x1pop = ran.randrange(0, len(rewards))
x1 = rewards[x1pop]
rewards.pop(x1pop)

x2pop = ran.randrange(0, len(rewards))
x2 = rewards[x2pop]
rewards.pop(x2pop)

x3pop = ran.randrange(0, len(rewards))
x3 = rewards[x3pop]
rewards.pop(x3pop)

x4pop = ran.randrange(0, len(rewards))
x4 = rewards[x4pop]
rewards.pop(x4pop)

x5pop = ran.randrange(0, len(rewards))
x5 = rewards[x5pop]
rewards.pop(x5pop)

x6pop = ran.randrange(0, len(rewards))
x6 = rewards[x6pop]
rewards.pop(x6pop)

x7pop = ran.randrange(0, len(rewards))
x7 = rewards[x7pop]
rewards.pop(x7pop)

# print(x1, x2, x3, x4, x5, x6, x7)
# print(rewards)

# exit()

space1 = ' '
space2 = '  '
space3 = '   '
space4 = '    '
space5 = '     '
space6 = '      '
space7 = '       '
space8 = '        '
space9 = '         '
space10 = '         '

count = 0

x1backup = x1
x2backup = x2
x3backup = x3
x4backup = x4
x5backup = x5
x6backup = x6
x7backup = x7

rolls = ran.randrange(28, 31)

distance = 0


frame = True
frameCount = 0

os.system('cls')
sleep(1)

while frame:

    # print(distance)

    # how large is the word
    for i in x1:
        count += 1

    # counter for how long the word is
    if count == 2:
        x1 = x1 + space9

    if count == 3:
        x1 = x1 + space8

    if count == 4:
        x1 = x1 + space7

    if count == 5:
        x1 = x1 + space6

    if count == 6:
        x1 = x1 + space5

    if count == 7:
        x1 = x1 + space4

    if count == 8:
        x1 = x1 + space3

    if count == 9:
        x1 = x1 + space2

    # reset count
    count = 0

    # how long is the word
    for i in x2:
        count += 1

    # counter for how long the word is
    if count == 2:
        x2 = x2 + space9

    if count == 3:
        x2 = x2 + space8

    if count == 4:
        x2 = x2 + space7

    if count == 5:
        x2 = x2 + space6

    if count == 6:
        x2 = x2 + space5

    if count == 7:
        x2 = x2 + space4

    if count == 8:
        x2 = x2 + space3

    if count == 9:
        x2 = x2 + space2

    # reset count
    count = 0

    # how long is the word
    for i in x3:
        count += 1

    # counter for how long the word is
    if count == 2:
        x3 = x3 + space9

    if count == 3:
        x3 = x3 + space8

    if count == 4:
        x3 = x3 + space7

    if count == 5:
        x3 = x3 + space6

    if count == 6:
        x3 = x3 + space5

    if count == 7:
        x3 = x3 + space4

    if count == 8:
        x3 = x3 + space3

    if count == 9:
        x3 = x3 + space2

    # reset count
    count = 0

    # how long is the word
    for i in x4:
        count += 1

    # counter for how long the word is
    if count == 2:
        x4 = x4 + space8

    if count == 3:
        x4 = x4 + space7

    if count == 4:
        x4 = x4 + space6

    if count == 5:
        x4 = x4 + space5

    if count == 6:
        x4 = x4 + space4

    if count == 7:
        x4 = x4 + space3

    if count == 8:
        x4 = x4 + space2

    if count == 9:
        x4 = x4 + space1

    # reset count
    count = 0

    # how long is the word
    for i in x5:
        count += 1

    # counter for how long the word is
    if count == 2:
        x5 = x5 + space9

    if count == 3:
        x5 = x5 + space8

    if count == 4:
        x5 = x5 + space7

    if count == 5:
        x5 = x5 + space6

    if count == 6:
        x5 = x5 + space5

    if count == 7:
        x5 = x5 + space4

    if count == 8:
        x5 = x5 + space3

    if count == 9:
        x5 = x5 + space2

    # reset count
    count = 0

    # how long is the word
    for i in x6:
        count += 1

    # counter for how long the word is
    if count == 2:
        x6 = x6 + space9

    if count == 3:
        x6 = x6 + space8

    if count == 4:
        x6 = x6 + space7

    if count == 5:
        x6 = x6 + space6

    if count == 6:
        x6 = x6 + space5

    if count == 7:
        x6 = x6 + space4

    if count == 8:
        x6 = x6 + space3

    if count == 9:
        x6 = x6 + space2

    # reset count
    count = 0

    # how long is the word
    for i in x7:
        count += 1

    # counter for how long the word is
    if count == 2:
        x7 = x7 + space9

    if count == 3:
        x7 = x7 + space8

    if count == 4:
        x7 = x7 + space7

    if count == 5:
        x7 = x7 + space6

    if count == 6:
        x7 = x7 + space5

    if count == 7:
        x7 = x7 + space4

    if count == 8:
        x7 = x7 + space3

    if count == 9:
        x7 = x7 + space2

    # reset count
    count = 0

    roller = [' |    ', x1, '|\n',
              '|    ', x2, '|\n',
              '|    ', x3, '|\n',
              '|   ', x4,  '| <------\n',
              '|    ', x5, '|\n',
              '|    ', x6, '|\n',
              '|    ', x7, '|\n']

    print(roller[0], roller[1], roller[2], roller[3],
          roller[4], roller[5], roller[6], roller[7],
          roller[8], roller[9], Fore.RED, roller[10], '\033[39m', roller[11],
          roller[12], roller[13], roller[14], roller[15],
          roller[16], roller[17], roller[18], roller[19],
          roller[20])

    if frameCount == 0:
        x1 = x7backup
        x2 = x1backup
        x3 = x2backup
        x4 = x3backup
        x5 = x4backup
        x6 = x5backup
        x7 = x6backup

    if frameCount == 1:
        x1 = x6backup
        x2 = x7backup
        x3 = x1backup
        x4 = x2backup
        x5 = x3backup
        x6 = x4backup
        x7 = x6backup

    if frameCount == 2:
        x1 = x5backup
        x2 = x6backup
        x3 = x7backup
        x4 = x1backup
        x5 = x2backup
        x6 = x3backup
        x7 = x4backup

    if frameCount == 3:
        x1 = x4backup
        x2 = x5backup
        x3 = x6backup
        x4 = x7backup
        x5 = x1backup
        x6 = x2backup
        x7 = x3backup

    if frameCount == 4:
        x1 = x3backup
        x2 = x4backup
        x3 = x5backup
        x4 = x6backup
        x5 = x7backup
        x6 = x1backup
        x7 = x2backup

    if frameCount == 5:
        x1 = x2backup
        x2 = x3backup
        x3 = x4backup
        x4 = x5backup
        x5 = x6backup
        x6 = x7backup
        x7 = x1backup

    if frameCount == 6:
        x1 = x1backup
        x2 = x2backup
        x3 = x3backup
        x4 = x4backup
        x5 = x5backup
        x6 = x6backup
        x7 = x7backup

    if frameCount == 7:
        x1 = x7backup
        x2 = x1backup
        x3 = x2backup
        x4 = x3backup
        x5 = x4backup
        x6 = x5backup
        x7 = x6backup

    if frameCount == 8:
        x1 = x6backup
        x2 = x7backup
        x3 = x1backup
        x4 = x2backup
        x5 = x3backup
        x6 = x4backup
        x7 = x6backup

    if frameCount == 9:
        x1 = x5backup
        x2 = x6backup
        x3 = x7backup
        x4 = x1backup
        x5 = x2backup
        x6 = x3backup
        x7 = x4backup

    if frameCount == 10:
        x1 = x4backup
        x2 = x5backup
        x3 = x6backup
        x4 = x7backup
        x5 = x1backup
        x6 = x2backup
        x7 = x3backup

    if frameCount == 11:
        x1 = x3backup
        x2 = x4backup
        x3 = x5backup
        x4 = x6backup
        x5 = x7backup
        x6 = x1backup
        x7 = x2backup

    if frameCount == 12:
        x1 = x2backup
        x2 = x3backup
        x3 = x4backup
        x4 = x5backup
        x5 = x6backup
        x6 = x7backup
        x7 = x1backup

    if frameCount == 13:
        x1 = x1backup
        x2 = x2backup
        x3 = x3backup
        x4 = x4backup
        x5 = x5backup
        x6 = x6backup
        x7 = x7backup

    if frameCount == 14:
        x1 = x7backup
        x2 = x1backup
        x3 = x2backup
        x4 = x3backup
        x5 = x4backup
        x6 = x5backup
        x7 = x6backup

    if frameCount == 15:
        x1 = x6backup
        x2 = x7backup
        x3 = x1backup
        x4 = x2backup
        x5 = x3backup
        x6 = x4backup
        x7 = x6backup

    if frameCount == 16:
        x1 = x5backup
        x2 = x6backup
        x3 = x7backup
        x4 = x1backup
        x5 = x2backup
        x6 = x3backup
        x7 = x4backup

    if frameCount == 17:
        x1 = x4backup
        x2 = x5backup
        x3 = x6backup
        x4 = x7backup
        x5 = x1backup
        x6 = x2backup
        x7 = x3backup

    if frameCount == 18:
        x1 = x3backup
        x2 = x4backup
        x3 = x5backup
        x4 = x6backup
        x5 = x7backup
        x6 = x1backup
        x7 = x2backup

    if frameCount == 19:
        x1 = x2backup
        x2 = x3backup
        x3 = x4backup
        x4 = x5backup
        x5 = x6backup
        x6 = x7backup
        x7 = x1backup

    if frameCount == 20:
        x1 = x1backup
        x2 = x2backup
        x3 = x3backup
        x4 = x4backup
        x5 = x5backup
        x6 = x6backup
        x7 = x7backup

    if frameCount == 21:
        x1 = x7backup
        x2 = x1backup
        x3 = x2backup
        x4 = x3backup
        x5 = x4backup
        x6 = x5backup
        x7 = x6backup

    if frameCount == 22:
        x1 = x6backup
        x2 = x7backup
        x3 = x1backup
        x4 = x2backup
        x5 = x3backup
        x6 = x4backup
        x7 = x6backup

    if frameCount == 23:
        x1 = x5backup
        x2 = x6backup
        x3 = x7backup
        x4 = x1backup
        x5 = x2backup
        x6 = x3backup
        x7 = x4backup

    if frameCount == 24:
        x1 = x4backup
        x2 = x5backup
        x3 = x6backup
        x4 = x7backup
        x5 = x1backup
        x6 = x2backup
        x7 = x3backup

    if frameCount == 25:
        x1 = x3backup
        x2 = x4backup
        x3 = x5backup
        x4 = x6backup
        x5 = x7backup
        x6 = x1backup
        x7 = x2backup

    if frameCount == 26:
        x1 = x2backup
        x2 = x3backup
        x3 = x4backup
        x4 = x5backup
        x5 = x6backup
        x6 = x7backup
        x7 = x1backup

    if frameCount == 27:
        x1 = x1backup
        x2 = x2backup
        x3 = x3backup
        x4 = x4backup
        x5 = x5backup
        x6 = x6backup
        x7 = x7backup

    if frameCount == 28:
        x1 = x7backup
        x2 = x1backup
        x3 = x2backup
        x4 = x3backup
        x5 = x4backup
        x6 = x5backup
        x7 = x6backup

    if frameCount == 29:
        x1 = x6backup
        x2 = x7backup
        x3 = x1backup
        x4 = x2backup
        x5 = x3backup
        x6 = x4backup
        x7 = x6backup

    if frameCount == 30:
        x1 = x5backup
        x2 = x6backup
        x3 = x7backup
        x4 = x1backup
        x5 = x2backup
        x6 = x3backup
        x7 = x4backup

    frameCount += 1

    if frameCount == rolls:

        sleep(1)

        print('\n\n\n Concragulation!!\n You won a' +
              Fore.CYAN, x5.upper() + '\033[39m' + '!!!')

        print('\n\nPlease press any key to continue...')
        m.getch()

        frame = False

    distance = rolls - frameCount

    if distance >= 6:
        speed = 0.2

    if distance == 5:
        speed = 0.3

    if distance == 5:
        speed = 0.5

    if distance <= 3:
        speed = 1.0

    sleep(speed)
    os.system('cls')

    # frameCount += 1
    # if frameCount == rolls:

    #     print('\n Concragulation!!\n You won -', x4)

    #     print('\n\nPlease press any key to continue...')
    #     m.getch()

    #     frame = False
