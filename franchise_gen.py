# TODO: THIS IS THE BEST WAY TO DO THIS IN MADDEN 12
# generates prospects in PLAY table from franchise file
import random
from random_name_gen import NameGen
from random_attributes import gen_attributes

csv_in = open('USR-DATA - PLAY.csv', 'r')
csv_out = open('PLAY-UPDATED.csv', 'w')
guide_out = open('GUIDE.csv', 'w')
idk123 = csv_in.readline()
print(idk123)
csv_out.write(idk123)

colleges = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 33,
            34, 36, 37, 38, 39, 41, 42, 43, 44, 45, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 63, 64, 65, 66, 67,
            68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 90, 91, 92, 93, 94, 95, 96, 97, 98,
            99, 100, 102, 104, 105, 106, 107, 109, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124,
            125, 126, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139, 140, 142, 143, 144, 145, 146, 147, 148, 149,
            150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170,
            171, 172, 173, 174, 176, 177, 178, 179, 180, 181, 183, 184, 185, 186, 187, 189, 190, 193, 194, 195, 196,
            201, 205, 206, 207, 208, 209, 210, 211, 212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226,
            227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 241, 242, 243, 245, 246, 247, 248, 250,
            251, 252, 253, 254, 255, 257, 258, 259, 260, 261, 263, 266, 269, 270, 271, 272, 273, 274, 277, 278, 282,
            283, 286, 287, 288, 289, 290, 292, 294, 295, 297, 302, 303, 306, 307, 308, 309, 310, 311, 312, 315, 317,
            318, 319, 320, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 334, 335, 337, 338, 339, 340, 343, 344,
            346, 347, 348, 349, 350, 351, 352, 353, 354]

attributes = ['SPD', 'AGI', 'ACC', 'AWR', 'STR', 'CAR', 'JMP', 'THP', 'TAS', 'TAM', 'TAD', 'THA', 'TOR', 'PAC', 'BCV',
              'ELU', 'JKM', 'SPM', 'SFA', 'TRK', 'CTH', 'SPC', 'CIT', 'RLS', 'RTE', 'TAK', 'POW', 'BSH', 'FNM', 'PMV',
              'PRC', 'PUR', 'MCV', 'ZCV', 'PRS', 'KAC', 'KPW', 'RET', 'IBL', 'PBK', 'PBS', 'PBF', 'RBK', 'RBS', 'RBF']


def get_overall(att, p):
    ovr = 0
    if p == 0:
        # QB
        ovr = int((att[3] / 3) + (att[7] / 3) +
                  (att[8] / 4) + (att[9] / 4) +
                  (att[10] / 6.75) + (att[13] / 7) +
                  (att[0] / 14) + (att[12] / 24) +
                  (att[1] / 24) + (att[2] / 38) - 50.13 + 0.5)
    elif p == 1:
        # HB
        ovr = int((att[0] / 3.75) + (att[3] / 3.75) +
                  (att[5] / 3.75) + (att[14] / 3.75) +
                  (att[1] / 7.5) + (att[2] / 7.5) +
                  (att[19] / 7.5) + (att[15] / 7.5) +
                  (att[17] / 11) + (att[16] / 11) +
                  (att[4] / 24) + (att[20] / 24) +
                  (att[18] / 24) + (att[24] / 24) - 80.95 + 0.5)
    elif p == 2:
        # FB
        ovr = int((att[3] / 2.75) + (att[38] / 3) +
                  (att[43] / 4) + (att[5] / 4) +
                  (att[2] / 6) + (att[44] / 6) +
                  (att[40] / 6) + (att[0] / 6) +
                  (att[19] / 6) + (att[4] / 10) +
                  (att[1] / 12) + (att[14] / 12) +
                  (att[18] / 12) + (att[41] / 12) +
                  (att[20] / 12) + (att[15] / 18) - 112 + 0.5)
    elif p == 3:
        # WR
        ovr = int((att[0] / 6.5) + (att[3] / 3.5) +
                  (att[5] / 6.5) + (att[20] / 6.5) +
                  (att[24] / 6.5) + (att[22] / 9) +
                  (att[23] / 9) + (att[2] / 10) +
                  (att[1] / 12) + (att[15] / 14) +
                  (att[21] / 14) + (att[6] / 15) +
                  (att[4] / 35) + (att[14] / 35) +
                  (att[19] / 55) + (att[18] / 55) +
                  (att[17] / 55) + (att[16] / 55) - 52 + 0.5)
    elif p == 4:
        # TE
        ovr = int((att[3] / 4) + (att[24] / 6) +
                  (att[22] / 5) + (att[20] / 5) +
                  (att[0] / 6) + (att[43] / 6) +
                  (att[44] / 6) + (att[4] / 6) +
                  (att[38] / 7) + (att[21] / 10) +
                  (att[1] / 10) + (att[2] / 10) +
                  (att[15] / 20) + (att[23] / 20) +
                  (att[5] / 20) + (att[14] / 20) +
                  (att[19] / 20) + (att[40] / 20) +
                  (att[41] / 20) + (att[6] / 20) +
                  (att[17] / 34) + (att[16] / 34) +
                  (att[18] / 51) - 97 + 0.5)
    elif p == 5:
        # LT
        ovr = int((att[40] / 3.5) + (att[3] / 4) +
                  (att[41] / 4) + (att[4] / 4) +
                  (att[43] / 5) + (att[44] / 7) +
                  (att[38] / 10) + (att[0] / 18) +
                  (att[1] / 18) + (att[2] / 18) - 55 + 0.5)
    elif p == 6:
        # LG
        ovr = int((att[40] / 6) + (att[3] / 3) +
                  (att[41] / 6) + (att[4] / 4) +
                  (att[43] / 4) + (att[44] / 3) +
                  (att[38] / 6) + (att[0] / 16) +
                  (att[1] / 8) + (att[2] / 8) - 76 + 0.5)
    elif p == 7:
        # C
        ovr = int((att[40] / 4) + (att[3] / 3) +
                  (att[41] / 4) + (att[4] / 5) +
                  (att[43] / 4) + (att[44] / 4) +
                  (att[38] / 7) + (att[0] / 14) +
                  (att[1] / 14) + (att[2] / 14) - 74 + 0.5)
    elif p == 8:
        # RG
        ovr = int((att[40] / 6) + (att[3] / 3) +
                  (att[41] / 6) + (att[4] / 4) +
                  (att[43] / 4) + (att[44] / 3) +
                  (att[38] / 6) + (att[0] / 16) +
                  (att[1] / 8) + (att[2] / 8) - 76 + 0.5)
    elif p == 9:
        # RT
        ovr = int((att[40] / 3.5) + (att[3] / 3) +
                  (att[41] / 5) + (att[4] / 4) +
                  (att[43] / 3.5) + (att[44] / 4) +
                  (att[38] / 8) + (att[0] / 16) +
                  (att[1] / 16) + (att[2] / 16) - 74 + 0.5)
    elif p == 10:
        # LE
        ovr = int((att[3] / 3) + (att[29] / 4) +
                  (att[28] / 4) + (att[0] / 5) +
                  (att[2] / 5) + (att[25] / 5) +
                  (att[27] / 5) + (att[30] / 6) +
                  (att[4] / 9) + (att[1] / 9) +
                  (att[31] / 9) + (att[26] / 27) - 87 + 0.5)
    elif p == 11:
        # RE
        ovr = int((att[3] / 4) + (att[29] / 4.5) +
                  (att[28] / 4.5) + (att[0] / 5) +
                  (att[2] / 5) + (att[25] / 6) +
                  (att[27] / 6) + (att[30] / 8) +
                  (att[4] / 9) + (att[1] / 9) +
                  (att[31] / 9) + (att[26] / 29) - 67 + 0.5)
    elif p == 12:
        # DT
        ovr = int((att[3] / 3.75) + (att[29] / 5) +
                  (att[28] / 5) + (att[0] / 10) +
                  (att[2] / 10) + (att[25] / 6) +
                  (att[27] / 5) + (att[30] / 10) +
                  (att[4] / 3) + (att[1] / 40) +
                  (att[31] / 40) - 52.85 + 0.5)
    elif p == 13:
        # LOLB
        ovr = int((att[3] / 3) + (att[25] / 5) +
                  (att[30] / 5) + (att[0] / 7) +
                  (att[29] / 7) + (att[28] / 7) +
                  (att[27] / 10) + (att[4] / 10) +
                  (att[2] / 10) + (att[31] / 10) +
                  (att[33] / 10) + (att[32] / 13) +
                  (att[1] / 20) + (att[26] / 20) +
                  (att[20] / 34) - 65 + 0.5)
    elif p == 14:
        # MLB
        ovr = int((att[3] / 4) + (att[25] / 3) +
                  (att[30] / 4) + (att[0] / 8) +
                  (att[29] / 15) + (att[28] / 15) +
                  (att[27] / 4) + (att[4] / 12) +
                  (att[2] / 12) + (att[31] / 6) +
                  (att[33] / 15) + (att[32] / 25) +
                  (att[1] / 12) + (att[26] / 12) - 80 + 0.5)
    elif p == 15:
        # ROLB
        ovr = int((att[3] / 3) + (att[25] / 5) +
                  (att[30] / 5) + (att[0] / 7) +
                  (att[29] / 7) + (att[28] / 7) +
                  (att[27] / 10) + (att[4] / 10) +
                  (att[2] / 10) + (att[31] / 10) +
                  (att[33] / 10) + (att[32] / 13) +
                  (att[1] / 21) + (att[26] / 21) +
                  (att[20] / 36) - 65 + 0.5)
    elif p == 16:
        # CB
        ovr = int((att[32] / 8.0) + (att[0] / 5.0) +
                  (att[2] / 5.0) + (att[3] / 3.5) +
                  (att[30] / 30.0) + (att[33] / 10.0) +
                  (att[1] / 10.0) + (att[25] / 15.0) +
                  (att[6] / 15.0) + (att[34] / 20.0) +
                  (att[4] / 30.0) - 20.4 + 0.5)
    elif p == 17:
        # FS
        ovr = int((att[3] / 4) + (att[33] / 4) +
                  (att[0] / 6) + (att[25] / 6) +
                  (att[30] / 6) + (att[1] / 10) +
                  (att[2] / 10) + (att[6] / 10) +
                  (att[31] / 10) + (att[32] / 10) +
                  (att[4] / 18) + (att[26] / 21) +
                  (att[20] / 30) - 45 + 0.5)
    elif p == 18:
        # SS
        ovr = int((att[3] / 3) + (att[33] / 4) +
                  (att[0] / 6) + (att[25] / 4) +
                  (att[30] / 4) + (att[1] / 16) +
                  (att[2] / 16) + (att[6] / 16) +
                  (att[31] / 6) + (att[32] / 9) +
                  (att[4] / 9) + (att[26] / 9) +
                  (att[20] / 14) - 72 + 0.5)
    elif p == 19:
        # K
        ovr = int((att[3] / 2) + (att[36] / 2) +
                  (att[35] / 0.8) - 114 + 0.5)
    elif p == 20:
        # P
        ovr = int((att[3] / 1.25) + (att[36] / 1.25) +
                  (att[35] / 1.25) - 127 + 0.5)
    return min(max(ovr, 12), 99)


def gen_colleges(num):
    ret = []
    for xyz in range(num):
        # 75% chance of being in first half
        if random.random() < 0.75:
            ret.append(colleges[random.randint(0, 141)])
        else:
            ret.append(colleges[random.randint(142, 281)])
    return ret


def get_potentials(overalls):
    ret = []
    for ovr in overalls:
        # 90+ OVR
        if ovr == 99:
            ret.append(99)
            continue
        elif ovr >= 90:
            ret.append(random.randint(ovr, 99))
            continue

        # 80-89 OVR
        elif ovr >= 80:
            r = random.random()
            # 10% absolute bust
            if r < 0.1:
                ret.append(ovr)
                continue
            # 70% chance within halfway to 99
            if r < 0.8:
                ret.append(random.randint(ovr + 1, int(ovr + (99 - ovr) / 2)))
                continue
            # 20% chance beyond halfway to 99
            ret.append(random.randint(int(ovr + (99 - ovr) / 2), 99))

        # 70-79 OVR
        elif ovr >= 70:
            r = random.random()
            # 15% absolute bust
            if r < 0.15:
                ret.append(ovr)
                continue
            # 50% chance C potential
            if r < 0.65:
                if ovr == 79:
                    ret.append(79)
                    continue
                ret.append(random.randint(ovr, 79))
                continue
            # 25% B potenial
            if r < 0.9:
                ret.append(random.randint(80, 89))
                continue
            # 10% chance A potential
            ret.append(random.randint(90, 99))

        # 69 and under OVR
        else:
            r = random.random()
            # 20% absolute bust
            if r < 0.2:
                ret.append(ovr)
                continue
            # 45% within 5 points
            elif r < 0.65:
                ret.append(random.randint(ovr + 1, ovr + 5))
                continue
            # 25% 6-10 points
            elif r < 0.9:
                ret.append(random.randint(ovr + 6, ovr + 10))
                continue
            # 10% 11+ points
            ret.append(random.randint(ovr + 11, 99))
    return ret


def get_order(pos, ovr):
    order = pos.copy()
    grade = ovr.copy()
    index = list(range(len(order)))
    xyz = list(zip(grade, order, index))
    xyz2 = sorted(xyz, reverse=True, key=lambda x: x[0])
    grade = list(qwe[0] for qwe in xyz2)
    order = list(qwe[1] for qwe in xyz2)
    index = list(qwe[2] for qwe in xyz2)
    other = []
    # separate FB K P
    while 2 in order:
        ind = order.index(2)
        other.append(index.pop(ind))
        order.pop(ind)
    while 19 in order:
        ind = order.index(19)
        other.append(index.pop(ind))
        order.pop(ind)
    while 20 in order:
        ind = order.index(20)
        other.append(index.pop(ind))
        order.pop(ind)


    # shuffle with moving window while keeping 1/2 in overall order
    shuffle1odds = 0.5
    j = 0
    for k in range(12):
        if k < 11:
            shuffled = []
            for l in range(40):
                r = random.random()
                if r < shuffle1odds:
                    shuffled.append(index[k * 20 + l])
                    index[k * 20 + l] = None
            random.shuffle(shuffled)
            m = 0
            for l in range(40):
                if index[k * 20 + l] is None:
                    index[k * 20 + l] = shuffled[m]
                    m += 1
        else:
            shuffled = []
            for l in range(28):
                r = random.random()
                if r < shuffle1odds:
                    shuffled.append(index[k * 20 + l])
                    index[k * 20 + l] = None
            random.shuffle(shuffled)
            m = 0
            for l in range(28):
                if index[k * 20 + l] is None:
                    index[k * 20 + l] = shuffled[m]
                    m += 1

    # shuffle over whole draft while keeping 1-odds in overall order
    shuffled_w = []
    shuffle2odds = 0.2
    for l1 in range(248):
        r = random.random()
        if r < shuffle2odds:
            shuffled_w.append(index[l1])
            index[l1] = None
    random.shuffle(shuffled_w)
    for l1 in range(248):
        if index[l1] is None:
            index[l1] = shuffled_w.pop(0)

    # insert FB K P randomly
    for oth in other:
        index.insert(random.randint(132, len(index) - 1), oth)

    return index


pi = [list(range(13)), list(range(19)), list(range(3)), list(range(32)), list(range(13)),
                     list(range(11)), list(range(9)), list(range(9)), list(range(9)), list(range(11)),
                     list(range(12)),
                     list(range(12)), list(range(20)), list(range(10)), list(range(12)), list(range(10)),
                     list(range(26)), list(range(10)), list(range(10)), list(range(3)), list(range(3))]


def pos_index_to_init(ord, poss, indxs):
    ret = []
    for xyz in range(257):
        ind = poss.index(ord[xyz])
        ret.append(ind + indxs[xyz])
    return ret


def get_ages(pos_list):
    ret = []
    for pos in pos_list:
        r = random.random()
        if pos == 0 or pos >= 19:
            # 5% chance QB K P is 25-30
            if r < 0.05:
                ret.append(random.randint(25, 30))
            # 5% chance QB K P is 20
            elif r < 0.1:
                ret.append(20)
            # 10% chance QB K P is 24
            elif r < 0.2:
                ret.append(24)
            # equal chances of 21 22 23
            else:
                ret.append(random.randint(21, 23))
        else:
            # 0.1% chance 25-30
            if r < 0.001:
                ret.append(random.randint(25, 30))
            # 9.9% chance 20
            elif r < 0.1:
                ret.append(20)
            # 5% chance 24
            elif r < 0.15:
                ret.append(24)
            # equal chances of 21 22 23
            else:
                ret.append(random.randint(21, 23))
    return ret


while True:
    line = csv_in.readline()
    if line == '':
        # reached EOF
        break

    fields = line.split('\n')[0].split(',')

    # check for non-rookie
    if fields[64] != '1015':
        csv_out.write(line)
        continue
csv_in.seek(0)

# generate 257 rookies
rookies = []

# names
ng = NameGen()
names = ng.gen_names(257)

# colleges
colleges = gen_colleges(257)

# positions and attributes
positions = []
attributes = []
for i in range(13):  #QB
    positions.append(0)
    attributes.append(gen_attributes(0))
for i in range(19):  #HB
    positions.append(1)
    attributes.append(gen_attributes(1))
for i in range(3):  #FB
    positions.append(2)
    attributes.append(gen_attributes(2))
for i in range(32):  #WR
    positions.append(3)
    attributes.append(gen_attributes(3))
for i in range(13):  #TE
    positions.append(4)
    attributes.append(gen_attributes(4))
for i in range(11):  #LT
    positions.append(5)
    attributes.append(gen_attributes(5))
for i in range(9):  #LG
    positions.append(6)
    attributes.append(gen_attributes(6))
for i in range(9):  #C
    positions.append(7)
    attributes.append(gen_attributes(7))
for i in range(9):  #RG
    positions.append(8)
    attributes.append(gen_attributes(8))
for i in range(11):  #RT
    positions.append(9)
    attributes.append(gen_attributes(9))
for i in range(12):  #LE
    positions.append(10)
    attributes.append(gen_attributes(10))
for i in range(12):  #RE
    positions.append(11)
    attributes.append(gen_attributes(11))
for i in range(20):  #DT
    positions.append(12)
    attributes.append(gen_attributes(12))
for i in range(10):  #LOLB
    positions.append(13)
    attributes.append(gen_attributes(13))
for i in range(12):  #MLB
    positions.append(14)
    attributes.append(gen_attributes(14))
for i in range(10):  #ROLB
    positions.append(15)
    attributes.append(gen_attributes(15))
for i in range(26):  #CB
    positions.append(16)
    attributes.append(gen_attributes(16))
for i in range(10):  #FS
    positions.append(17)
    attributes.append(gen_attributes(17))
for i in range(10):  #SS
    positions.append(18)
    attributes.append(gen_attributes(18))
for i in range(3):  #K
    positions.append(19)
    attributes.append(gen_attributes(19))
for i in range(3):  #P
    positions.append(20)
    attributes.append(gen_attributes(20))

# generate ages
ages = get_ages(positions)

# calculate overalls
overalls = []
for i in range(257):
    if attributes[i] != None:
        overalls.append(get_overall(attributes[i], positions[i]))


# generate potentials
potentials = get_potentials(overalls)
for i in range(len(overalls)):
    print(f'{positions[i]} ovr {overalls[i]} pot {potentials[i]}')

# get order of players
indices = get_order(positions, overalls)
print(indices)

# # get random player from each position in order
# positions_indexed = [list(range(13)), list(range(19)), list(range(3)), list(range(32)), list(range(13)),
#                      list(range(11)), list(range(9)), list(range(9)), list(range(9)), list(range(11)), list(range(12)),
#                      list(range(12)), list(range(20)), list(range(10)), list(range(12)), list(range(10)),
#                      list(range(26)), list(range(10)), list(range(10)), list(range(3)), list(range(3))]
# order_indices = []
#
# for i in order:
#     order_indices.append(positions_indexed[i].pop(random.randint(0, len(positions_indexed[i]) - 1)))
# print(order_indices)
#
# # absolute indices
# indices = pos_index_to_init(order, positions, order_indices)
# print('\n\n')
# print(order)
# print(positions)
# print(order_indices)
# print(indices)
# print('\n\n')

# write guide header
guide_out.write('POSITION,ROUND,PICK,NAME,OVERALL,POTENTIAL,HEIGHT,WEIGHT\n')

guide_pos = ['00-QB', '01-HB', '02-FB', '03-WR', '04-TE', '05-LT', '06-LG', '07-C', '08-RG', '09-RT', '10-LE', '11-RE',
             '12-DT', '13-LOLB', '14-MLB', '15-ROLB', '16-CB', '17-FS', '18-SS', '19-K', '20-P']

# write rookies into csv
# print(names)
indx = 0
while indx < 257:
    line = csv_in.readline()
    if line == '':
        # reached EOF
        break
    fields = line.split('\n')[0].split(',')
    # check for non-rookie
    if fields[64] != '1015':
        continue
    i = indx

    # change fields
    fields[32] = names[i][0]
    fields[33] = names[i][1]
    fields[180] = positions[indices[i]]  # pos
    fields[168] = overalls[indices[i]]
    fields[142] = potentials[indices[i]]
    fields[106] = colleges[indices[i]]
    fields[68] = ages[indices[i]]
    if i < 224:
        fields[143] = int(i / 32) + 1
        fields[92] = i % 32 + 1
    else:
        fields[143] = 63
        fields[92] = 511
    # attributes
    att = attributes[indices[i]]
    fields[67] = att[0]
    fields[90] = att[1]
    fields[51] = att[2]
    fields[169] = att[3]
    fields[167] = att[4]
    fields[155] = att[5]
    fields[150] = att[6]
    fields[148] = att[7]
    fields[172] = att[8]
    fields[115] = att[9]
    fields[60] = att[10]
    fields[29] = att[11]
    fields[160] = att[12]
    fields[31] = att[13]
    fields[204] = att[14]
    fields[200] = att[15]
    fields[118] = att[16]
    fields[122] = att[17]
    fields[36] = att[18]
    fields[165] = att[19]
    fields[86] = att[20]
    fields[57] = att[21]
    fields[89] = att[22]
    fields[110] = att[23]
    fields[164] = att[24]
    fields[95] = att[25]
    fields[192] = att[26]
    fields[79] = att[27]
    fields[179] = att[28]
    fields[211] = att[29]
    fields[162] = att[30]
    fields[201] = att[31]
    fields[55] = att[32]
    fields[59] = att[33]
    fields[71] = att[34]
    fields[50] = att[35]
    fields[161] = att[36]
    fields[195] = att[37]
    fields[45] = att[38]
    fields[96] = att[39]
    fields[173] = att[40]
    fields[75] = att[41]
    fields[97] = att[42]
    fields[175] = att[43]
    fields[76] = att[44]
    fields[41] = att[45]
    fields[94] = att[46]
    fields[189] = att[47]
    fields[191] = att[48]
    fields[127] = att[49]

    print(f'pos {positions[indices[i]]} #{att[49]}')

    # write to csv
    str = ""
    for f in fields:
        str += f'{f},'
    str += "\n"
    csv_out.write(str)

    # write to guide
    guide_out.write(f'{guide_pos[positions[indices[i]]]},{int(i / 32) + 1},{i % 32 + 1},{names[i][0]} {names[i][1]},'
                    f'{overalls[indices[i]]},{potentials[indices[i]]},{att[47]},{att[48]+160}\n')

    indx += 1

csv_in.close()
csv_out.close()
guide_out.close()
