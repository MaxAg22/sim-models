from num_methods.mul_linear_cong_generator import get_mul_generator

a = 2 ** 16 + 3
m = 2 ** 31
c = 0
u = 1

def en_circulo(Nsim, seq):
    en_circ = 0
    for i in range(0, len(seq), 3):
        grupo = seq[i:i+3]
        x,y,z = grupo
        x = x - m/2
        y = y - m/2
        z = z - m/2
        if x ** 2 + y ** 2 + z ** 2 <= m/10 ** 2:
            en_circ += 1
    return en_circ/Nsim


Nsim = int(input("Nsim: ")) * 3
seq = get_mul_generator(a,m,u,Nsim)
print(en_circulo(Nsim, seq))
