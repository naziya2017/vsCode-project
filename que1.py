def prit(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n):
        isPrime[i] = True
    for p in range(2, n + 1):
        if p * p <= n and isPrime[p]:
            for i in range(p * 2, n + 1, p):
                isPrime[i] = False

def superPrimes(n):
    isPrime = [True for _ in range(n + 1)]
    prit(n, isPrime)
    primes = []
    j = 0
    for p in range(2, n + 1):
        if isPrime[p]:
            primes.append(p)
            j += 1  # Increment j when a prime is found
    for k in range(j):
        if isPrime[primes[k]]:
            print(primes[k], end=" ")

n = 241
print("Super-Primes less than or equal to", n, "are:")
superPrimes(n)
