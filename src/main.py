import IVIS_Test
from SelectFun import SelectRoad
from SelectFun import SelectCarPosi
from SelectFun import SelectCarTrack
from SelectFun import SelectPedPosition
from IVIS_Test import PaintIamge
from ScreenFun import ScreeningPed
from ScreenFun import ScreeningArrow
count = 0
RoadList = ['十字路口']
CarPosiList = ['东']
CarTraList = ['从右至左', '从左至右', '从上至下', '从下至上', '从左至右再至上', '从左至右再至下', '从右至左再至上', '从右至左再至下']
PedPosiList = ['东上', '东下', '西上', '西下', '南左', '南右', '北左', '北右']
for RoadType in RoadList:
    for CarPosition in CarPosiList:
        for CarTrack in CarTraList:
            for PedPosition in PedPosiList:
                print("十字路口")
                print("The position of a car: {}".format(CarPosition))
                print("The track of the car: {}".format(CarTrack))
                print("The position of pedestrian: {}".format(PedPosition))

                Flag = [0, 0, 0, 0]  #
                Flag[0] = SelectRoad(RoadType)
                Flag[1] = SelectCarPosi(CarPosition)
                Flag[2] = SelectCarTrack(CarTrack)
                Flag[3] = SelectPedPosition(PedPosition)
                if ScreeningArrow(Flag[2], Flag[1]) == 0:
                    continue
                if ScreeningPed(Flag[3], Flag[1], Flag[2]) == 0:
                    continue
                PaintIamge(Flag[0], Flag[1], Flag[2], Flag[3])
                count = count + 1
print('IVIS自动化生成{}张场景'.format(count))
