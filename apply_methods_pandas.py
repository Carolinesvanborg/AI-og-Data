import pandas as pd
import matplotlib.pyplot as plt

# indlæs datasættet i en DataFrame
df = pd.read_csv("recipeData.csv", encoding='latin-1')
print(df)

# fjern manglende værdier
print(df.info())
print(df.isna().sum())

print(df.shape)
clean_df = df.dropna()  # Drop all rows with null!
print(clean_df.shape)

# plot numeriske variabler i datasættet
print(df.describe()) # Find numeriske værdier
fig = plt.figure()
axis = df["PrimaryTemp"].plot.hist()
plt.show()