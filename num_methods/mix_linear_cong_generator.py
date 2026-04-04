"""module"""
import sys

def rand_mixto(a,c,m,u):
    """mix congruential generator"""
    return (a*u+c) % m

def get_mix_generator():
    """sequence generator"""
    if len(sys.argv) != 6:
        print("Error: Multiplier a, " \
        "Increment c " \
        "Modulus m " \
        "Seed u and " \
        "Length n are required")
        return
    a, c, m, u, n = map(int, sys.argv[1:])

    result = []
    for _ in range(n):
        u = rand_mixto(a,c,m,u)
        result.append(u)

    print(result)

    return result


if __name__ == "__main__":
    get_mix_generator()