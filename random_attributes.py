import random


def get_0():
    att = []
    # scrambler / balanced / pocket
    r = random.random()
    trait = 0
    if r < (1/3):
        trait = 2
    elif r < (2/3):
        trait = 1

    att.append(random.randint(15 * trait + 50, 14 * trait + 71))
    att.append(random.randint(15 * trait + 50, 14 * trait + 71))
    att.append(random.randint(15 * trait + 50, 14 * trait + 71))
    att.append(random.randint(40, 85))
    att.append(random.randint(50, 75))
    if trait == 2:
        att.append(random.randint(70, 99))
    else:
        att.append(random.randint(50, 85))
    att.append(random.randint(15 * trait + 50, 14 * trait + 71))
    r = random.random()
    tas, tam, tad = 0, 0, 0
    # good gunslinger (THP DAC)
    if r < 0.2:
        att.append(random.randint(90, 99))
        tas = random.randint(60, 90)
        tam = random.randint(60, 90)
        tad = random.randint(70, 95)
    # project (THP)
    elif r < 0.5:
        att.append(random.randint(90, 99))
        tas = random.randint(60, 85)
        tam = random.randint(60, 85)
        tad = random.randint(55, 85)
    # good game manager (SAC MAC)
    elif r < 0.7:
        att.append(random.randint(75, 89))
        tas = random.randint(70, 95)
        tam = random.randint(70, 95)
        tad = random.randint(55, 85)
    # not good
    else:
        att.append(random.randint(70, 89))
        tas = random.randint(60, 85)
        tam = random.randint(60, 85)
        tad = random.randint(50, 85)
    att.append(tas)
    att.append(tam)
    att.append(tad)
    att.append(int((tas + tam + tad) / 3))
    if trait == 2:
        att.append(random.randint(60, 99))
    else:
        att.append(random.randint(50, 80))
    att.append(random.randint(60, 99))
    if trait == 2:
        for i in range(6):
            att.append(random.randint(60, 99))
    else:
        for i in range(6):
            att.append(random.randint(50, 80))
    #CTH
    for i in range(25):
        att.append(random.randint(20, 50))
    #STA
    att.append(random.randint(70, 99))
    att.append(random.randint(70, 99))
    if trait == 2:
        att.append(random.randint(69, 75))
    else:
        att.append(random.randint(71, 80))
    att.append(random.randint(40, 90))
    att.append(random.randint(1, 19))
    return att


def get_1():
    att = []
    # power / balanced / elusive
    r = random.random()
    trait = 0
    if r < (1/3):
        trait = 2
    elif r < (2/3):
        trait = 1

    att.append(random.randint(4 * trait + 81, 5 * trait + 89))
    att.append(random.randint(4 * trait + 81, 5 * trait + 89))
    att.append(random.randint(4 * trait + 81, 5 * trait + 89))
    att.append(random.randint(40, 85))
    if trait == 0:
        att.append(random.randint(70, 85))
    else:
        att.append(random.randint(50, 75))
    att.append(random.randint(60, 99))
    att.append(random.randint(70, 99))
    # THP
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(60, 99))
    if trait == 2:
        for i in range(3):
            att.append(random.randint(75, 99))
    else:
        for i in range(3):
            att.append(random.randint(65, 99))
    if trait == 0:
        for i in range(2):
            att.append(random.randint(75, 99))
    else:
        for i in range(2):
            att.append(random.randint(65, 99))
    for i in range(5):
        att.append(random.randint(55, 85))
    # TAK
    for i in range(12):
        att.append(random.randint(20, 50))
    att.append(random.randint(40, 99))
    att.append(random.randint(20, 50))
    for i in range(3):
        att.append(random.randint(35, 75))
    for i in range(3):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(70, 99))
    att.append(random.randint(66, 76))
    if trait == 0:
        att.append(random.randint(40, 80))
    else:
        att.append(random.randint(20, 80))
    r = random.random()
    if r < 0.3:
        att.append(random.randint(1, 9))
    elif r < 0.7:
        att.append(random.randint(20, 29))
    elif r < 0.9:
        att.append(random.randint(40, 49))
    else:
        att.append(random.randint(30, 39))
    return att


def get_2():
    att = []
    for i in range(3):
        att.append(random.randint(70, 89))
    att.append(random.randint(40, 85))
    att.append(random.randint(60, 89))
    att.append(random.randint(60, 99))
    att.append(random.randint(70, 89))
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(60, 89))
    att.append(random.randint(40, 79))
    att.append(random.randint(40, 79))
    att.append(random.randint(40, 79))
    att.append(random.randint(60, 89))
    att.append(random.randint(60, 89))
    att.append(random.randint(60, 89))
    att.append(random.randint(40, 79))
    att.append(random.randint(40, 79))
    att.append(random.randint(40, 79))
    att.append(random.randint(40, 79))
    for i in range(13):
        att.append(random.randint(20, 50))
    att.append(random.randint(60, 99))
    att.append(random.randint(50, 69))
    att.append(random.randint(50, 69))
    att.append(random.randint(50, 69))
    att.append(random.randint(60, 79))
    att.append(random.randint(60, 79))
    att.append(random.randint(60, 79))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(71, 78))
    att.append(random.randint(60, 120))
    att.append(random.randint(30, 49))
    return att


def get_3():
    att = []
    for i in range(3):
        att.append(random.randint(83, 99))
    att.append(random.randint(40, 85))
    att.append(random.randint(40, 70))
    att.append(random.randint(40, 70))
    att.append(random.randint(83, 99))
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(50, 99))
    att.append(random.randint(50, 99))
    for i in range(9):
        att.append(random.randint(60, 99))
    for i in range(12):
        att.append(random.randint(20, 50))
    att.append(random.randint(40, 99))
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 90))
    att.append(random.randint(60, 90))
    att.append(random.randint(68, 79))
    att.append(random.randint(10, 79))
    r = random.random()
    if r < 0.6:
        att.append(random.randint(1, 19))
    else:
        att.append(random.randint(80, 89))
    return att


def get_4():
    att = []
    for i in range(3):
        att.append(random.randint(70, 95))
    att.append(random.randint(40, 85))
    att.append(random.randint(70, 90))
    att.append(random.randint(40, 70))
    att.append(random.randint(70, 95))
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(50, 75))
    att.append(random.randint(50, 75))
    r = random.random()
    if r < 0.3:
        for i in range(4):
            att.append(random.randint(65, 85))
    else:
        for i in range(4):
            att.append(random.randint(50, 75))
    r = random.random()
    if r < 0.4:
        for i in range(5):
            att.append(random.randint(70, 90))
    else:
        for i in range(5):
            att.append(random.randint(55, 80))
    for i in range(13):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.4:
        for i in range(7):
            att.append(random.randint(60, 85))
    else:
        for i in range(7):
            att.append(random.randint(40, 65))
    att.append(random.randint(70, 90))
    att.append(random.randint(60, 90))
    att.append(random.randint(74, 82))
    att.append(random.randint(60, 130))
    r = random.random()
    if r < 0.3:
        att.append(random.randint(1, 19))
    elif r < 0.45:
        att.append(random.randint(40, 49))
    else:
        att.append(random.randint(80, 89))
    return att



def get_5():
    att = []
    for i in range(3):
        att.append(random.randint(40, 70))
    att.append(random.randint(40, 85))
    att.append(random.randint(75, 99))
    for i in range(33):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.6:
        for i in range(8):
            att.append(random.randint(70, 99))
    else:
        for i in range(8):
            att.append(random.randint(60, 95))
    att.append(random.randint(60, 90))
    att.append(random.randint(75, 82))
    att.append(random.randint(140, 230))
    att.append(random.randint(50, 79))
    return att


def get_6():
    att = []
    for i in range(3):
        att.append(random.randint(40, 70))
    att.append(random.randint(40, 85))
    att.append(random.randint(75, 99))
    for i in range(33):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.6:
        for i in range(8):
            att.append(random.randint(70, 99))
    else:
        for i in range(8):
            att.append(random.randint(60, 95))
    att.append(random.randint(60, 90))
    att.append(random.randint(72, 78))
    att.append(random.randint(120, 200))
    att.append(random.randint(50, 79))
    return att



def get_10():
    att = []
    trait = 0
    r = random.random()
    if r < (1/3):
        trait = 2
    elif r < (2/3):
        trait = 1

    for i in range(3):
        att.append(random.randint(10 * trait + 55, 10 * trait + 72))
    att.append(random.randint(40, 85))
    att.append(random.randint(75, 99))
    att.append(random.randint(20, 50))
    att.append(random.randint(10 * trait + 55, 10 * trait + 72))
    for i in range(18):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.25:
        for i in range(7):
            att.append(random.randint(60, 95))
    else:
        for i in range(7):
            att.append(random.randint(55, 89))
    for i in range(13):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(71, 79))
    if trait == 2:
        att.append(random.randint(80, 120))
    elif trait == 1:
        att.append(random.randint(100, 140))
    else:
        att.append(random.randint(120, 160))
    r = random.random()
    if r < 0.1:
        att.append(random.randint(1, 9))
    elif r < 0.4:
        att.append(random.randint(50, 59))
    elif r < 0.7:
        att.append(random.randint(70, 79))
    else:
        att.append(random.randint(90, 99))
    return att


def get_12():
    att = []
    trait = 0
    r = random.random()
    if r < (1 / 3):
        trait = 2
    elif r < (2 / 3):
        trait = 1

    for i in range(3):
        att.append(random.randint(5 * trait + 55, 5 * trait + 65))
    att.append(random.randint(40, 85))
    att.append(random.randint(75, 99))
    att.append(random.randint(20, 50))
    att.append(random.randint(5 * trait + 55, 5 * trait + 65))
    for i in range(18):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.25:
        for i in range(7):
            att.append(random.randint(60, 95))
    else:
        for i in range(7):
            att.append(random.randint(55, 89))
    for i in range(13):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(71, 79))
    if trait == 2:
        att.append(random.randint(120, 160))
    elif trait == 1:
        att.append(random.randint(140, 180))
    else:
        att.append(random.randint(160, 200))
    r = random.random()
    if r < 0.3:
        att.append(random.randint(50, 59))
    elif r < 0.65:
        att.append(random.randint(70, 79))
    else:
        att.append(random.randint(90, 99))
    return att


def get_13():
    att = []
    trait = 0
    r = random.random()
    if r < (1 / 3):
        trait = 2
    elif r < (2 / 3):
        trait = 1

    for i in range(3):
        att.append(random.randint(5 * trait + 70, 8 * trait + 80))
    att.append(random.randint(40, 85))
    att.append(random.randint(70, 99))
    att.append(random.randint(20, 50))
    att.append(random.randint(5 * trait + 70, 8 * trait + 80))
    for i in range(13):
        att.append(random.randint(20, 50))
    for i in range(5):
        att.append(random.randint(40, 80))
    r = random.random()
    if r < 0.25:
        for i in range(7):
            att.append(random.randint(60, 95))
    else:
        for i in range(7):
            att.append(random.randint(55, 89))
    r = random.random()
    if r < 0.25:
        for i in range(3):
            att.append(random.randint(60, 95))
    else:
        for i in range(3):
            att.append(random.randint(50, 79))
    for i in range(10):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(70, 78))
    if trait == 2:
        att.append(random.randint(55, 90))
    else:
        att.append(random.randint(80, 120))
    r = random.random()
    if r < 0.2:
        att.append(random.randint(1, 9))
    elif r < 0.8:
        att.append(random.randint(40, 59))
    else:
        att.append(random.randint(90, 99))
    return att


def get_14():
    att = []
    trait = 0
    r = random.random()
    if r < (1 / 3):
        trait = 2
    elif r < (2 / 3):
        trait = 1

    for i in range(3):
        att.append(random.randint(5 * trait + 70, 8 * trait + 80))
    att.append(random.randint(40, 85))
    att.append(random.randint(70, 99))
    att.append(random.randint(20, 50))
    att.append(random.randint(5 * trait + 70, 8 * trait + 80))
    for i in range(13):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.3:
        for i in range(5):
            att.append(random.randint(60, 80))
    else:
        for i in range(5):
            att.append(random.randint(40, 70))
    r = random.random()
    if r < 0.5:
        for i in range(7):
            att.append(random.randint(75, 95))
    else:
        for i in range(7):
            att.append(random.randint(55, 89))
    for i in range(3):
        att.append(random.randint(50, 90))
    for i in range(10):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(70, 78))
    if trait == 2:
        att.append(random.randint(60, 90))
    else:
        att.append(random.randint(80, 120))
    if r < 0.2:
        att.append(random.randint(1, 9))
    elif r < 0.8:
        att.append(random.randint(40, 59))
    else:
        att.append(random.randint(90, 99))
    return att


def get_16():
    att = []
    trait = 0
    r = random.random()
    if r < (1 / 3):
        trait = 2
    elif r < (2 / 3):
        trait = 1

    for i in range(3):
        att.append(random.randint(5 * trait + 80, 5 * trait + 89))
    att.append(random.randint(40, 85))
    att.append(random.randint(50, 75))
    att.append(random.randint(50, 80))
    att.append(random.randint(5 * trait + 80, 5 * trait + 89))
    for i in range(7):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.25:
        for i in range(6):
            att.append(random.randint(60, 80))
    else:
        for i in range(6):
            att.append(random.randint(40, 70))
    r = random.random()
    if r < 0.25:
        for i in range(5):
            att.append(random.randint(60, 80))
    else:
        for i in range(5):
            att.append(random.randint(40, 70))
    r = random.random()
    if r < 0.25:
        for i in range(2):
            att.append(random.randint(65, 90))
    else:
        for i in range(2):
            att.append(random.randint(55, 80))
    r = random.random()
    if r < 0.25:
        for i in range(3):
            att.append(random.randint(60, 85))
    else:
        for i in range(3):
            att.append(random.randint(40, 70))
    r = random.random()
    if r < 0.25:
        for i in range(2):
            att.append(random.randint(65, 90))
    else:
        for i in range(2):
            att.append(random.randint(50, 80))
    r = random.random()
    if r < 0.2:
        for i in range(3):
            att.append(random.randint(65, 95))
    else:
        for i in range(3):
            att.append(random.randint(55, 85))
    for i in range(2):
        att.append(random.randint(20, 50))
    att.append(random.randint(50, 99))
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(68, 78))
    att.append(random.randint(10, 80))
    r = random.random()
    if r < 0.2:
        att.append(random.randint(1, 9))
    elif r < 0.6:
        att.append(random.randint(20, 29))
    elif r < 0.8:
        att.append(random.randint(40, 49))
    else:
        att.append(random.randint(30, 39))
    return att


def get_17():
    att = []
    trait = 0
    r = random.random()
    if r < (1 / 3):
        trait = 2
    elif r < (2 / 3):
        trait = 1

    for i in range(3):
        att.append(random.randint(5 * trait + 80, 5 * trait + 89))
    att.append(random.randint(40, 85))
    att.append(random.randint(50, 75))
    att.append(random.randint(50, 80))
    att.append(random.randint(5 * trait + 80, 5 * trait + 89))
    for i in range(7):
        att.append(random.randint(20, 50))
    for i in range(6):
        att.append(random.randint(50, 80))
    for i in range(5):
        att.append(random.randint(40, 80))
    r = random.random()
    if r < 0.25:
        for i in range(2):
            att.append(random.randint(65, 90))
    else:
        for i in range(2):
            att.append(random.randint(50, 80))
    r = random.random()
    if r < 0.25:
        for i in range(3):
            att.append(random.randint(60, 90))
    else:
        for i in range(3):
            att.append(random.randint(45, 75))
    r = random.random()
    if r < 0.25:
        for i in range(2):
            att.append(random.randint(60, 90))
    else:
        for i in range(2):
            att.append(random.randint(55, 80))
    r = random.random()
    if r < 0.25:
        for i in range(3):
            att.append(random.randint(60, 90))
    else:
        for i in range(3):
            att.append(random.randint(50, 85))
    for i in range(2):
        att.append(random.randint(20, 50))
    att.append(random.randint(50, 99))
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(70, 78))
    att.append(random.randint(20, 80))
    r = random.random()
    if r < 0.2:
        att.append(random.randint(1, 9))
    elif r < 0.6:
        att.append(random.randint(20, 29))
    elif r < 0.8:
        att.append(random.randint(40, 49))
    else:
        att.append(random.randint(30, 39))
    return att


def get_18():
    att = []
    trait = 0
    r = random.random()
    if r < (1 / 3):
        trait = 2
    elif r < (2 / 3):
        trait = 1

    for i in range(3):
        att.append(random.randint(5 * trait + 80, 5 * trait + 89))
    att.append(random.randint(40, 85))
    att.append(random.randint(50, 75))
    att.append(random.randint(50, 80))
    att.append(random.randint(5 * trait + 80, 5 * trait + 89))
    for i in range(7):
        att.append(random.randint(20, 50))
    r = random.random()
    if r < 0.25:
        for i in range(6):
            att.append(random.randint(60, 80))
    else:
        for i in range(6):
            att.append(random.randint(50, 70))
    r = random.random()
    if r < 0.25:
        for i in range(5):
            att.append(random.randint(60, 80))
    else:
        for i in range(5):
            att.append(random.randint(40, 70))
    r = random.random()
    if r < 0.25:
        for i in range(2):
            att.append(random.randint(65, 90))
    else:
        for i in range(2):
            att.append(random.randint(50, 80))
    r = random.random()
    if r < 0.25:
        for i in range(3):
            att.append(random.randint(65, 90))
    else:
        for i in range(3):
            att.append(random.randint(50, 80))
    r = random.random()
    if r < 0.25:
        for i in range(2):
            att.append(random.randint(65, 90))
    else:
        for i in range(2):
            att.append(random.randint(50, 80))
    r = random.random()
    if r < 0.25:
        for i in range(3):
            att.append(random.randint(65, 90))
    else:
        for i in range(3):
            att.append(random.randint(60, 80))
    for i in range(2):
        att.append(random.randint(20, 50))
    att.append(random.randint(50, 99))
    for i in range(7):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(60, 99))
    att.append(random.randint(70, 78))
    att.append(random.randint(20, 100))
    r = random.random()
    if r < 0.2:
        att.append(random.randint(1, 9))
    elif r < 0.6:
        att.append(random.randint(20, 29))
    elif r < 0.8:
        att.append(random.randint(40, 49))
    else:
        att.append(random.randint(30, 39))
    return att


def get_19():
    att = []
    for i in range(3):
        att.append(random.randint(60, 80))
    att.append(random.randint(60, 85))
    att.append(random.randint(40, 70))
    for i in range(30):
        att.append(random.randint(20, 50))
    # KAC
    att.append(random.randint(70, 99))
    att.append(random.randint(80, 99))
    for i in range(8):
        att.append(random.randint(20, 50))
    att.append(random.randint(70, 99))
    att.append(random.randint(70, 99))
    att.append(random.randint(67, 77))
    att.append(random.randint(1, 90))
    att.append(random.randint(1, 19))
    return att


def gen_attributes(pos):
    if pos == 0:
        return get_0()
    elif pos == 1:
        return get_1()
    elif pos == 2:
        return get_2()
    elif pos == 3:
        return get_3()
    elif pos == 4:
        return get_4()
    elif pos == 5:
        return get_5()
    elif pos == 6:
        return get_6()
    elif pos == 7:
        return get_6()
    elif pos == 8:
        return get_6()
    elif pos == 9:
        return get_5()
    elif pos == 10:
        return get_10()
    elif pos == 11:
        return get_10()
    elif pos == 12:
        return get_12()
    elif pos == 13:
        return get_13()
    elif pos == 14:
        return get_14()
    elif pos == 15:
        return get_13()
    elif pos == 16:
        return get_16()
    elif pos == 17:
        return get_17()
    elif pos == 18:
        return get_18()
    elif pos == 19:
        return get_19()
    elif pos == 20:
        return get_19()
    return False
