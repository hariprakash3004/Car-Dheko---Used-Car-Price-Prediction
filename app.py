import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Load dataset and model
final_cars = pd.read_csv("C:/Users/SAM/Desktop/used car price prediction/finalcar.csv")
with open('gb_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and image
st.title("Car Dheko Uesd car Price Prediction App")
st.write("Enter the details below to get an estimated price.")
car_image = Image.open('C:/Users/SAM/Desktop/used car price prediction/pexels-mikebirdy-136872.jpg')  # Replace with your image file
st.image(car_image, use_column_width=True)

# Sidebar for user inputs with options based on data in CSV
st.sidebar.header("Enter Car Specifications")

# Unique options for dropdowns
bodytype_options = sorted(final_cars['bodytype'].unique())
car_seats_options = sorted(final_cars['Car_seats'].unique())
model_year_options = sorted(final_cars['modelYear'].unique())
kilometer_options = sorted(final_cars['kilometer'].unique())
fueltype_options = sorted(final_cars['fueltype'].unique())
ownerNo_options = sorted(final_cars['ownerNo'].unique())
transmission_options = sorted(final_cars['transmission'].unique())
insurance_options = sorted(final_cars['Insurance'].unique())
engine_cc_options = sorted(final_cars['engine_cc'].unique())
oem_options = sorted(final_cars['oem'].unique())
gear_box_options = sorted(final_cars['gear_box'].unique())
mileage_options = sorted(final_cars['Mileage'].unique())
drivetype_options = sorted(final_cars['drivetype'].unique())
city_options = sorted(final_cars['city'].unique())

# User inputs as dropdowns
bodytype = st.sidebar.selectbox("Body Type", bodytype_options)
car_seats = st.sidebar.selectbox("Number of Seats", car_seats_options)
modelYear = st.sidebar.selectbox("Model Year", model_year_options)
kilometer = st.sidebar.selectbox("Kilometers Driven", kilometer_options)
fueltype = st.sidebar.selectbox("Fuel Type", fueltype_options)
ownerNo = st.sidebar.selectbox("Number of Previous Owners", ownerNo_options)
transmission = st.sidebar.selectbox("Transmission Type", transmission_options)
insurance = st.sidebar.selectbox("Insurance Status", insurance_options)
engine_cc = st.sidebar.selectbox("Engine Size (cc)", engine_cc_options)
oem = st.sidebar.selectbox("OEM", oem_options)
gear_box = st.sidebar.selectbox("Gear Box", gear_box_options)
mileage = st.sidebar.selectbox("Mileage (km/l)", mileage_options)
drivetype = st.sidebar.selectbox("Drive Type", drivetype_options)
city = st.sidebar.selectbox("City", city_options)

# Prepare input data as a DataFrame for encoding
input_data = pd.DataFrame({
    'bodytype': [bodytype],
    'Car_seats': [car_seats],
    'modelYear': [modelYear],
    'kilometer': [kilometer],
    'fueltype': [fueltype],
    'ownerNo': [ownerNo],
    'transmission': [transmission],
    'Insurance': [insurance],
    'engine_cc': [engine_cc],
    'oem': [oem],
    'gear_box': [gear_box],
    'Mileage': [mileage],
    'drivetype': [drivetype],
    'city': [city]
})

# Align input columns with model training data using one-hot encoding
input_data_encoded = pd.get_dummies(input_data)
final_cars_encoded = pd.get_dummies(final_cars).reindex(columns=input_data_encoded.columns, fill_value=0)

# Predict button
if st.button("Estimated used car price"):
    # Predict using the encoded input data
    predicted_price = model.predict(input_data_encoded)[0]
    st.subheader(f"Estimated Car Price: ${predicted_price:,.2f}")

# Footer
st.write("\n\n---")
st.write("Developed by hariprakash N - Car Price Prediction App")
