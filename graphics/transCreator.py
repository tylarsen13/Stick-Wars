from PIL import Image

userInput = raw_input("Please enter unit name: ")

img = Image.open(userInput + '.png')
img = img.convert("RGBA")

pixdata = img.load()

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (255, 255, 255, 0)

img.save(userInput + "1.png", "PNG")
img.close()

img1 = Image.open(userInput + '1.png')
img1 = img1.convert("RGBA")

pixdata1 = img1.load()

for y in xrange(img1.size[1]):
    for x in xrange(img1.size[0]):
        if pixdata1[x, y] == (237, 28, 36, 255):
            pixdata1[x, y] = (0, 0, 255, 255)

img1.save(userInput + "2.png", "PNG")
img1.close()

img2 = Image.open(userInput + '1.png')
img2 = img2.convert("RGBA")

pixdata2 = img2.load()

for y in xrange(img2.size[1]):
    for x in xrange(img2.size[0]):
        if pixdata2[x, y] == (237, 28, 36, 255):
            pixdata2[x, y] = (0, 64, 0, 255)

img2.save(userInput + "3.png", "PNG")
img2.close()

img3 = Image.open(userInput + '1.png')
img3 = img3.convert("RGBA")

pixdata3 = img3.load()

for y in xrange(img3.size[1]):
    for x in xrange(img3.size[0]):
        if pixdata3[x, y] == (237, 28, 36, 255):
            pixdata3[x, y] = (255, 242, 0, 255)

img3.save(userInput + "4.png", "PNG")
img3.close()