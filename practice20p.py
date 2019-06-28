import matplotlib.pyplot as plt

scores = {"virat":82, "rohit":140, "rahul":102, "dhavan":118, "dhoni":56}

plt.bar(0, scores["virat"])
plt.bar(1, scores["rohit"])
plt.bar(2, scores["rahul"])
plt.bar(3, scores["dhavan"])
plt.bar(4, scores["dhoni"])

plt.show()

