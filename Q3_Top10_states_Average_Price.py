# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:07:08 2023

@author: manim
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_honda_sell_data_new.csv")

# Group the data by state and condition, and calculate the average price for each group
state_prices = df.groupby(['State', 'Condition'])['Price'].mean().unstack()

# Calculate the total average price by state, and sort the values in descending order
state_avg_price = state_prices.mean(axis=1).sort_values(ascending=False)

# Select the top 10 states by average price, excluding DE and WV
top_10_states = state_avg_price.loc[~state_avg_price.index.isin(['DE', 'WV', 'AK', 'WY', 'OK'])].head(10).index

# only the top 10 states
state_prices_top10 = state_prices.loc[top_10_states]

#generate summary statistics for the filtered data
print(state_prices_top10.describe())

# Define the colors for each category
colors = ['#2f4b7c', '#8dc6f7', '#8193a5']

#Create a side by side bar
ax = state_prices_top10.plot.bar(figsize=(14, 12), width=0.8, color=colors)

# Set the title and axis labels
plt.title('Average Honda Car Price by State')
plt.xlabel('State')
plt.ylabel('Price($)')

# Add average price values to each bar
for i in range(len(state_prices_top10)):
    for j in range(len(state_prices_top10.columns)):
        value = state_prices_top10.iloc[i,j]
        offset = (j - 1) * 0.3
        plt.text(i + offset, value+1000, f"${value:.0f}", ha='center', va='bottom', rotation=90, fontsize=10)

# Show the plot
plt.show()


