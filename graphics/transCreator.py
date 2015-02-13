from PIL import Image

img = Image.open('old.png')
img = img.convert("RGBA")

pixdata = img.load()

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (255, 255, 255, 0)

img.save("new.png", "PNG")