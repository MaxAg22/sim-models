"""module"""
import sys


def rand_multi(a,m,u):
    """mix congruential generator"""
    return (a*u) % m


def get_mul_generator(a,m,u,n):
    """sequence generator"""
    sequence = []
    for _ in range(n):
        u = rand_multi(a,m,u)
        sequence.append(u)

    return sequence


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error: Multiplier a, " \
        "Modulus m " \
        "Seed u and " \
        "Length n are required")
    else:
        params = list(map(int, sys.argv[1:]))
        result = get_mul_generator(*params)
        print(result)
