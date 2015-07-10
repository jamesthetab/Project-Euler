a=1
b=1
list = [1]

while b <= 4000000:
        list.append(b)
        c=b
        b=a+b
        a=c
print(list)

plist = []

for s in list:
        if not(s%2):
                plist.append(s)
print(plist)

t=0

for p in plist:
        t += p

print(t)
