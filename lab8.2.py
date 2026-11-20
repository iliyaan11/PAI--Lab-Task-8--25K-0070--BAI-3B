import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
d2 = df[df['scenario'] == '02_MonthlySales'].copy()

plt.figure(figsize=(8, 5))
for comp, grp in d2.groupby('school_type'):
    plt.plot(grp['study_hours'], grp['exam_score'], marker='o', label=comp)

plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()
plt.show()