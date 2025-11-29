from scipy.stats import zscore

z = np.abs(zscore(df['age']))
out_z = df['age'][z > 3]

Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
out_iqr = df['age'][(df['age'] < Q1 - 1.5*IQR) | (df['age'] > Q3 + 1.5*IQR)]
