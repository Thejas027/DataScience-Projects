# ===============================
# Student Performance Analysis
# ===============================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: ensures plots open correctly in VS Code
import matplotlib
matplotlib.use('TkAgg')

# 1. Set visualization style
sns.set(style="whitegrid")

# 2. Robust path handling to locate CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "StudentsPerformance.csv")

# 3. Load dataset
df = pd.read_csv(DATA_PATH)

# 4. Initial exploration
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

# 5. Data cleaning
print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# 6. Rename columns for clarity (match CSV exactly)
df.rename(columns={
    'Parental level of education': 'parent_education',
    'test preparation course': 'test_prep'
}, inplace=True)

# 7. Feature engineering
df['total_score'] = df['math score'] + df['reading score'] + df['writing score']
df['average_score'] = df['total_score'] / 3

# 8. Descriptive statistics
print("\nAverage scores by subject:")
print(df[['math score', 'reading score', 'writing score']].mean())

print("\nOverall average score statistics:")
print(df['average_score'].describe())

# 9. Group-wise analysis
print("\nAverage score by gender:")
print(df.groupby('gender')['average_score'].mean())

print("\nAverage score by test preparation:")
print(df.groupby('test_prep')['average_score'].mean())

print("\nAverage score by parental education:")
print(df.groupby('parent_education')['average_score'].mean().sort_values(ascending=False))

# 10. Data visualization

# Histogram of Math Scores
plt.figure()
plt.hist(df['math score'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.show()

# Average Score by Gender
plt.figure()
sns.barplot(x='gender', y='average_score', data=df, palette='pastel')
plt.title("Average Student Performance by Gender")
plt.show()

# Test Preparation vs Performance
plt.figure()
sns.boxplot(x='test_prep', y='average_score', data=df, palette='Set2')
plt.title("Effect of Test Preparation on Performance")
plt.show()

# 11. Insights
print("\nINSIGHTS:")
print("1. Students who completed the test preparation course scored higher on average.")
print("2. Reading scores are generally higher than math scores.")
print("3. Parental education level shows a positive relationship with student performance.")
print("4. Gender-based performance differences are relatively small.")
