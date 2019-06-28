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

plt.plot(X, Y1, "o")
plt.plot(X, Y2, "^")
plt.plot(X, Y3, "D")

plt.show()