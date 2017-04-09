from PIL import Image
from io import BytesIO
import urllib.request

url = r"http://www.pythonchallenge.com/pc/def/oxygen.png"
data = urllib.request.urlopen(url).read()

img = Image.open(BytesIO(data))

row = [img.getpixel((index, img.height / 2)) for index in range(img.width)]

ords = [r for r, g, b, a in row[::7] if r == g == b]

print("".join(map(chr, ords)))

ords2 = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print("".join(map(chr, ords2)))
