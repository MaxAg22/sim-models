from random import random
from math import log


# genera una v.a normal estándar
def Normal_rechazo(mu, sigma):
    while True:
        y1 = -log(1 - random())
        y2 = -log(1 - random())
        if y2 >= (y1 - 1) ** 2 / 2:
            if random() < 0.5:
                return y1 * sigma + mu
            return -y1 * sigma + mu


def Media_Muestral_X():
    X = Normal_rechazo(0, 1)
    Media = X
    Scuad, n = 0, 1  # Scuad = Sˆ2(1)
    while n <= 100:
        n += 1
        X = Normal_rechazo(0, 1)
        MediaAnt = X
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
    return (Media, Scuad, n)


media, scuad, n = Media_Muestral_X()
print(f"Media muestral: {media}")
print(f"Varianza muestral: {scuad}")
print(f"Cantidad de valores a generar n: {n}")
