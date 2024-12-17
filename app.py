import streamlit as st
import joblib
import numpy as np


model = joblib.load('random_forest_model.pkl')

def make_prediction(inputs):
    input_data = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

def run_app():
    st.title("Autoimmune Sickness Duration Prediction Model")

    st.write("""
    This application predicts the sickness duration of an autoimmune condition based on various test results.
    Please enter the values for the following medical features:
    """)

    WBC_Count = st.number_input('WBC Count (cells/mcL)', min_value=0.0, max_value=100000.0, value=5.0, step=0.1)
    MCH = st.number_input('MCH (pg)', min_value=0.0, max_value=100.0, value=27.0, step=0.1)
    RDW = st.number_input('RDW (%)', min_value=10.0, max_value=20.0, value=14.0, step=0.1)
    PLT_Count = st.number_input('PLT Count (cells/mcL)', min_value=0.0, max_value=1000000.0, value=300000.0, step=1000.0)
    MCV = st.number_input('MCV (fL)', min_value=50.0, max_value=100.0, value=90.0, step=0.1)
    CRP = st.number_input('CRP (mg/L)', min_value=0.0, max_value=200.0, value=5.0, step=0.1)
    Neutrophils = st.number_input('Neutrophils (%)', min_value=0.0, max_value=100.0, value=60.0, step=0.1)
    RBC_Count = st.number_input('RBC Count (million cells/mcL)', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    Hemoglobin = st.number_input('Hemoglobin (g/dL)', min_value=0.0, max_value=20.0, value=13.0, step=0.1)
    ESR = st.number_input('ESR (mm/hr)', min_value=0, max_value=100, value=10)
    Esbach = st.number_input('Esbach (g/dL)', min_value=0.0, max_value=20.0, value=0.5, step=0.1)
    MBL_Level = st.number_input('MBL Level (ng/mL)', min_value=0.0, max_value=500.0, value=50.0, step=1.0)
    MCHC = st.number_input('MCHC (g/dL)', min_value=30.0, max_value=40.0, value=33.0, step=0.1)
    Hematocrit = st.number_input('Hematocrit (%)', min_value=20.0, max_value=60.0, value=45.0, step=0.1)
    Age = st.number_input('Age (years)', min_value=0, max_value=100, value=30)
    Monocytes = st.number_input('Monocytes (%)', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    Reticulocyte_Count = st.number_input('Reticulocyte Count (%)', min_value=0.0, max_value=10.0, value=0.5, step=0.1)
    Eosinophils = st.number_input('Eosinophils (%)', min_value=0.0, max_value=100.0, value=3.0, step=0.1)
    C3 = st.number_input('C3 (mg/dL)', min_value=0.0, max_value=200.0, value=100.0, step=1.0)
    Basophils = st.number_input('Basophils (%)', min_value=0.0, max_value=100.0, value=1.0, step=0.1)
    Lymphocytes = st.number_input('Lymphocytes (%)', min_value=0.0, max_value=100.0, value=30.0, step=0.1)
    C4 = st.number_input('C4 (mg/dL)', min_value=0.0, max_value=100.0, value=30.0, step=1.0)
    MPV = st.number_input('MPV (fL)', min_value=5.0, max_value=20.0, value=9.0, step=0.1)
    Diagnosis_Graves_disease = st.selectbox("Diagnosis Graves' Disease", ('Yes', 'No'))

    inputs = [
        WBC_Count, MCH, RDW, PLT_Count, MCV, CRP, Neutrophils, RBC_Count,
        Hemoglobin, ESR, Esbach, MBL_Level, MCHC, Hematocrit, Age, Monocytes,
        Reticulocyte_Count, Eosinophils, C3, Basophils, Lymphocytes, C4, MPV
    ]
    try:
        Diagnosis_Graves_disease = 1 if Diagnosis_Graves_disease == 'Yes' else 0
        inputs.append(Diagnosis_Graves_disease)

        inputs = [float(i) for i in inputs]  

        if st.button('Predict'):
            prediction = make_prediction(inputs)
            st.write(f"The predicted sickness duration in months is: {prediction[0]:.2f}")

    except ValueError as e:
        st.error(f"Error: {str(e)}")
        st.warning("Please ensure all input fields contain valid numeric values.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    run_app()