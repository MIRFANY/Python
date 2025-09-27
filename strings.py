#single line string
x = "irfan"

#multiline string

a = """Loren ipsum sit amet,
consectetue adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """

print(a)



#strings are arrays

a = "hello, world!"
print(a[1])

#looping through a string
for x in "banana":
    print(x)


#string length
a = "Hello, World!"
print(len(a))


#check string
txt = "The best things in life are free!"
print("free" in txt)


# using it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("yes, it is present ")

txt = "THe best things in life are free!"
print("best" not in txt)

