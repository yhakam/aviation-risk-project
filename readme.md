# Aviation Risk Intelligence Platform  
### Real-Time Flight Monitoring, Weather Fusion, and AI-Powered Risk Analysis

This project aims to build an end-to-end aviation intelligence system capable of:

- collecting real-time flight data from OpenSky Network  
- retrieving METAR/TAF weather observations from authoritative aviation sources  
- merging operational and meteorological data into a unified enriched dataset  
- performing advanced exploratory data analysis (EDA) on global flight activity  
- preparing high-quality features for machine learning risk models  
- providing interactive visualizations and dashboards  
- enabling a future API for real-time risk scoring  

The objective is to create a **professional-grade AI pipeline**, similar to what is used in  
**airlines, aviation safety agencies, and aerospace companies**.

---

## 1. Project Overview

Modern aviation risk monitoring requires combining heterogeneous data streams:

- **ADS-B flight telemetry**  
- **Weather conditions at departure, arrival, and en-route**  
- **Aircraft performance metrics**  
- **Operational context**

This platform performs the first essential steps toward a scalable aviation risk engine:

1. **Data Ingestion Layer**  
   - Real-time flight snapshots from OpenSky (`/api/states/all`)  
   - METAR observations via NOAA / AWC AviationWeather API  

2. **Preprocessing & Fusion Layer**  
   - Cleans raw data  
   - Aligns timestamps  
   - Enriches each flight with the corresponding METAR context  

3. **Exploratory Data Analysis (EDA)**  
   - Structural analysis of flight variables  
   - Analysis of meteorological conditions  
   - Identification of missing data patterns  
   - Early correlations between weather and flight behavior  

4. **Feature Engineering (Upcoming)**  
   - Aircraft dynamics extraction  
   - Weather-derived severity indexes  
   - Flight phase detection  
   - Risk-relevant synthetic variables  

5. **Machine Learning Pipeline (Upcoming)**  
   - Baseline models  
   - Gradient boosting models for risk classification  
   - Explainability tools (SHAP)  
   - Model evaluation suite  

6. **Application Layer (Upcoming)**  
   - **Streamlit dashboard** for visualization  
   - **REST API (FastAPI)** for flight risk inference  

---

## 2. Repository Structure

