# 🌍 COVID-19 Global Data Tracker

An interactive data analysis and visualization project that tracks global COVID-19 trends over time. The tracker provides insights into cases, deaths, and vaccination rollouts across countries using real-world data.

---

## 🎯 Project Objectives

- Import and clean COVID-19 global data
- Analyze time trends: cases, deaths, and vaccinations
- Compare metrics across countries and time
- Visualize trends using interactive and static charts
- Communicate findings with clear narrative and visuals
- (Bonus) Display data on a global choropleth map
- (Bonus) Allow user interaction for country/date filtering

---

## 🛠️ Tools and Libraries Used

- Python (v3.8+)
- Jupyter Notebook
- pandas
- matplotlib & seaborn
- plotly
- streamlit
- geopandas *(optional, for shapefile-based maps)*
- geodatasets *(if using geopandas maps)*

---

## 🚀 How to Run/View the Project

### ▶️ Option 1: Jupyter Notebook

1. Clone the repository or download the notebook.
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn plotly geopandas geodatasets
   ```
3. Open and run the notebook in Jupyter:
   ```bash
   jupyter notebook covid_tracker.ipynb
   ```

### ▶️ Option 2: Streamlit App

1. Install Streamlit:
   ```bash
   pip install streamlit
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```

> Make sure `owid-covid-data.csv` is in the same folder as your notebook or script.

---

## 📊 Sample Visualizations

- Total COVID-19 cases and deaths over time
- Vaccination progress by country
- Interactive country comparisons
- Choropleth map of global case density

---

## 🔍 Insights & Reflections

- Countries with early, aggressive vaccination efforts show better control of death rates.
- Some nations experienced multiple waves of infections; trend lines reveal seasonal or policy-driven patterns.
- ICU/hospitalization data, where available, complements case/death numbers by showing healthcare system burden.
- Interactive dashboards help users explore data dynamically, making it easier to extract insights.

---

## 📁 Data Source

- [Our World in Data – COVID-19 Dataset](https://github.com/owid/covid-19-data)

---

## 🧠 Author

*Mercylyne Jepleting*  
mercylynetuwei@gmail.com
