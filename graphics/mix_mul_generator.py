"""call this script from root as: python3 -m graphics.congruential_graphs"""
import matplotlib.pyplot as plt
from num_methods.mix_linear_cong_generator import get_mix_generator
from num_methods.mul_linear_cong_generator import get_mul_generator

a = int(input("Multiplier: "))
c = int(input("Increment: "))
m = int(input("Modulus: "))
u = int(input("Seed: "))
n = int(input("Sequence length: "))

sequence = get_mix_generator(a,c,m,u,n)
sequence1 = get_mul_generator(a,m,u,n)

x = sequence[:-1]
y = sequence[1:]
x1 = sequence1[:-1]
y1 = sequence1[1:]

# suma:
z1 = x + y
z2 = x1 + y1

plt.subplot(2,2,1)
plt.scatter(x,y,color='blue')

plt.subplot(2,2,2)
plt.scatter(x1,y1,color='red')

plt.subplot(2,2,3)
plt.scatter(z1,z2,color='orange')

plt.show()
