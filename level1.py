import re
import string

baseIndex = ord('a')

# inputString = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq \
# glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. \
# lmu ynnjw ml rfc spj."""

inputString = "map" #.html

outputString = ""

for char in inputString:
    if re.match("[a-z]", char):
        index = ord(char) - baseIndex
        index = (index + 2) % 26
        outputString += chr(index + baseIndex)
    else:
        outputString += char

print(outputString)

# OR
translateMap = inputString.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[0:2])
print(inputString.translate(translateMap))
