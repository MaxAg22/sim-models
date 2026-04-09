"""module"""
def von_neumann(d):
    """von Neuman generator"""
    d = (d**2 // 100) % 10000
    return d

u = int(input("4 digits seed: "))
n = int(input("sequence length: "))
k = 0
pos = 0
period = False
result = [u]

for _ in range(n):
    u = von_neumann(u)
    if not period and u in result:
        pos = result.index(u)
        k = len(result) - pos
        period = True

    result.append(u)

print(result)
print(f"period: {k} and n0: {pos}" )
