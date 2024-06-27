import streamlit as st
import pandas as pd
import pickle


model = pickle.load(open("xgbr_model.pkl", "rb"))


st.title("Laptop Price Predictor")

def predict_price(company, type_name, inches, ram, os, weight, touchscreen, ips, screen_width, screen_height,
                  cpu_brand, cpu_freq, memory_size, memory_type, gpu_brand):
    input_data = pd.DataFrame({
        "Company": [company],
        "TypeName": [type_name],
        "Inches": [inches],
        "Ram": [ram],
        "OpSys": [os],
        "Weight": [weight],
        "Touchscreen": [1 if touchscreen == "Yes" else 0],
        "IPS": [1 if ips == "Yes" else 0],
        "ScreenWidth": [screen_width],
        "ScreenHeight": [screen_height],
        "CpuBrand": [cpu_brand],
        "CpuFrequency": [cpu_freq],
        "MemorySize": [memory_size],
        "MemoryType": [memory_type],
        "GpuBrand": [gpu_brand]
    })
    prediction = model.predict(input_data)
    return prediction[0]


# Input fields
company = st.text_input("Enter the company name:")
type_name = st.text_input("Enter the type of laptop:")
inches = st.number_input("Enter the screen size in inches:", min_value=0.0)
ram = st.number_input("Select the RAM size (GB):", min_value=0)
os = st.text_input("Enter the operating system:")
weight = st.number_input("Enter the weight in kg:", min_value=0.0)
touchscreen = st.selectbox("Is it a touchscreen?", ["Yes", "No"])
ips = st.selectbox("Does it have IPS?", ["Yes", "No"])
screen_width = st.number_input("Enter the screen width in pixels:", min_value=0)
screen_height = st.number_input("Enter the screen height in pixels:", min_value=0)
cpu_brand = st.text_input("Enter the CPU brand:")
cpu_freq = st.number_input("Enter the CPU frequency in GHz:", min_value=0.0)
memory_size = st.number_input("Enter the memory size in GB:", min_value=0)
memory_type = st.text_input("Enter the memory type (e.g., SSD, HDD):")
gpu_brand = st.text_input("Enter the GPU brand:")


if st.button("Predict Price"):
    prediction = predict_price(company, type_name, inches, ram, os, weight, touchscreen, ips, screen_width, screen_height, cpu_brand, cpu_freq, memory_size, memory_type, gpu_brand)

    st.write(f"The predicted price of the laptop is: {prediction:.2f}")