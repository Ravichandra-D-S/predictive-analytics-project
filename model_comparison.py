
import pandas as pd
import matplotlib.pyplot as plt

# Load model comparison data
df = pd.read_csv("output/model_comparison.csv")

# Create comparison chart
metrics = ["MAE", "RMSE", "R2 Score"]

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

for i, metric in enumerate(metrics):
    axes[i].bar(df["Model"], df[metric])
    axes[i].set_title(metric)
    axes[i].set_ylabel("Score")
    axes[i].tick_params(axis="x", rotation=20)
    axes[i].grid(axis="y", alpha=0.3)

plt.suptitle("Baseline vs Seasonal Model Performance")
plt.tight_layout()

plt.savefig("output/model_comparison.png")
plt.show()

print("Model comparison graph saved successfully!")
