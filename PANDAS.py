#
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

#Ex-1
'''iris = sns.load_dataset("iris")
iris.to_csv("iris.csv", index=False)

df = pd.read_csv("iris.csv")

print(df.head())

df.info()

print(df.describe())

print(df.isnull().sum())

df['long_sepal'] = df['sepal_length'] > 5.0
print(df.head())
'''

#Ex-2
#this showes 2 windows
'''
df = sns.load_dataset('titanic')


for col in df.select_dtypes(['category']).columns:
    df[col] = df[col].astype('object')

for col in df.columns:
    if df[col].dtype == 'O':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())


le = LabelEncoder()
for col in ['sex', 'embarked']:
    df[col] = le.fit_transform(df[col])


plt.hist(df['age'], bins=10, color='lightblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

plt.scatter(df['age'], df['fare'], alpha=0.5, color='green')
plt.title('Fare vs Age')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
'''

#Ex-3
 #part of this was sampled from existing projects, but i refined most of it.
 '''
df = sns.load_dataset('iris')

for col in df.columns:
    if df[col].dtype == 'O' or str(df[col].dtype) == 'category':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())

grouped = df.groupby('species').agg({'sepal_length': ['mean', 'max'], 'petal_width': ['sum', 'mean']})
print(grouped, "\n")

pivot = pd.pivot_table(df, values='sepal_width', index='species', columns='petal_width', aggfunc='mean')
print(pivot, "\n")

filtered = df[df['sepal_length'] > 6]
print(filtered[['species', 'sepal_length', 'petal_width']], "\n")

sorted_df = df.sort_values('petal_width', ascending=False)
print(sorted_df[['species', 'sepal_length', 'petal_width']].head(), "\n")

plt.hist(df['sepal_length'], bins=10, color='lightcoral', edgecolor='black')
plt.title('Sepal Length Distribution')
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.show()

plt.scatter(df['sepal_length'], df['petal_width'], alpha=0.6, color='purple')
plt.title('Petal Width vs Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.show()
'''












