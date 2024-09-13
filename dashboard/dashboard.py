import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_data = pd.read_csv('data/day.csv')
hour_data = pd.read_csv('data/hour.csv')

# Title
st.title('Bike Sharing Dashboard')

# Total Rentals Per Day
st.header('Total Bike Rentals Per Day')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.lineplot(x='dteday', y='cnt', data=day_data, ax=ax1)
ax1.set_title('Total Bike Rentals Per Day')
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Rentals')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Rentals by Hour
st.header('Bike Rentals by Hour')
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=hour_data, ax=ax2)
ax2.set_title('Bike Rentals by Hour')
ax2.set_xlabel('Hour of the Day')
ax2.set_ylabel('Total Rentals')
plt.xticks(range(0, 24))
st.pyplot(fig2)