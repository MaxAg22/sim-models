"""module"""
def von_neumann(d):
    """von Neuman generator"""
    d = (d**2 // 100) % 10000
    return d

u = int(input("4 digits seed: "))
n = int(input("sequence length: "))
result = []

for _ in range(n):
    u = von_neumann(u)
    result.append(u)

print(result)
