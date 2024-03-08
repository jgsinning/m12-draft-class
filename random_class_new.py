# converts csv from get_player_list to USR-DATA draft class
import sys
from random import randint
import random
from random_name_gen import NameGen

csv = open('players.csv', 'r')
template = open('USR-DATA-TEMPLATE', 'rb')
outfile = open('USR-DATA', 'wb')

csv_header_1 = "00,01,02,COLLEGE,FIRST,LAST,1c,1d,1e,1f,OVR,21,POS,WGT,HGT,STR,AGI,SPD,ACC,AWR,CTH,CAR,THP,THA,KPW,KAC," \
             "BTK,TAK,32,PBK,RBK,35,36,JMP,38,TRK,ELU,BCV,SFA,SPM,JKM,IBK,RBS,RBF,PBS,PBF,PMV,FMV,BSH,PUR,PRC,MCV," \
             "ZCV,4b,SPC,CIT,RTE,POW,PRS,RLS,INJ,STA,54,55,56,57,58,59,5a,5b,5c,5d,5e,5f,60,61,62,63,64,65,66,67," \
             "68,69,6a,6b,6c,6d,6e,6f,70,71,72,73,74,75,76,77\n"

csv_header_2 = "0,1,2,COLLEGE,FIRST,LAST,1c,1d,1e,1f,OVR,21,POS,WGT,HGT,STR,AGI,SPD,ACC,AWR,CTH,CAR,THP,THA,KPW,KAC," \
             "BTK,TAK,32,PBK,RBK,35,36,JMP,38,TRK,ELU,BCV,SFA,SPM,JKM,IBK,RBS,RBF,PBS,PBF,PMV,FMV,BSH,PUR,PRC,MCV," \
             "ZCV,4b,SPC,CIT,RTE,POW,PRS,RLS,INJ,STA,54,55,56,57,58,59,5a,5b,5c,5d,5e,5f,60,61,62,63,64,65,66,67," \
             "68,69,6a,6b,6c,6d,6e,6f,70,71,72,73,74,75,76,77\n"

# ensure header matches
header_line = csv.readline()
if header_line != csv_header_1 and header_line != csv_header_2:
    print("Error: CSV header formatted incorrectly")
    sys.exit(1)


# gets position from CSV
def get_pos(num):
    if num == 'QB':
        return 0
    elif num == 'HB':
        return 1
    elif num == 'FB':
        return 2
    elif num == 'WR':
        return 3
    elif num == 'TE':
        return 4
    elif num == 'LT':
        return 5
    elif num == 'LG':
        return 6
    elif num == 'C':
        return 7
    elif num == 'RG':
        return 8
    elif num == 'RT':
        return 9
    elif num == 'LE':
        return 10
    elif num == 'RE':
        return 11
    elif num == 'DT':
        return 12
    elif num == 'LOLB':
        return 13
    elif num == 'MLB':
        return 14
    elif num == 'ROLB':
        return 15
    elif num == 'CB':
        return 16
    elif num == 'FS':
        return 17
    elif num == 'SS':
        return 18
    elif num == 'K':
        return 19
    else:
        return 20


# returns a random college uniformly
def get_college():
    c = random.randint(1, 147)
    if c >= 145:
        if c == 145:
            return 211
        elif c == 146:
            return 229
        return 230
    return c


# returns random year and redshirt
def get_age():
    n = random.random()
    if n < 0.01:  # normal class is 0.0025
        return 1, 2
    elif n < 0.4:  # normal class is 0.34
        m = random.random()
        if m < 0.4:
            return 2, 0
        return 2, 2
    m = random.random()
    if m < 0.6:  # normal class is more like 0.42
        return 3, 0
    return 3, 2


# get list of names
name_gen = NameGen()
name_list = name_gen.gen_names(num_names=1600)

# randomly generate player attributes (with names from csv)
i = 0
while i < 1600:
    line = csv.readline().split('\n')[0].split(',')
    # first 3 bytes
    for j in range(4):
        outfile.write(int(line[j]).to_bytes(1, 'little', signed=False))
    # college
    outfile.write(get_college().to_bytes(1, 'little', signed=False))
    # names
    padding_first = 12 - len(name_list[i][0])
    padding_last = 12 - len(name_list[i][1])
    outfile.write(bytes(name_list[i][0], 'utf-8'))
    for j in range(padding_first):
        outfile.write(b'\x00')
    outfile.write(bytes(name_list[i][1], 'utf-8'))
    for j in range(padding_last):
        outfile.write(b'\x00')
    # next 2 are simple
    for j in range(6, 8):
        outfile.write(int(line[j]).to_bytes(1, 'little'))
    # next 2 are year and redshirt
    year, redshirt = get_age()
    outfile.write(year.to_bytes(1, 'little'))
    outfile.write(redshirt.to_bytes(1, 'little'))
    # random overall
    outfile.write(randint(70, 99).to_bytes(1, 'little'))
    # jersey number
    outfile.write(int(line[11]).to_bytes(1, 'little'))
    # handle position label
    position = get_pos(line[12])
    outfile.write(position.to_bytes(1, 'little'))
    # height/weight
    for j in range(13, 15):
        outfile.write(int(line[j]).to_bytes(1, 'little'))
    # 13 random
    for j in range(15, 28):
        outfile.write(randint(40, 99).to_bytes(1, 'little'))
    # 1 idk
    outfile.write(int(line[28]).to_bytes(1, 'little'))
    # 2 random
    for j in range(29, 31):
        outfile.write(randint(40, 99).to_bytes(1, 'little'))
    # 2 idk
    outfile.write(int(line[31]).to_bytes(1, 'little'))
    outfile.write(int(line[32]).to_bytes(1, 'little'))
    # 1 random
    outfile.write(randint(40, 99).to_bytes(1, 'little'))
    # 1 just 0
    outfile.write(b'\x00')
    # 18 random
    for j in range(35, 53):
        outfile.write(randint(40, 99).to_bytes(1, 'little'))
    # 1 idk
    outfile.write(int(line[53]).to_bytes(1, 'little'))
    # 8 random
    for j in range(54, 62):
        outfile.write(randint(40, 99).to_bytes(1, 'little'))
    # the rest take from template
    for j in range(62, len(line)):
        outfile.write(int(line[j]).to_bytes(1, 'little'))
    # iterate
    i += 1

# close the csv
csv.close()

# the first 192,000 bytes of the template are irrelevant
template.read(192000)
# TODO: the remaining 1,536 bytes may or may not be important?
remaining_bytes = template.read(1536)
outfile.write(remaining_bytes)

# close the template
template.close()

# close the output file
outfile.close()
