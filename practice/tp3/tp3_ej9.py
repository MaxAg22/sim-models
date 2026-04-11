"""tp3-ej9"""
from random import randint

def play_game():
    """Returns game points"""
    x = randint(1,6)
    points = 0
    if x in (1,0):
        points = 2 * randint(1,6)
    else:
        points = randint(1,6) + randint(1,6)

    return points

def simulate_games(n_sim):
    """Returns the game wins avg"""
    count = 0
    for _ in range(n_sim):
        points = play_game()
        count += 1 if points > 6 else 0

    return count/n_sim

values = [100, 1000, 10000]
for n in values:
    avg = simulate_games(n)
    print(f"sim length: {n} and avg: {avg}")
