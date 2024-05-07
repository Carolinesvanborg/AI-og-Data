import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

url = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Complete_TAVG_complete.txt"

df = pd.read_csv(url, delim_whitespace=True, skiprows=34, header=None, index_col= False)

# Præprocesser data for at fjerne manglende værdier (NaN).
df_clean = df.dropna()

print(df_clean.head(3))

# middelværdi, median, standardafvigelse, min/max, kvartiler
print(df_clean.describe())
print(df_clean.columns)

# visualisering af linjeplot af temperaturen over tid
x = df_clean[0]  # X-axis points
y = df_clean[2] # Y-axis points
 
plt.plot(x, y)  # Plot the chart
plt.xlabel("Time")  # Set X-axis label
plt.ylabel("Monthly Anomaly, Unc.")  # Set Y-axis label
plt.title("Temperature Over Time")  # Set plot title
plt.show()  # display

#  figur med flere underplots
# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot each subplot
axs[0, 0].plot(df_clean[0], df_clean[3])
axs[0, 0].set_title('Annual Anomaly, Unc')
axs[0, 1].plot(df_clean[0], df_clean[4])
axs[0, 1].set_title('Five-year Anomaly, Unc')
axs[1, 0].plot(df_clean[0], df_clean[5])
axs[1, 0].set_title('Ten-year Anomaly, Unc')
axs[1, 1].plot(df_clean[0], df_clean[6])
axs[1, 1].set_title('Twenty-year Anomaly, Unc')

# Add labels and title
for ax in axs.flat:
    ax.set(xlabel='Year', ylabel='Temperature')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.tight_layout()
plt.show()

# varmekort der repræsenterer ændringer i temperaturer over årene.
x3d = df_clean[0]  # X-axis points
y3d = df_clean[1] # Y-axis points
z3d = df_clean[2] # z-axis points

# Create figure and 3D subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')


# Create the heatmap
img = ax.scatter(x3d, y3d, z3d, c=z3d, cmap='coolwarm', marker='s', s=40)

# Add color bar
cbar = plt.colorbar(img)
cbar.set_label('Temperature')

# Add title and labels
ax.set_title("3D Heatmap")
ax.set_xlabel('Year')
ax.set_ylabel('Month')
ax.set_zlabel('Temperature')

# Calculate average temperature for each year
avg_temp_yearly = df_clean.groupby(0)[2].mean()

# Plot line representing average temperature changes over the years
ax.plot(avg_temp_yearly.index, [df_clean[1].unique().mean()] * len(avg_temp_yearly), avg_temp_yearly.values, color='black', marker='o', linestyle='-', markersize=0, label = "Average temperature")
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, loc= 'upper right')

# Display plot
plt.show()
