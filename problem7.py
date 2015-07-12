def factors(n):
    factors = []
    # remove any factors of 2 first
    while n % 2 == 0:
        factors.append(2)
        n = n/2
    # now look for odd factors
    p = 3
    while n != 1:
        while n % p == 0:
            factors.append(p)
            n = n/p
        p += 2
    return factors
 
def nprime(n):
    prime = 2 # last prime
    count = 1 # number of primes
    num = 3 # next number to check
    while count < n:
        if len(factors(num)) == 1:
            prime = num
            count += 1
        num += 2 # only check odd numbers
    return prime
 
 
print(nprime(10001))
