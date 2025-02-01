import matplotlib.pyplot as plt
import numpy as np

# Data from the results table
models = ['No Controls', 'Basic Controls', 'Random Forest', 'Boosted Trees', 'Logit NN']
rmse_y = [0.166927, 0.165138, 0.169374, 0.162378, 0.169374]
rmse_d = [0.499150, 0.491929, 0.486639, 0.485752, 0.485868]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot RMSE comparison
x = np.arange(len(models))
width = 0.35

rects1 = ax.bar(x - width/2, rmse_y, width, label='RMSE Y', color='skyblue')
rects2 = ax.bar(x + width/2, rmse_d, width, label='RMSE D', color='lightcoral')

ax.set_ylabel('RMSE Value')
ax.set_title('RMSE Comparison Across Models')
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, ha='right')
ax.legend()

# Add value labels on the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.3f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90)

autolabel(rects1)
autolabel(rects2)

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('model_comparison_plots.png', dpi=300, bbox_inches='tight')