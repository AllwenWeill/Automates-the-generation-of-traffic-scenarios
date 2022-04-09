ArrowAndCar = [[0, 6, 7], [1, 4, 5], [3], [2]]#东、西、南、北(Car)
PedAndCar = [[0, 1], [2, 3], [3, 4], [5, 6]]#东、西、南、北(Car)
PedAndArrow = [[0, 1, 2, 3], [0, 1, 2, 3], [4, 5, 6, 7], [4, 5, 6, 7], [2, 3, 6, 7], [2, 3, 4, 5], [0, 1,6, 7], [0, 1, 4, 5]]#'从右至左', '从左至右', '从上至下', '从下至上', '从左至右再至上', '从左至右再至上', '从左至右再至下', '从右至左再至上', '从右至左再至下'
#该函数仅用来匹配箭头与车的相对位置
def ScreeningArrow(PosiArrow, PosiCar):
    if PosiArrow in ArrowAndCar[PosiCar]:
        return 1
    else:
        return 0
#该函数仅用来匹配行人与车的相对位置
def ScreeningPed(PosiPed, PosiCar, PosiArrow):
    if PosiPed in PedAndArrow[PosiArrow]:
        return 1
    else:
        return 0

