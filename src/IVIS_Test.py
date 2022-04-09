from PIL import Image

def PaintIamge(RoadNum, CarPosiNum, CarTrackNum, PedPosiNum):
    RoadFlag = ['./Roadabout.png']
    CarPosiFlag = ['./West_Car.png', './East_Car.png', './South_Car.png', './North_Car.png']
    CarTrackFlag = ['./Left.png','./Right.png','./Down.png','./Up.png','./Left Up.png','./Left Down.png','./Right Up.png','./Right Down.png']
    PedPosiFlag = ['./East.png', './West.png', './North.png', './South.png']
    img_road = Image.open(RoadFlag[RoadNum])
    img_car = Image.open(CarPosiFlag[CarPosiNum])
    img_arrow = Image.open(CarTrackFlag[CarTrackNum])
    if PedPosiNum == 4 or PedPosiNum == 6:
        img_ped = Image.open(PedPosiFlag[0])
    elif PedPosiNum == 5 or PedPosiNum == 7:
        img_ped = Image.open(PedPosiFlag[1])
    elif PedPosiNum == 1 or PedPosiNum == 3:
        img_ped = Image.open(PedPosiFlag[2])
    elif PedPosiNum == 0 or PedPosiNum == 2:
        img_ped = Image.open(PedPosiFlag[3])
    img_road = img_road.convert("RGBA")
    img_ped = img_ped.convert("RGBA")
    img_car = img_car.convert("RGBA")
    img_arrow = img_arrow.convert("RGBA")
    bg = Image.new("RGBA", (600, 600))  #背景(600,600)是大小
    img_road = img_road.resize((600, 600))
    img_ped = img_ped.resize((50, 50))
    if CarTrackNum == 0 or CarTrackNum == 1:
        img_car = img_car.resize((70, 50))
    else:
        img_car = img_car.resize((50, 70))
    if CarTrackNum == 0 or CarTrackNum == 1:
        img_arrow = img_arrow.resize((120, 20))
    elif CarTrackNum in range(4,8):
        img_arrow = img_arrow.resize((120, 120))
    else:
        img_arrow = img_arrow.resize((20, 120))
    Position_Car = [[460,220],[60,300],[320,470],[230,50]]
    Position_Arrow = [[330,240], [160,320], [240,120], [340,340], [160,220], [160,320], [320,140], [320,240]]
    Position_Ped = [[400, 150], [400, 380], [150, 150], [150, 380], [180, 400], [380, 400], [180, 100], [380, 100]]
    bg.paste(img_road, (0, 0), img_road)
    bg.paste(img_car, Position_Car[CarPosiNum], img_car)
    bg.paste(img_arrow, Position_Arrow[CarTrackNum], img_arrow)
    bg.paste(img_ped, Position_Ped[PedPosiNum], img_ped)
    bg.show()


# bg.save("./result/ok.png")