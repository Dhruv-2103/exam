import matplotlib.pyplot as plt

# DB 1
x1 = [10, 20, 30, 40, 50]
y1 = [11, 21, 31, 41, 51]

# DB 2
x2 = [25, 32, 45, 55, 61]
y2 = [14, 16, 28, 33, 54]

plt.scatter(x1, y1, c="pink",marker="s")
plt.scatter(x2, y2, c="gray",marker="^")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
