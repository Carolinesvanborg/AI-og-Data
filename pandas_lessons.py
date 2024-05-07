# Import Pandas 
import pandas as pd

# Create a basic series instance
series = pd.Series(data=["UK", "France", "Italy"])
print(series)

# Series instance with a name
series = pd.Series(data=["UK", "France", "Italy"], name="country")
print(series)

# Pass my own index to the constructor
series = pd.Series(data=["UK", "France", "Italy"], 
                       index=["a", "b", "c"],
                       name="country")
print(series)

# Data can be used as a dict. 
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"})
print(series)

# Use index with dicts
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"},
                   index=["b", "c", "d", "a"])
print(series)

# Accessing elements in a series with slicing
series = pd.Series(data=["UK", "France", "Italy"])
print(series)
print(series[0])
print(series[1:])

# Access elements by their index labels
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"})
print(series)
print(series["a"])
print(series[["c","b"]])

# If you need a NumPy array representation of your data, you can access it using the series.to_numpy() method. To convert it to a Python list, you can use list(series) or series.tolist()
series = pd.Series(data={"a": "UK", "b": "France", "c": "Italy"})
series_array = series.to_numpy()
print(type(series_array))

print(series_array)

series_list = list(series)  # or series.tolist()
print(type(series_list))

print(series_list)

# How to create a dataframe
data = [["UK", "London"], ["France", "Paris"], ["Italy", "Rome"]]
df = pd.DataFrame(data=data)
print(df)

# pandas automatically labels columns as 0 and 1, and rows as 0, 1, and 2. Like Series, you can customise these.
prefixes = ["+44", "+33", "+39"]
col_names = ["country", "capital"]
df = pd.DataFrame(data=data, index=prefixes, columns=col_names)
print(df)

# Pass in a dict as the data argument. You can have the column names as keys. The values can be a 1D np.array, a list or a Series (a list is used in the example below).
data = {"country": ["UK", "France", "Italy"], 
            "capital": ["London", "Paris", "Rome"]}
prefixes = ["+44", "+33", "+39"]
df = pd.DataFrame(data=data, index=prefixes)
print(df)

# Pass in a list of dict, where each element in the list is a representation of a row (rather than a column).
data = [{"country": "UK", "capital": "London"},
            {"country": "France", "capital": "Paris"},
            {"country": "Italy", "capital": "Rome"}]
prefixes = ["+44", "+33", "+39"]
df = pd.DataFrame(data=data, index=prefixes)
print(df)


# Opret csv-fil med data
data = {
    'code': ['+44', '+33', '+39'],
    'country': ['UK', 'France', 'Italy'],
    'capital': ['London', 'Paris', 'Rome']
}

# Opret en DataFrame
df = pd.DataFrame(data)

# Gem DataFrame til en CSV-fil
df.to_csv('capitals.csv', index=False)

print("CSV-filen er oprettet.")

# pd.read_csv() to load a DataFrame from the file.
df = pd.read_csv("capitals.csv") 
print(df)

#  pd.read_csv() to read the data in as a string.
df = pd.read_csv("capitals.csv", dtype=str) 
print(df)

# If you want code to act as the index, tell pd.read_csv() to use column 0 as the index!
df = pd.read_csv("capitals.csv", index_col=0)
print(df)

# Create a DataFrame instance
df2 = pd.read_csv("Pokemon.csv")
print(df2)

# Examine the dataset
print(df2.index) # 	The index (row labels) of the DataFrame.
print(df2.columns) # The column labels of the DataFrame.
print(df2.dtypes) # Return the dtypes in the DataFrame.
print(df2.info) # Print a concise summary of a DataFrame
print(df2.select_dtypes) #subset of the DataFrame's columns based on the column dtypes.
print(df2.values) # Numpy representation of the DataFrame
print(df2.axes) # A list of the axes in the DataFrame
print(df2.ndim) # Number of axes / array dimentions
print(df2.size) # The number of elements in this object
print(df2.shape) # Dimentionality of the DataFrame
print(df2.memory_usage) # Memory usage of each column in bytes
print(df2.empty) # Check if the Dataframe is empty
print(df2.set_flags) # Returns a new object with updated flags

# Find out how many columns the dataset contains.
print(df2.shape)

# Find out the column names in the dataset. Can you convert this into a Python list?
print(df2.columns)
print(len(df2.columns))
print(type(df2.columns))

column_list = list(df2)  # or list(df.columns) or df.columns.tolist()
print(type(column_list))

# Get the data type for each column (is it a boolean? An integer? A string?) Can you convert this info into a NumPy array?

print(df2.dtypes)
print(type(df2.dtypes))

dtype_array = df2.dtypes.to_numpy() # or df.dtypes.values
print(dtype_array)

# Find out how many rows (instances) there are in this DataFrame.
print(f"number of rows {df2.index}")

# Examine the dataset more
print((df2.head(20))) # Print out the first 20 Pokemons
print((df2.tail(10))) # Print out the last 10 Pokemons
print(df2.info())
print(df2.describe())

# Accessing DataFrame columns
print(df2.columns)

# Rename the columns
df2.rename(columns={"Sp. Atk": "Special Attack", 
                       "Sp. Def": "Special Defense"},
              inplace=True) # the inplace keyword argument makes pandas modifies the DataFrame columns directly. If this is False, then the method will return a new DataFrame instead.
print(df2.columns)

# Accessing individual DataFrame columns
name_column = df2["Name"]
print(type(name_column))
print(name_column.head())

# Accessing multiple DataFrame columns
columns_df2 = df2[["Name", "Type 1", "Type 2"]] 
print(type(columns_df2))
print(columns_df2.head())

# Accessing rows
df3 = pd.read_csv("pokemon.csv", index_col="Name")
print(df3.head(10))

# Access the row for "Charmeleon"
charmeleon_series = df3.loc["Charmeleon"]
print(type(charmeleon_series))
print(charmeleon_series)

# Access the same Series by position (row number), using the .iloc attribute. Charmeleon would be at row 5 (counting from 0).
charmeleon_series = df3.iloc[5]
print(charmeleon_series)

# Accessing rows via slicing
# You can slice using the index labels.
pokemon_subset = df3.loc["Ivysaur":"Charmander"]
print(len(pokemon_subset))
print(pokemon_subset)

# You can also slice using the row number (starting from 0).
pokemon_subset = df3.iloc[1:4]
print(len(pokemon_subset)) 
print(pokemon_subset)

# Accessing specific rows and columns
print(df3.loc[:, "Type 1"])
print(df3.loc[:, ["Type 1", "Generation"]])
print(df3.loc[["Squirtle", "Pikachu"], ["Type 1", "Generation"]])
print(df3.iloc[1:3, -4:-2])  # Multiple rows and columns by position

# Row and column statistics
# For numeric data, the method returns a Series/DataFrame that includes the index count, mean, std, min, max etc.

print(df3["Speed"].describe())

# For object data such as strings, the resulting Series/DataFrame includes count, unique, top and freq (of top element).
print(df3["Type 1"].describe())

# Use the .value_counts() method (for Series/DataFrame) to get the frequency counts for each unique element in the data.
print(df3["Type 1"].value_counts())

# How many Legendary Pokemons are there? Use .value_counts() to discover this!
print(df3["Legendary"].value_counts())

# Iterating over columns
# for col in df3:
#     print(col)

# # Iterating over rows
# for (key, value) in df3.items(): # iterer over kolonnenavne og deres tilhørende nøgle
#     print(key, value)

# for (row_index, row) in df3.iterrows(): # iterer iver hver række i DF, hvor hver iteration giver adgang til rækkeindeks og række som en Series.
#     print(row_index, row)

# for row in df3.itertuples(): # iterere over hver række i DataFrame, hvor hver iteration giver adgang til hele rækken som en namedtuple
#     print(row)

# DataFrame filtering
# Check whether a Pokemon is of a "Grass" type
condition_series = (df3["Type 1"] == "Grass")
print(condition_series.head())

# show only "Grass" type Pokemons
filtered_df = df3[df3["Type 1"] == "Grass"]
print(filtered_df.head(10))

# A more complicated example (what does it do?)
print(df3[df3["Type 1"].isin(["Water", "Fire"])].head(10)) # rækker, hvor værdien i kolonnen "Type 1" er enten "Water" eller "Fire".

# And another complex one (what does it do?)
filtered_df = df3[(df3["Type 1"] == "Psychic") & 
                     (df3["Generation"] <=3) & 
                     (df3["Legendary"] == True)]
filtered_df = filtered_df[["Type 1", "Type 2", "Generation"]]
print(filtered_df) # rækker, der opfylder flere betingelser på én gang

# Print all Pokemons that have "Water" as Type 1 and "Dragon" as Type 2.
filtered_df = df3[(df3["Type 1"] == "Water") & (df3["Type 2"] == "Dragon")]
print(filtered_df)

# Print all Pokemons that are either Type 2 "Electric" or Type 2 "Ice"
filtered_df = df3[df3["Type 2"].isin(["Electric", "Ice"])]
print(filtered_df)

# Missing values
print(df3.info())

#You can use the .isna() or .isnull() method to figure out the rows that are null. Combine that with .sum() and you get some useful statistics.
print(df3.isna().sum())

# Figure out which rows contain NA values in Type 2
null_type2 = df3[df3["Type 2"].isna()]
print(null_type2)

# Removing missing values
print(df3.shape)
clean_df = df3.dropna()  # Drop all rows with null!
print(clean_df.shape)

# Drop all columns that contain at least one NA value
clean_df = df3.dropna(axis=1)  # Drop columns with NA values

# The methods above returns a copy of the DataFrame with the NA rows/columns removed. If you want to modify (mutate) the DataFrame directly, pass in inplace=True.
df3.dropna(inplace=True)

# Replacing missing values
# Instead of removing NA values, you can also replace them with another value of your choice. Use df.fillna() for this.

# Let's get back our original data before dropping the NAs earlier!
df = pd.read_csv("pokemon.csv", index_col="Name")
df["Type 2"].fillna("Standard", inplace=True)
print(df)
print(df.isna().sum())

# Append rows to DataFrame
dataframe = pd.read_csv("pokemon.csv", index_col="Name")
print(df.shape)

# doubled_df = dataframe.append(dataframe)  # Append the same Pokemon rows to DataFrame
# print(doubled_df.shape)

# Drop duplicates
df = pd.read_csv("pokemon.csv", index_col="Name")
print(df.shape)

df.drop_duplicates(inplace=True)
print(df.shape)

# Apply functions
def standardise(data):
        return (data - data.mean()) / data.std()

df = pd.read_csv("pokemon.csv", index_col="Name")
df[["Attack", "Defense"]] = df[["Attack", "Defense"]].apply(standardise)
print(df)

# Let’s transform Type 1 to uppercase, using lambda functions.
df["Type 1"] = df["Type 1"].apply(lambda x:x.upper())
print(df)

# Plotting
import matplotlib.pyplot as plt
df = pd.read_csv("pokemon.csv", index_col="Name")
fig = plt.figure()
axis = df["Defense"].plot.hist()
plt.show()