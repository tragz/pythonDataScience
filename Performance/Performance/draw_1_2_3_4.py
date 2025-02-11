# Generate input values
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, 100)

# Compute different complexities
y1 = n        # O(n)
y2 = n**2     # O(n^2)
y3 = n**3     # O(n^3)
y4 = n**4     # O(n^4)

# Plot the graphs
plt.figure(figsize=(8, 5))
plt.plot(n, y1, label=r'$O(n)$', color='g', linewidth=2)
plt.plot(n, y2, label=r'$O(n^2)$', color='r', linewidth=2)
#plt.plot(n, y3, label=r'$O(n^3)$', color='b', linewidth=2)
#plt.plot(n, y4, label=r'$O(n^4)$', color='purple', linewidth=2)

# Labels and legend
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.title('Growth of Different Complexity Functions')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
