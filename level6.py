import re
import zipfile
import ntpath

zip_ref = zipfile.ZipFile("input/channel.zip", 'r')
zip_ref.extractall("input/channel")
info_list = zip_ref.infolist()
zip_ref.close()

info_map = dict()

for info in info_list:
    info_map[info.filename] = info.comment

file_path = "input/channel/%s.txt"
nothing = "90052"

pattern = re.compile(r"Next nothing is (\d+)")

for index in range(1000):
    filename = file_path % nothing
    with open(filename) as file:
        data = file.read()

    #print(data)
    char = info_map.get(ntpath.basename(filename))

    print(char.decode("utf-8"), end='')

    match = pattern.search(data)
    if match:
        nothing = match.group(1)

