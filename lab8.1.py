import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
d1 = df[df['scenario'] == '01_StudyVsScore'].copy()
d1['study_hours'] = pd.to_numeric(d1['study_hours'])
d1['prep_course'] = d1['prep_course'].fillna('None')

plt.figure(figsize=(8, 5))
sns.scatterplot(data=d1, x='study_hours', y='exam_score', hue='prep_course', style='prep_course', s=80)
plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()