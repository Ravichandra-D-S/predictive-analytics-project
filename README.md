\# Sales Forecasting Using Machine Learning



\## Project Overview



This project focuses on predicting monthly sales using historical sales data and machine learning techniques.



The project uses Python and Scikit-learn to build and evaluate sales prediction models. It compares a baseline Linear Regression model with an improved model that includes seasonal features.



The main objective is to understand historical sales patterns, predict future sales values, and evaluate model performance.



\## Objectives



\- Analyze historical sales data.

\- Clean and preprocess the dataset.

\- Convert daily sales records into monthly sales data.

\- Visualize monthly sales trends.

\- Build a Linear Regression model.

\- Improve predictions using seasonal features.

\- Compare model performance using evaluation metrics.



\## Technologies Used



\- Python 3.12

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- VS Code



\## Dataset



\*\*Dataset Name:\*\* Superstore Sales Dataset



\*\*Source:\*\* Kaggle



\[Download Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)



The dataset contains 9,994 sales records and 21 columns, including:



\- Order Date

\- Ship Date

\- Customer Name

\- Product Category

\- Sales

\- Quantity

\- Discount

\- Profit

\- Region



The historical sales data covers January 2014 to December 2017.



\## Project Structure



```text

PredictiveAnalytics/

│

├── data/

│   └── sales\_data.csv

│

├── output/

│   ├── actual\_vs\_predicted.png

│   ├── cleaned\_sales\_data.csv

│   ├── model\_comparison.csv

│   ├── model\_comparison.png

│   ├── monthly\_sales.csv

│   ├── monthly\_sales\_trend.png

│   ├── prediction\_results.csv

│   └── seasonal\_prediction\_results.csv

│

├── venv/

│

├── predictive\_analytics.py

├── model\_comparison.py

└── requirements.txt

```



\## Project Workflow



\### 1. Data Loading and Inspection

Loaded the Superstore dataset using Pandas and inspected its structure, columns, and missing values.



\### 2. Data Cleaning

\- Converted Order Date into datetime format.

\- Checked and removed duplicate records.

\- Sorted records by date.

\- Saved the cleaned dataset.



\### 3. Monthly Sales Aggregation

Grouped sales records into monthly totals to analyze sales trends over time.



\### 4. Data Visualization

Created a monthly sales trend graph to understand historical sales patterns.



\### 5. Baseline Model

Built a Linear Regression model using a time-based feature to predict monthly sales.



\### 6. Improved Seasonal Model

Improved the baseline model by introducing seasonal features to capture recurring monthly patterns.



\### 7. Model Evaluation

Evaluated both models using:

\- Mean Absolute Error (MAE)

\- Root Mean Squared Error (RMSE)

\- R² Score



\### 8. Model Comparison

Compared the baseline and seasonal models using evaluation metrics and visualized their performance.



\## Model Performance



The following results were obtained using 36 training records and 12 testing records.



| Evaluation Metric | Baseline Model | Seasonal Model |

|---|---:|---:|

| MAE | 19,663.55 | 12,956.64 |

| RMSE | 23,664.50 | 17,705.75 |

| R² Score | 0.157 | 0.528 |



\### Results and Analysis



The seasonal model performed better than the baseline model on the test dataset.



\- MAE decreased from 19,663.55 to 12,956.64.

\- RMSE decreased from 23,664.50 to 17,705.75.

\- R² Score improved from 0.157 to 0.528.



This indicates that including seasonal features helped the model capture more variation in historical monthly sales.



\## How to Run the Project



\### Step 1: Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\### Step 2: Open the Project Folder



```bash

cd PredictiveAnalytics

```



\### Step 3: Create a Virtual Environment



```bash

python -m venv venv

```



\### Step 4: Activate the Environment (Windows PowerShell)



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### Step 5: Install Required Libraries



```bash

python -m pip install -r requirements.txt

```



\### Step 6: Run the Predictive Analytics Script



```bash

python predictive\_analytics.py

```



\### Step 7: Generate the Model Comparison Graph



```bash

python model\_comparison.py

```



Generated CSV files and graphs are saved in the `output` folder.



\## Key Learnings



Through this project, I learned:



\- Data loading and preprocessing using Pandas.

\- Working with historical time-series data.

\- Monthly sales aggregation.

\- Data visualization using Matplotlib.

\- Building machine learning models using Scikit-learn.

\- Understanding regression evaluation metrics.

\- Improving model performance using seasonal features.

\- Comparing machine learning models.



\## Conclusion



This project demonstrates how historical sales data can be used to build machine learning models for sales forecasting.



The improved seasonal model achieved better evaluation results than the baseline Linear Regression model on the test dataset.



This project provided practical experience in data analytics, machine learning, data visualization, and model evaluation.



\---



\*\*Project:\*\* Sales Forecasting Using Machine Learning  

\*\*Domain:\*\* Data Analytics and Machine Learning  

\*\*Language:\*\* Python  

\*\*Purpose:\*\* Data Analytics Internship Project

