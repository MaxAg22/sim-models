"""Ej2c-2023"""
import random as rm


def play_game():
    """Simulates a single game returns 1 if A wins, 2 if B wins and 0 if draw"""
    u = rm.random()
    v = rm.random()
    if v < 0.5 < u: # A wins
        return 1
    if u < 0.5 < v: # B wins
        return 2
    return 0


def simulate_game(n_sim):
    """Returns avg when A wins in round 2"""
    a_wins = 0
    for _ in range(n_sim):
        r1 = play_game() # round 1
        if r1 == 1:
            a_wins += 1
        elif r1 == 0: # draw
            r2 = play_game() # round 2
            if r2 == 1:
                a_wins += 1

    return a_wins/n_sim

values = [100, 1000, 10000, 100000, 1000000]
for n in values:
    avg = simulate_game(n)
    print(f"Nsim: {n} and Avg: {avg}")

