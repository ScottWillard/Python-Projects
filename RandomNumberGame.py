import random
import numpy as np
import matplotlib.pyplot as plt


numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def game(x, y):
    for i in range(10000):
        player = random.choice(numList)
        computer = random.choice(numList2)
        if player < computer:
            x += 1
        else:
            y += 1
    print("========SCORE========")
    print("Player:", x, "Computer:", y)
    objects = (x, y)
    y_pos = np.arange(len(objects))
    performance = [x, y]

    plt.bar(y_pos, performance, alpha = 0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Score')
    plt.title("X vs. Y")
    plt.show()


game(x, y)
