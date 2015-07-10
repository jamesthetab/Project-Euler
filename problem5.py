def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

x=20
mult = 1
i=1

while i<=x:
	temp=mult
	print(prime_factors(i))
	for t in prime_factors(i):
		if temp%t == 0:
			temp = temp/t
		else:
			mult = mult*t
	print(mult)
	i+=1

print(prime_factors(mult))


