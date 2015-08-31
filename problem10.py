a = 1

while a<=997:
    b = 1
    while b<= 1000-a-1:
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print(a,b,c)
            break
        b = b+1
    a= a+1

