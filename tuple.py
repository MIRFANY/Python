#add items
#1. convert the tuple into a list and add the thing you want to this created list and then convert it to a tuple
thistuple = ("apple", "banana", "cherry")

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#2. add tuple to a tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
 
print(thistuple)

