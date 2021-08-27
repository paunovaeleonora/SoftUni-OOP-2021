def get_primes(data):
    for n in data:
        if n > 1:
            is_prime = True
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))