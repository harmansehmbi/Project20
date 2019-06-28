import matplotlib.pyplot as plt

X = list(range(1,11))

# List  Comprehension

Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print(X)
print(Y1)
print(Y2)
print(Y3)

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.legend() # How we can place a legend on different positions -> Explore

plt.xlabel("X-Axis")
plt.xlabel("Y-Axis")

plt.title("Polynomial Graph")
plt.grid(True)

# To save Graph
plt.savefig("MyGraph")      # saved as MyGraph.png

plt.show()