"""module"""


def von_neumann(d):
    """von Neuman generator"""
    d = (d**2 // 100) % 10000
    return d

def get_von_neuman_seq(u,n_sim):
    """generates a von neuman seq"""
    k = 0
    pos = 0
    period = False
    seq = [u]

    for _ in range(n_sim):
        u = von_neumann(u)
        if not period and u in seq:
            pos = seq.index(u)
            k = len(seq) - pos
            period = True
        seq.append(u)

    return (seq, k, pos)


if __name__ == "__main__":
    seed = int(input("4 digits seed: "))
    n = int(input("sequence length: "))
    result = get_von_neuman_seq(seed, n)
    print(f"Sequence: {result[0]} \nK: {result[1]}\nN0: {result[2]}")
