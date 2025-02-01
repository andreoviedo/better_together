import matplotlib.pyplot as plt
import numpy as np

# Data from the results table
models = ['No Controls', 'Basic Controls', 'Random Forest', 'Boosted Trees', 'Logit NN']
estimates = [-0.018161, -0.016652, -0.015743, -0.016000, -0.015981]
lower_ci = [-0.021293, -0.019090, -0.018308, -0.018538, -0.018526]
upper_ci = [-0.015029, -0.014213, -0.013179, -0.013463, -0.013436]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot estimates and confidence intervals
y_positions = np.arange(len(models))
ax.scatter(estimates, y_positions, color='darkblue', s=100, zorder=3)

# Plot confidence intervals
for i in range(len(models)):
    ax.hlines(y=y_positions[i], xmin=lower_ci[i], xmax=upper_ci[i], 
              color='darkblue', alpha=0.5, linewidth=2, zorder=2)

# Customize the plot
ax.set_yticks(y_positions)
ax.set_yticklabels(models)
ax.grid(True, axis='x', linestyle='--', alpha=0.7, zorder=1)

# Add a vertical line at x=0
ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5, zorder=1)

# Labels and title
ax.set_xlabel('Estimate with 95% Confidence Interval')
ax.set_title('Effect of Multiple Borrowers on Default Risk\nAcross Different Models')

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('estimates_plot.png', dpi=300, bbox_inches='tight')