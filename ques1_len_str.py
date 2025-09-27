#wap to input user's first name and print its length
# fname = input("enter your first name: ")

# print(len(fname))

#wap to find the occurence of '$' in a string

name = "I$r$f$a$n$"
cnt = 0
for i in range (0,len(name)):
    if(name[i]=="$"):
        cnt=cnt +1


print(cnt)


## different method
name = "I$r$f$a$n"
cnt = name.count("$")
print(cnt)