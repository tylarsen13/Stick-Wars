from PIL import Image

userInput = raw_input("Filename to make transparent: ")
colors = [(255, 0, 0, 255), (0, 0, 255, 255), (0, 64, 0, 255), (255, 242, 0, 255)]
i = 1
for color in colors:
    img = Image.open(userInput + str(i) +'.png')
    img = img.convert("RGBA")

    pixdata = img.load()
    a, b, c, d = color
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y] == color:
                pixdata[x, y] = (a/2, b/2, c/2, 255)

    img.save(userInput + str(i) + "inactive" + ".png", "PNG")
    img.close()
    i += 1
