from random import randint


def add_coins():
    coins = 0
    while True:
        chance = randint(1, 100)
        coins += 1
        if chance == 1:
            return coins

    return coins


scores = []
for _ in range(100):
    scores.append(add_coins())

print(sum(scores) / len(scores))
