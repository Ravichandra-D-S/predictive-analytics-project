
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load monthly sales data
df = pd.read_csv("output/monthly_sales.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create time-based features
df["Month_Number"] = np.arange(len(df))

month = df["Order Date"].dt.month

df["Month_Sin"] = np.sin(2 * np.pi * month / 12)
df["Month_Cos"] = np.cos(2 * np.pi * month / 12)

# Select input features and target
X = df[["Month_Number", "Month_Sin", "Month_Cos"]]
y = df["Sales"]

# Split data chronologically
X_train = X.iloc[:36]
X_test = X.iloc[36:]

y_train = y.iloc[:36]
y_test = y.iloc[36:]

# Train improved Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate improved model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Display evaluation results
print("\nIMPROVED MODEL - SEASONAL FEATURES")
print("----------------------------------")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 3))

# Save improved predictions
results = pd.DataFrame({
    "Date": df["Order Date"].iloc[36:],
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred
})

results.to_csv(
    "output/seasonal_prediction_results.csv",
    index=False
)

# Compare with the original baseline model
baseline = pd.read_csv("output/prediction_results.csv")

baseline_mae = mean_absolute_error(
    baseline["Actual Sales"],
    baseline["Predicted Sales"]
)

baseline_rmse = np.sqrt(mean_squared_error(
    baseline["Actual Sales"],
    baseline["Predicted Sales"]
))

baseline_r2 = r2_score(
    baseline["Actual Sales"],
    baseline["Predicted Sales"]
)

comparison = pd.DataFrame({
    "Model": ["Baseline Model", "Seasonal Model"],
    "MAE": [baseline_mae, mae],
    "RMSE": [baseline_rmse, rmse],
    "R2 Score": [baseline_r2, r2]
})

print("\nMODEL COMPARISON")
print("----------------")
print(comparison.round(3))

comparison.to_csv(
    "output/model_comparison.csv",
    index=False
)

print("\nImproved predictions and model comparison saved successfully!")
