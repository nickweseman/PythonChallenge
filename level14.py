from PIL import Image

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

image = Image.open('input/wire.png')
new_image = Image.new('RGB', [100, 100])

x, y, p = -1, 0, 0
d = 200

while d / 2 > 0:
    for v in delta:
        steps = d // 2

        for step in range(steps):
            x, y = x + v[0], y + v[1]
            new_image.putpixel((x, y), image.getpixel((p, 0)))
            p += 1
        d -= 1

new_image.save('output/level14.jpg')
