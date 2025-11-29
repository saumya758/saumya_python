import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Dataset
df = pd.DataFrame({
    "age": [22,25,30,35,40,45,50,55],
    "bmi": [21,24,27,29,31,28,26,30],
    "steps": [9000,8500,7000,6000,5000,4000,3000,2000]
})

# 1 Histogram
df['bmi'].hist()
plt.show()

# 2 Boxplot
sns.boxplot(df['bmi'])
plt.show()

# 3 Heatmap
sns.heatmap(df.corr(), annot=True)
plt.show()
