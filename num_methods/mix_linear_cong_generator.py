"""module"""
import sys


def rand_mixto(a,c,m,u):
    """mix congruential generator"""
    return (a*u+c) % m


def get_mix_generator(a,c,m,u,n):
    """sequence generator"""
    sequence = []
    for _ in range(n):
        u = rand_mixto(a,c,m,u)
        sequence.append(u)

    return sequence


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Error: Multiplier a, " \
        "Increment c " \
        "Modulus m " \
        "Seed u and " \
        "Length n are required")
    else:
        params = list(map(int, sys.argv[1:]))
        result = get_mix_generator(*params)
        print(result)
