import matplotlib.pyplot as plt
import numpy as np

# Sample data (ensuring the same length for all lists)
age_groups = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
              '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']
male_population = [6036477, 6790369, 6192022, 5351153, 4897926,
                   4489240, 4409701, 4156091, 3598355, 3054415,
                   2583167, 2145794, 1680418, 1186095, 718051,
                   361254, 129093]
female_population = [5744964, 6485712, 5900267, 5130410, 4687421,
                     4286192, 4245100, 4064313, 3501534, 2946920,
                     2499402, 2156734, 1809600, 1407056, 951160,
                     550063, 229252]

# Convert data to negative values for males
male_population = [-x for x in male_population]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Create the bar charts
ax.barh(age_groups, male_population, color='blue', label='Males')
ax.barh(age_groups, female_population, color='cyan', label='Females')

# Add labels, title, and legend
ax.set_xlabel('Population (in millions)', fontsize=20, fontweight='bold')
ax.set_ylabel('Age Group', fontsize=20, fontweight='bold')
ax.set_title('Population Pyramid', fontsize=20, fontweight='bold')
ax.legend(loc='upper right', fontsize=20)

# Customize ticks for better readability
x_ticks = np.arange(-7000000, 8000000, 1000000)
ax.set_xticks(x_ticks)
ax.set_xticklabels([f"{abs(x)//1000000}M" for x in x_ticks], fontsize=15, fontweight='bold')
ax.set_yticklabels(age_groups, fontsize=15, fontweight='bold')

# Add gridlines for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
