import streamlit as st
import pandas as pd
import pickle

# ✅ Set page config
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

# ✅ Load the model
@st.cache_resource
def load_model():
    with open('laptop_price_model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# ✅ Extract expected feature names from model
expected_features = model.get_booster().feature_names

# 🎨 Clean, simple styling
st.markdown(
    """
    <style>
    /* Background setup */
    .stApp {
        background-color: #8ec3eb;
        color: #333333;
    }

    /* Buttons style */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 4px;
        transition: 0.3s;
        font-size: 18px;
        border: none;
    }

    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }

    /* Inputs style - clean look */
    .stTextInput input, .stNumberInput input, .stSelectbox select, .stRadio div {
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        background: #ffffff;
        color: #333333;
        border: 1px solid #ddd;
    }

    /* Headings style */
    h1, h2, h3 {
        font-family: 'Trebuchet MS', sans-serif;
        color: #d64161;
    }

    /* Prediction result style */
    .prediction-result {
        font-size: 28px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ App Title and Description
st.title('💻 Laptop Price Predictor')
st.markdown('### Enter laptop specifications to predict the price 🚀')

# ✅ User input fields
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('Brand', ['Apple', 'HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Other'])
    type_name = st.selectbox('Type', ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible'])
    ram = st.slider('RAM (GB)', 2, 64, 8)
    weight = st.number_input('Weight (Kg)', min_value=0.5, max_value=5.0, value=1.5)

with col2:
    touchscreen = st.radio('Touchscreen', ['No', 'Yes'])
    ips = st.radio('IPS Display', ['No', 'Yes'])
    ppi = st.number_input('Pixels Per Inch (PPI)', min_value=50, max_value=400, value=150)
    cpu_brand = st.selectbox('CPU Brand', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD'])

hdd = st.number_input('HDD (GB)', min_value=0, max_value=2000, value=0)
ssd = st.number_input('SSD (GB)', min_value=0, max_value=2000, value=256)
gpu_brand = st.selectbox('GPU Brand', ['Intel', 'AMD', 'Nvidia'])
os = st.selectbox('Operating System', ['Windows', 'Mac', 'Linux', 'Others'])

# ✅ Convert user inputs to DataFrame
input_data = pd.DataFrame([[company, type_name, ram, weight, int(touchscreen == 'Yes'),
                            int(ips == 'Yes'), ppi, cpu_brand, hdd, ssd, gpu_brand, os]],
                          columns=['Company', 'TypeName', 'Ram', 'Weight', 'TouchScreen', 'Ips',
                                   'Ppi', 'Cpu_brand', 'HDD', 'SSD', 'Gpu_brand', 'Os'])

# ✅ One-hot encoding to match training data columns
input_data = pd.get_dummies(input_data)

# ✅ Ensure all expected columns are present (add missing ones with 0s)
for col in expected_features:
    if col not in input_data.columns:
        input_data[col] = 0

# ✅ Reorder columns to match model’s expectations
input_data = input_data[expected_features]

# ✅ Prediction button with error handling
if st.button('💸 Predict Price'):
    try:
        with st.spinner('💭 Analyzing specs...'):
            prediction = model.predict(input_data)
        st.success('✅ Prediction Complete!')
        st.markdown(f'<p class="prediction-result">💰 Estimated Price: ${round(prediction[0], 2)}</p>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")

# ✅ Footer
st.markdown("### Thanks For Using Me ❤️")
