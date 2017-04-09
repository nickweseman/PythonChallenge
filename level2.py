
frequencyMap = dict()

with open('input/level2') as file:
    data = file.read()

    for char in data:
        currentCount = 0 if frequencyMap.get(char) is None else frequencyMap.get(char)

        frequencyMap[char] = currentCount + 1

for key in frequencyMap.keys():
    print(key, frequencyMap.get(key))
