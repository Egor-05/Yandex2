size = 16
print(f'{" " * 6}    {" ".join("{:02x}".format(i) for i in range(size))}\n')
with open('data.txt', 'rb') as f:
    counter = 0
    while True:
        data = f.read(size)
        if not data:
            break
        print('{:06x}    {:52}{}'.format(counter, ' '.join('{:02x}'.format(i) for i in data),
              ''.join(chr(i) if chr(i).isprintable() else '.' for i in data)))
        counter += size