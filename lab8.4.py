import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
d4 = df[df['scenario'] == '04_CustAgeDist'].copy()
d4['prep_course'] = pd.to_numeric(d4['prep_course'])

plt.figure(figsize=(8, 5))
sns.histplot(data=d4, x='prep_course', hue='study_hours', bins=5, kde=True)
plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")
plt.show()