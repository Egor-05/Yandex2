from PIL import Image

im = Image.open("image.png")
pixels = im.load()
x, y = im.size
dr = pixels[0, 0]
up, down, left, right = y + 1, 0, x + 1, 0
for i in range(x):
    for j in range(y):
        if pixels[i, j] != dr:
            if j < up:
                up = j
            if j > down:
                down = j
            if i > right:
                right = i
            if i < left:
                left = i
im1 = im.crop((left, up, right + 1, down + 1))
im1.save('res.png')