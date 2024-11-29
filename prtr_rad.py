import numpy as np
import matplotlib.pyplot as plt

# Data for the radar chart
labels = ['New Entrant Threat', 'Competitive Rivalry', 'Buyer Power', 'Supplier Power', 'Threat of Substitute']
values = [3, 3, 2, 4, 4]
num_vars = len(labels)

# Compute the angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Close the plot (circular plot)
values += values[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='skyblue', alpha=0.4)
ax.plot(angles, values, color='blue', linewidth=2)

# Add labels for each axis
ax.set_yticks([1, 2, 3, 4, 5])  # Optional: customize ticks
ax.set_yticklabels(['1', '2', '3', '4', '5'], color="red", size=12)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, color="black", size=14, weight='bold')

# Add title and show the plot
plt.title('Porter\'s Radar', size=16, color='darkblue', weight='bold')
plt.show()
