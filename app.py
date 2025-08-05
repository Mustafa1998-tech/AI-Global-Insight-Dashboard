import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page config with dark theme
st.set_page_config(page_title="Global AI Usage Dashboard - Dark Mode", layout="wide")

# Custom CSS for dark background and white text
st.markdown(
    """
    <style>
    .main {
        background-color: #121212;
        color: white;
    }
    .stMetric {
        color: white !important;
    }
    .css-1d391kg, .css-18e3th9 { 
        background-color: #121212;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load data
df = pd.read_csv("ai_data.csv")

# General metrics
total_countries = df["Country"].nunique()
total_users = df["Users_Millions"].sum()
avg_usage = df["AI_Usage_Perc"].mean()
top_country = df.loc[df["AI_Usage_Perc"].idxmax()]["Country"]
top_usage = df["AI_Usage_Perc"].max()

# Title and description
st.markdown("<h2 style='color:#FFD700;'>🌍 Global AI Usage Analysis Dashboard</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#ADFF2F;'>An interactive dashboard with vibrant rainbow colors and dark mode like Power BI</p>", unsafe_allow_html=True)

# Metrics display
col1, col2, col3, col4 = st.columns(4)
col1.metric("🌐 Number of Countries", total_countries)
col2.metric("👥 Total Users (Millions)", f"{total_users:.0f}")
col3.metric("📊 Average Usage (%)", f"{avg_usage:.2f}")
col4.metric("🏆 Top Country", f"{top_country} ({top_usage}%)")

# Continent filter
continents = ["All"] + sorted(df["Continent"].unique())
selected = st.selectbox("🔍 Filter by Continent", continents)

if selected != "All":
    filtered_df = df[df["Continent"] == selected]
else:
    filtered_df = df.copy()

# Top AI usage countries bar plot with rainbow colors
st.subheader("📊 Top AI Usage Countries")
top_countries = filtered_df.sort_values(by="AI_Usage_Perc", ascending=False).head(10)
fig1, ax1 = plt.subplots(figsize=(10,6))
sns.barplot(data=top_countries, y="Country", x="AI_Usage_Perc", palette="rainbow", ax=ax1)
ax1.set_facecolor('#121212')
fig1.patch.set_facecolor('#121212')
ax1.tick_params(colors='white')
ax1.spines['bottom'].set_color('white')
ax1.spines['left'].set_color('white')
ax1.set_xlabel("Usage Percentage (%)", color='white')
ax1.set_ylabel("Country", color='white')
ax1.set_title("Top 10 Countries by AI Usage", color='white')
st.pyplot(fig1)

# Users distribution by continent pie chart with rainbow colors
st.subheader("📈 Users Distribution by Continent")
users_by_continent = filtered_df.groupby("Continent")["Users_Millions"].sum()
fig2, ax2 = plt.subplots(figsize=(8,8))
colors = sns.color_palette("rainbow", len(users_by_continent))
ax2.pie(users_by_continent, labels=users_by_continent.index, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'color':'white','weight':'bold'})
ax2.axis('equal')
fig2.patch.set_facecolor('#121212')
st.pyplot(fig2)

# Usage percentage distribution by continent box plot with dark background
st.subheader("📊 AI Usage Percentage Distribution by Continent")
fig3, ax3 = plt.subplots(figsize=(10,6))
sns.boxplot(data=filtered_df, x="Continent", y="AI_Usage_Perc", palette="rainbow", ax=ax3)
ax3.set_facecolor('#121212')
fig3.patch.set_facecolor('#121212')
ax3.tick_params(colors='white')
ax3.spines['bottom'].set_color('white')
ax3.spines['left'].set_color('white')
ax3.set_ylabel("Usage Percentage (%)", color='white')
ax3.set_xlabel("Continent", color='white')
ax3.set_title("AI Usage Percentage Distribution by Continent", color='white')
st.pyplot(fig3)

# Data table with dark style
st.subheader("📋 Data Table")
st.dataframe(filtered_df.style.set_properties(**{
    'background-color': '#121212',
    'color': 'white',
    'border-color': 'gray'
}), use_container_width=True)

# Interactive map with Plotly Express using dark theme
st.subheader("🌍 Interactive Map")

if {"Latitude", "Longitude"}.issubset(filtered_df.columns):
    fig_map = px.scatter_geo(
        filtered_df,
        lat="Latitude",
        lon="Longitude",
        size="Users_Millions",
        color="AI_Usage_Perc",
        color_continuous_scale=px.colors.sequential.Plasma,
        hover_name="Country",
        hover_data={"AI_Usage_Perc": True, "Users_Millions": True},
        title="Country Locations and AI Users Size",
        projection="natural earth",
        template="plotly_dark"
    )
    fig_map.update_layout(
        geo=dict(
            showland=True,
            landcolor="rgb(18, 18, 18)",
            showcountries=True,
            countrycolor="rgb(80, 80, 80)"
        ),
        margin={"r":0,"t":30,"l":0,"b":0},
        paper_bgcolor='rgba(18,18,18,1)',
        font=dict(family="Segoe UI", size=14, color="white")
    )
    st.plotly_chart(fig_map, use_container_width=True)
else:
    st.warning("The dataset does not contain Latitude and Longitude columns for map display.")
