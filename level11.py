from PIL import Image
from io import BytesIO
import requests

url = r"http://www.pythonchallenge.com/pc/return/cave.jpg"
username = "huge"
password = "file"
data = requests.get(url, auth=(username, password)).content

img = Image.open(BytesIO(data))

evenImage = Image.new("RGB", (img.width // 2, img.height // 2))
oddImage = Image.new("RGB", (img.width // 2, img.height // 2))

evenW = 0
oddW = 0
for w in range(img.width):
    for h in range(img.height):
        if (w + h) % 2 == 0:
            evenImage.putpixel((w // 2, h // 2), img.getpixel((w, h)))
        else:
            oddImage.putpixel((w // 2, h // 2), img.getpixel((w, h)))

evenImage.save("output/even.jpg")
oddImage.save("output/odd.jpg")
