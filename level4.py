import urllib.request
import re

url = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing = "12345"

pattern = re.compile(r"and the next nothing is (\d+)")

for i in range(400):
    data = urllib.request.urlopen(url % nothing).read().decode()
    print(data)

    match = pattern.search(data, re.DOTALL)
    if match:
        nothing = match.group(1)
        continue

    match = re.search(r"Divide by two and keep going", data, re.DOTALL)
    if match:
        nothing = str((int(int(nothing) / 2)))
