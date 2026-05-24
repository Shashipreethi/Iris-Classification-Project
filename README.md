# Iris-Classification-Project

## Project Overview
This project uses Machine Learning algorithms to classify iris flower species based on flower measurements.

## Dataset
Iris Classification Dataset

Features:
- sepal_length
- sepal_width
- petal_length
- petal_width

Target:
- species

## Algorithms Used
1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree

## Exploratory Data Analysis
Performed:
- Pairplot
- Heatmap
- Boxplots

## Model Evaluation Metrics
- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-score

## Best Model
KNN achieved the best accuracy.

## Project Structure

Iris-Classification-Project/
                    │
                    ├── data/
                    ├── notebook/
                    ├── models/
                    ├── screenshots/
                    ├── inference.py
                    ├── README.md
                    └── best_iris_model.pkl

## Run Project

Install libraries:

pip install pandas numpy matplotlib seaborn scikit-learn joblib

Run notebook:
jupyter notebook

Run inference:
python inference.py

## Example Prediction

Input:
[5.1, 3.5, 1.4, 0.2]

Output:
setosa

## Author
A.V.Shashi Preethi
