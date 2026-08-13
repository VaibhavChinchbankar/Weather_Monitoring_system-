import streamlit as st
import pickle


with open("weather_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🌦️ Weather Monitoring System")
st.write("Enter the weather parameters to predict rainfall.")


temperature = st.number_input("Temperature", value=25.0)
humidity = st.number_input("Humidity", value=70.0)
wind_speed = st.number_input("Wind Speed", value=10.0)
cloud_cover = st.number_input("Cloud Cover", value=50.0)
pressure = st.number_input("Pressure", value=1010.0)


if st.button("Predict"):

    prediction = model.predict([[
        temperature,
        humidity,
        wind_speed,
        cloud_cover,
        pressure
    ]])

    st.success("Prediction: " + str(prediction[0]))
