import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "Age": np.random.randint(18,60,50),
    "Gender": np.random.choice(["M","F"], 50),
    "Steps": np.random.randint(2000,12000,50),
    "Sleep": np.random.uniform(4,9,50),
    "BMI": np.random.uniform(18,35,50),
    "Workout": np.random.randint(10,120,50)
})

df.fillna(df.mean(numeric_only=True), inplace=True)

print(df.corr()[["Workout","BMI","Sleep"]])

plt.scatter(df['Workout'], df['BMI'])
plt.show()

sns.lineplot(x=df['Sleep'], y=df['Workout'])
plt.show()
