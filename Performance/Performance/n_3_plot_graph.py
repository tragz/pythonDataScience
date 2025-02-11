import numpy as np
import matplotlib.pyplot as plt

# Generate Input Values
n = np.linspace(0, 10, 100)
y = n**3

# plot the graph
plt.figure(figsize=(8, 5))
plt.plot(n, y, label=r'$O(n^3)$', color='b', linewidth=2)
plt.xlabel("Input size (n)")
plt.ylabel("Operations")
plt.title("O(n3) Growth")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
