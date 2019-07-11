import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("G:/DS/Titanic-Machine-Learning/train.csv")
columns = df.columns
print(df.dtypes)
sns.distplot(df['Parch'])
plt.show()



