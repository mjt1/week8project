import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🌍 COVID-19 Global Data Tracker")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data.csv", parse_dates=['date'])
    return df

df = load_data()

# Sidebar filters
countries = df['location'].dropna().unique().tolist()
selected_countries = st.sidebar.multiselect("Select countries", countries, default=["Kenya", "United States"])
min_date = df['date'].min()
max_date = df['date'].max()
date_range = st.sidebar.date_input("Select date range", [min_date, max_date])

# Filter data
df_filtered = df[df['location'].isin(selected_countries)]
df_filtered = df_filtered[(df_filtered['date'] >= pd.to_datetime(date_range[0])) &
                          (df_filtered['date'] <= pd.to_datetime(date_range[1]))]

# Line plot: Total Cases
st.subheader("Total COVID-19 Cases Over Time")
fig, ax = plt.subplots()
sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location', ax=ax)
st.pyplot(fig)

# Optional: ICU/hospitalization data
if 'hosp_patients' in df.columns:
    st.subheader("COVID-19 Hospitalizations Over Time")
    fig2, ax2 = plt.subplots()
    sns.lineplot(data=df_filtered, x='date', y='hosp_patients', hue='location', ax=ax2)
    st.pyplot(fig2)
