
with open('input/evil2.gfx', 'rb') as file:
    data = file.read()

    for i in range(5):
        open("output/%d.jpg" % i, 'wb').write(data[i::5])

