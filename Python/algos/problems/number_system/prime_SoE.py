# number of prime numbers using Sieve of Eratosthenes
import math


def sieve(n):
    array_of_primes = [False] * (n + 1)
    range_end = int(math.sqrt(n))

    for i in range(2, range_end + 1):
        if not array_of_primes[i]:
            j = i * 2
            while j <= n:
                array_of_primes[j] = True
                j += i

    return print_primes(array_of_primes)


def print_primes(array_of_primes):
    i = 2
    lst = []
    while i < len(array_of_primes):
        print(array_of_primes[i])
        if not array_of_primes[i]:
            lst.append(i)
        i += 1
    print(lst)


sieve(40)
