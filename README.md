# Laptop Prediction Model

A machine learning project that predicts laptop prices based on their specifications using regression techniques. This includes data preprocessing, feature engineering, model training, and a Streamlit web app for live predictions.

---

## ​ Table of Contents

1. [Project Overview](#project-overview)  
2. [Dataset & Features](#dataset--features)  
3. [Methodology](#methodology)  
4. [How to Run](#how-to-run)  
5. [Usage](#usage)  
6. [Results & Evaluation](#results--evaluation)  
7. [Tech Stack](#tech-stack)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## ​ Project Overview

This project aims to build a regression model that predicts laptop prices using real-world specifications such as:

- **Company** (e.g., Dell, HP, Apple)  
- **Type** (Notebook, Ultrabook, Gaming, etc.)  
- **Display specs** (Screen Inches, Resolution, Touch/IPS)  
- **CPU & GPU**  
- **RAM** & **Storage** (HDD, SSD capacities)  
- **Others** (Weight, OS, etc.)

---

## ​ Dataset & Features

- `laptop_prices.csv`: Primary dataset used for training.
- Key columns include: `Inches`, `Ram`, `SSD`, `HDD`, `Flash_Storage`, `TouchScreen`, `IPS_Screen`, `Company`, `TypeName`, `CPU_Brand`, `GPU_Brand`, etc.

---

## ​​ Methodology

1. **Preprocessing**:  
   - Handling missing values  
   - Parsing and cleaning feature columns (e.g., `"8GB"` → `8`)  
   - Encoding categorical variables (One-Hot, Label Encoding)  

2. **Feature Engineering**:  
   - Creating new features (e.g., `IPS_Screen`, `TouchScreen`)  
   - Extracting parts of composite strings (`CPU_Brand`, `GPU_Brand`)  

3. **Model Training**:  
   - Compared models: Linear Regression, SVR, Random Forest, XGBoost, etc.  
   - Hyperparameter tuning using Grid Search & Cross-Validation  

4. **Evaluation**:  
   - Metrics used: R² score, RMSE

5. **Deployment**:  
   - Streamlit app (`streamlit_app.py`) for live predictions

- Utility functions in `util.py` for single-instance prediction.

---

## ​ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/sameerchokhande/Laptop_Prediction_Model.git
   cd Laptop_Prediction_Model
2.Install dependencies:
pip install -r requirements.txt

3.Launch Streamlit app:
streamlit run streamlit_app.py





Tech Stack
Python

Data Processing: Pandas, NumPy

Visualization & EDA: Seaborn, Matplotlib

Machine Learning: Scikit-learn, XGBoost

Deployment: Streamlit

Persistence: pickle / joblib
