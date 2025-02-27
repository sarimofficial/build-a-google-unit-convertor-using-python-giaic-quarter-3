import streamlit as st
from forex_python.converter import CurrencyRates

# Google Unit Converter
st.header("🔢 Google Unit Converter")
unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature", "Currency"])

if unit_type == "Length":
    length_units = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Millimeters": 0.001, "Miles": 1609.34, "Yards": 0.9144, "Feet": 0.3048, "Inches": 0.0254}
    from_unit = st.selectbox("From", list(length_units.keys()))
    to_unit = st.selectbox("To", list(length_units.keys()))
    value = st.number_input("Enter Value", min_value=0.0)
    if st.button("Convert"):
        result = value * (length_units[to_unit] / length_units[from_unit])
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "Weight":
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))
    value = st.number_input("Enter Value", min_value=0.0)
    if st.button("Convert"):
        result = value * (weight_units[to_unit] / weight_units[from_unit])
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "Temperature":
    temp_value = st.number_input("Enter Temperature")
    temp_from = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_to = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        if temp_from == "Celsius":
            result = temp_value * 9/5 + 32 if temp_to == "Fahrenheit" else temp_value + 273.15 if temp_to == "Kelvin" else temp_value
        elif temp_from == "Fahrenheit":
            result = (temp_value - 32) * 5/9 if temp_to == "Celsius" else (temp_value - 32) * 5/9 + 273.15 if temp_to == "Kelvin" else temp_value
        else:
            result = temp_value - 273.15 if temp_to == "Celsius" else (temp_value - 273.15) * 9/5 + 32 if temp_to == "Fahrenheit" else temp_value
        st.success(f"{temp_value} {temp_from} = {result:.2f} {temp_to}")

elif unit_type == "Currency":
    c = CurrencyRates()
    from_currency = st.text_input("From Currency (e.g., USD)")
    to_currency = st.text_input("To Currency (e.g., EUR)")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Convert"):
        try:
            result = c.convert(from_currency.upper(), to_currency.upper(), amount)
            st.success(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
        except Exception as e:
            st.error("Invalid currency code or conversion error.")

# Footer
st.markdown("---")
st.write("© 2025 **Created by Muhammad Sarim **. All rights reserved.")
