import streamlit as st
import pickle
import numpy as np

st.title("check the Envirnment")
#input data
carbon_emission = st.number_input("Carbon Emission (g/km)", min_value=0.0, max_value=500.0, format="%f")
st.divider()
energy_output_value = st.number_input("Energy Output Value (kW)", min_value=0.0, max_value=1000.0, value=100.0, format="%f")
st.divider()
renewability_index = st.number_input("Renewability Index (0-1)", min_value=0.0, max_value=1.0, value=0.5, format="%f")
st.divider()
cost_efficiency = st.number_input("Cost Efficiency ($/kWh)", min_value=0.0, max_value=1.0, value=0.1, format="%f")  
st.divider()

#predict
with open('green_tech_model.pkl', 'rb') as file:
    model = pickle.load(file)
if st.button(" Predict"):
    input_data = np.array([[carbon_emission, energy_output_value, renewability_index, cost_efficiency]])

    prediction = model.predict(input_data)

    #display result
    if prediction[0] == 1:
        st.success("Congrats This Envirnment is Environmentally Friendly")
    else:
        st.info("Envirnment is not sustainable, Consider other options")
        
