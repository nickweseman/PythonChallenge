import urllib.request
import pickle

url = r"http://www.pythonchallenge.com/pc/def/banner.p"

pickle_data = pickle.load(urllib.request.urlopen(url))

for top_list in pickle_data:
    for bottom_list in top_list:
        char = bottom_list[0]
        frequency = bottom_list[1]

        for i in range(frequency):
            print(char, end='')
    print()

#OR
for top_list in pickle_data:
    print("".join(k * v for k, v in top_list))

