import re 
txt = "The game is on"
# x = txt = re.search("^The.*game$", txt)

x = re.findall("e", txt)

print(x)