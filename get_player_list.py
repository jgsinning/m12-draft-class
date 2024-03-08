# converts NCAA 12 export file to CSV of players with positions and NCAA overalls

# file = open("C:\\Users\\jason\\Desktop\\M12 Draft Class\\USR-DATA", "rb")
file = open("C:\\Users\\jason\\Desktop\\rpcs3\\dev_hdd0\\home\\00000001\\savedata\\BLUS30745-DRAFT-YTREWQ\\USR-DATA", "rb")


def get_pos(num):
    if num == 0:
        return 'QB'
    elif num == 1:
        return 'HB'
    elif num == 2:
        return 'FB'
    elif num == 3:
        return 'WR'
    elif num == 4:
        return 'TE'
    elif num == 5:
        return 'LT'
    elif num == 6:
        return 'LG'
    elif num == 7:
        return 'C'
    elif num == 8:
        return 'RG'
    elif num == 9:
        return 'RT'
    elif num == 10:
        return 'LE'
    elif num == 11:
        return 'RE'
    elif num == 12:
        return 'DT'
    elif num == 13:
        return 'LOLB'
    elif num == 14:
        return 'MLB'
    elif num == 15:
        return 'ROLB'
    elif num == 16:
        return 'CB'
    elif num == 17:
        return 'FS'
    elif num == 18:
        return 'SS'
    elif num == 19:
        return 'K'
    elif num == 20:
        return 'P'
    else:
        return 'ERROR'


csv_header = "00,01,02,COLLEGE,FIRST,LAST,1c,1d,1e,1f,OVR,21,POS,WGT,HGT,STR,AGI,SPD,ACC,AWR,CTH,CAR,THP,THA,KPW,KAC," \
             "BTK,TAK,32,PBK,RBK,35,36,JMP,38,TRK,ELU,BCV,SFA,SPM,JKM,IBK,RBS,RBF,PBS,PBF,PMV,FMV,BSH,PUR,PRC,MCV," \
             "ZCV,4b,SPC,CIT,RTE,POW,PRS,RLS,INJ,STA,54,55,56,57,58,59,5a,5b,5c,5d,5e,5f,60,61,62,63,64,65,66,67," \
             "68,69,6a,6b,6c,6d,6e,6f,70,71,72,73,74,75,76,77\n"


# 1600 players in each class
players = []
counter = 0
while counter < 1600:
    player = []
    for i in range(4):
        player.append(file.read(1))
    for i in range(2):
        player.append(file.read(12))
    for i in range(92):
        player.append(file.read(1))

    players.append(player)

    counter += 1
    if counter % 100 == 0:
        print(counter)

print(players)
file.close()
# file = open("C:\\Users\\jason\\Desktop\\M12 Draft Class\\USR-DATA", "rb")


player_str = ""
player_str += csv_header
for p in players:
    i = 0
    # first 3 unknown
    while i < 3:
        player_str += f"{int.from_bytes(p[i], 'little', signed=False)},"
        i += 1
    # college
    player_str += f"{int.from_bytes(p[i], 'little', signed=False)},"
    i += 1
    # names
    while i < 6:
        player_str += (p[i].strip(b'\x00')).decode('UTF-8') + ','
        i += 1
    # 6 simple/unknown
    while i < 12:
        player_str += f"{int.from_bytes(p[i], 'little', signed=False)},"
        i += 1
    # position
    player_str += get_pos(int.from_bytes(p[i], 'little', signed=False)) + ','
    i += 1
    # do the rest except last
    while i < len(p) - 1:
        player_str += f"{int.from_bytes(p[i], 'little', signed=False)},"
        i += 1
    # do last
    player_str += f"{int.from_bytes(p[i], 'little', signed=False)}\n"


# "C:\\Users\\jason\\Desktop\\rpcs3\\dev_hdd0\\home\\00000001\\savedata\\BLUS30745-DRAFT-YTREWQ\\USR-DATA"
# player_file = open('random_players.csv', 'w')
player_file = open('C:\\Users\\jason\\Desktop\\rpcs3\\dev_hdd0\\home\\00000001\\savedata\\BLUS30745-DRAFT-YTREWQ\\USR-DATA.csv', 'w')
player_file.write(player_str)
player_file.close()


"""
for p in players:
    first = (p[0].strip(b'\x00')).decode('UTF-8')
    last = (p[1].strip(b'\x00')).decode('UTF-8')
    ovr = int.from_bytes(p[2], 'little', signed=False)
    pos = get_pos(int.from_bytes(p[3], 'little', signed=False))
    player_str += f"{ovr},{pos},{first},{last}\n"
"""
