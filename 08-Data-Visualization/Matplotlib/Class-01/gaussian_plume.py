import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure with custom size & DPI
plt.figure(figsize=(8, 4), dpi=120)   # width=8in, height=4in, 120 pixels/inch

plt.plot(x, y, color="teal", marker="o")
plt.title("Custom Figure Size & DPI")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()