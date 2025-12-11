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

The repository is organized following a modular, production-oriented layout
commonly used in professional data science and machine learning projects.

### Application Layer
- `app/api/`  
  REST API for real-time risk inference (FastAPI, upcoming)
- `app/streamlit/`  
  Interactive dashboard for visualization and monitoring (Streamlit, upcoming)

### Data Layer
- `data/raw/`  
  Raw flight telemetry (OpenSky) and meteorological observations (METAR)
- `data/processed/`  
  Cleaned and enriched flight–weather datasets

### Analysis & Research
- `notebooks/01_eda_flights_enriched.ipynb`  
  Exploratory data analysis of the enriched dataset

### Core Pipeline
- `src/ingestion/`  
  Data collection scripts (OpenSky, METAR)
- `src/preprocessing/`  
  Data cleaning, alignment, and flight–weather fusion
- `src/features/`  
  Feature engineering and risk-related variable construction (upcoming)
- `src/models/`  
  Model training, inference, and serialization (upcoming)
- `src/evaluation/`  
  Model evaluation, diagnostics, and explainability (upcoming)
- `src/utils/`  
  Shared utility functions

### Project Configuration
- `requirements.txt`  
  Python dependencies
- `.gitignore`  
  Git ignore rules
- `README.md`  
  Project documentation




---

## 3. Technologies Used

- **Python 3.10+**
- **Pandas, NumPy**
- **Seaborn, Matplotlib**
- **Requests**
- **Scikit-Learn**
- **XGBoost / LightGBM (upcoming)**
- **SHAP explainability**
- **Streamlit / FastAPI (upcoming)**


---

## 4. Current Capabilities

- Fully automated collection of flight telemetry  
- METAR ingestion with robust error handling  
- Clean dataset merging with temporal alignment  
- Unified flight-weather dataset of >10,000 rows per snapshot  
- Initial exploratory data analysis  
- Project-ready modular codebase  
- Production-style repository layout  

---

## 5. Roadmap

### ✓ Completed
- Project structure  
- Ingestion (OpenSky + METAR)  
- Raw → Processed transformation  
- Enriched dataset generation  
- Setup for professional EDA  

###  In Progress
- Advanced EDA (correlations, distributions, anomalies)
- Feature engineering (weather indexes, aircraft dynamics)
- Model training and evaluation

###  Coming Next
- Real-time risk scoring  
- Interactive dashboard  
- Model explainability suite  
- API for external integration  

---

## 6. Vision

The long-term goal is to develop a **real-time aviation risk assessment engine** capable of:

- detecting abnormal flight dynamics  
- quantifying risk under adverse weather  
- predicting potential incident scenarios  
- assisting aviation safety teams in decision-making  

The project follows industry-level engineering principles and aims to demonstrate  
**machine learning applied to high-stakes, real-world systems.**

---

## 7. Author

**Yassine Hakam**  
Master's candidate in AI & Big Data  

---

# This project is built with high engineering standards and aims to meet expectations of top-tier universities and future aerospace employers.
