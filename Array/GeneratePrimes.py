def generate_primes(n):
    is_prime = [True]*(n+1)
    primes = []
    for p in range(0, n+1):
        if p == 0 or p == 1:
            is_prime[p] = False
            continue
        if (is_prime[p]):
            primes.append(p)
        for i in range(p, n+1, p):
            is_prime[i] = False
    return primes

print(generate_primes(19))
