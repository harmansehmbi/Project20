import matplotlib.pyplot as plt

scores = {"virat":82, "rohit":140, "rahul":102, "dhavan":118, "dhoni":56}

for i, key in enumerate(scores):
    plt.bar(i, scores[key])

plt.xlabel("BatsMen")
plt.ylabel("Scores")

plt.title("Indian Batting")
plt.show()

