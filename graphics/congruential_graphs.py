"""call this script from root as: python3 -m graphics.congruential_graphs"""
import matplotlib.pyplot as plt
from num_methods.mix_linear_cong_generator import get_mix_generator

a = int(input("Multiplier: "))
c = int(input("Increment: "))
m = int(input("Modulus: "))
u = int(input("Seed: "))
n = int(input("Sequence length: "))

sequence = get_mix_generator(a,c,m,u,n)

x = sequence[:-1]
y = sequence[1:]

plt.scatter(x,y,color='blue')

plt.title('Secuencia aleatoria congruencial linear mixta')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.grid(True)
plt.show()
