with open('input.bmp', mode='rb') as f1:
    header = f1.read(54)
    res = [255 - val for val in f1.read()]
    with open("res.bmp", mode="wb") as f2:
        f2.write(header)
        f2.write(bytes(res))