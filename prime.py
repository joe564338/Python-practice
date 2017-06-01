import math
def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    root = math.sqrt(n)
    factor = 3
    while factor <= root:
        if n % factor == 0:
            return False
        factor += 2
    return True

def get_primes(n):
    while True:
        if is_prime(n):
            yield n
        n += 1

def sum_primes():
    summation = 0
    for i in get_primes(2):
        summation += i
        if i > 2000000:
            return summation

print(sum_primes())