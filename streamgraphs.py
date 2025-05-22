# Streamgraphs using Python
# Library used: matplotlib, numpy
# To install, run in terminal:
# pip install matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np

# Create x values
x = np.linspace(0, 10, 100)

# Create y values
y1 = np.sin(x)
y2 = np.cos(x)

# Plot Streamgraph using stackplot with 'wiggle' baseline
plt.stackplot(x, y1, y2, baseline='wiggle')

# Add title
plt.title('Streamgraph')

# Display the plot
plt.show()
