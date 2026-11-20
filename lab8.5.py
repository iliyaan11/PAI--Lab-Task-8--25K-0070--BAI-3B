import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
d5 = df[df['scenario'] == '05_AdVsRevenue'].copy()
d5['study_hours'] = pd.to_numeric(d5['study_hours'])
d5['prep_course'] = pd.to_numeric(d5['prep_course'])

plt.figure(figsize=(8, 5))
sns.regplot(data=d5, x='study_hours', y='prep_course', color='darkgreen', marker='+')
plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()