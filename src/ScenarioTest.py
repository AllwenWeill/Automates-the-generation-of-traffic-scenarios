from PIL import Image
img_road = Image.open("./Roadabout.png")
img_ped = Image.open("./East.png")
img_car = Image.open("./East_Car.png")
img_arrow = Image.open("./Right.png")
img_road = img_road.convert("RGBA")
img_ped = img_ped.convert("RGBA")
img_car = img_car.convert("RGBA")
img_arrow = img_arrow.convert("RGBA")
bg = Image.new("RGBA", (600, 600))  #(600,600)是大小
print(img_ped.size)
print(img_road.size)
print(img_car)
print(img_arrow)
img_road = img_road.resize((600, 600))
img_ped = img_ped.resize((50, 50))
img_car = img_car.resize((70, 50))
img_arrow = img_arrow.resize((120, 20))
bg.paste(img_ped, (180, 400), img_ped)
bg.paste(img_road, (0, 0), img_road)
bg.paste(img_car, (60,300), img_car)
bg.paste(img_arrow, (160,320), img_arrow)
bg.show()
count = 0
count = count + 1
print('IVIS自动化生成{}张场景'.format(count))
# bg.save("./result/ok.png")