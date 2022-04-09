def SelectRoad(RoadStr):
    if RoadStr == '十字路口':
        return 0
    elif RoadStr == '丁字路口':
        return 1

def SelectCarPosi(CarPosiStr):
    if(CarPosiStr) == '东':
        return 0
    elif(CarPosiStr) == '西':
        return 1
    elif(CarPosiStr) == '南':
        return 2
    elif(CarPosiStr) == '北':
        return 3

def SelectCarTrack(CarTrackStr):#'从右至左', '从左至右', '从上至下', '从下至上', '从左至右再至上', '从左至右再至下', '从右至左再至上', '从右至左再至下'
    if(CarTrackStr) == '从右至左':
        return 0
    elif(CarTrackStr) == '从左至右':
        return 1
    elif(CarTrackStr) == '从上至下':
        return 2
    elif (CarTrackStr) == '从下至上':
        return 3
    elif (CarTrackStr) == '从左至右再至上':
        return 4
    elif (CarTrackStr) == '从左至右再至下':
        return 5
    elif (CarTrackStr) == '从右至左再至上':
        return 6
    elif (CarTrackStr) == '从右至左再至下':
        return 7

def SelectPedPosition(PedPosiStr):
    if(PedPosiStr) == '东上':
        return 0
    elif(PedPosiStr) == '东下':
        return 1
    elif(PedPosiStr) == '西上':
        return 2
    elif (PedPosiStr) == '西下':
        return 3
    elif (PedPosiStr) == '南左':
        return 4
    elif (PedPosiStr) == '南右':
        return 5
    elif (PedPosiStr) == '北左':
        return 6
    elif (PedPosiStr) == '北右':
        return 7