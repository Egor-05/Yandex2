from PIL import Image

im = Image.open("image.bmp")
x, y = im.size

for i in range(4):
    for j in range(4):
        if str(i) + str(j) != '33':
            if i != 4 and j != 4:
                im2 = im.crop((i * (x / 4), j * (y / 4), (i + 1) * (x / 4), (j + 1) * (y / 4)))
                im2.save(f'image{str(j + 1)}{str(i + 1)}.bmp')

