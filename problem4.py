pal = []

a=1
while a<1000:
        b=1
        while b<1000:
                x= a*b
                if str(x) == str(x)[::-1]:
                        pal.append(x)
                b +=1
        a +=1

print(pal)

big = max(pal)

print(big)
