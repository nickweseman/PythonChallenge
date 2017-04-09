import re
import urllib.request

url = r"http://www.pythonchallenge.com/pc/def/equality.html"

data = urllib.request.urlopen(url).read().decode()
data = "".join(re.findall(r"<!--(.*)-->", data, re.DOTALL))
data = data.replace('\n', '')

solution = ""

for index, char in enumerate(data):
    if not data[index - 4].isupper() and data[index - 3].isupper() and data[index - 2].isupper() and \
            data[index - 1].isupper() and not data[index].isupper() and data[index + 1].isupper() and \
            data[index + 2].isupper() and data[index + 3].isupper() and not data[index + 4].isupper():
        solution += data[index]

print(solution)

# OR
solution = "".join(re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", data))
print(solution)
