import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age": [20,25,30,35,40,45,200],
    "income": [20,25,30,35,100,110,120],
    "bmi": [18,20,22,24,26,28,50]
})

df.fillna(df.mean(), inplace=True)

# Outlier detection
sns.boxplot(df['age']);plt.show()
sns.histplot(df['income']);plt.show()
sns.heatmap(df.corr(), annot=True);plt.show()
