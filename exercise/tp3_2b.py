import random

def simulate_game():
    "Simulates the game, return 1 on win"
    u = random.random()
    if u < 0.5:
        x = random.random() + random.random()
    else:
        x = random.random() + random.random()+ random.random()

    return 1 if x >= 1 else 0

def get_probability(n):
    "Simulates n games and return win probability"
    victories = 0
    for _ in range(n):
        victories += simulate_game()
   
    return victories / n

if __name__ == "__main__":
    values = [100, 1000, 10000, 100000, 1000000]
    for n in values:
        result = get_probability(n)
        print(f"Sim length: {n} | probability: {result}")
