# Autoimmune Sickness Duration Prediction using Random Forest Regression
This project aims to predict an autoimmune disease's sickness duration in months using Random Forest Regression. This project is deployed as a web service using Streamlit Cloud. THe model accepts 24 inputs to predict the sickness duration. 

### Feature Descriptions:
- WBC Count (cells/mcL): White blood cell count in the blood sample.
- MCH (pg): Mean corpuscular hemoglobin, a measure of the average amount of hemoglobin in a red blood cell.
- RDW (%): Red cell distribution width, indicating the variation in the size of red blood cells.
- PLT Count (cells/mcL): Platelet count, a measure of the number of platelets in the blood.
- MCV (fL): Mean corpuscular volume, indicating the average size of red blood cells.
- CRP (mg/L): C-reactive protein, an indicator of inflammation in the body.
- Neutrophils (%): The percentage of neutrophils in the blood sample.
- RBC Count (million cells/mcL): Red blood cell count.
- Hemoglobin (g/dL): The amount of hemoglobin in the blood.
- ESR (mm/hr): Erythrocyte sedimentation rate, a test that measures how quickly red blood cells settle.
- Esbach (g/dL): An indicator of protein levels in urine.
- MBL Level (ng/mL): Mannose-binding lectin, a protein involved in the immune response.
- MCHC (g/dL): Mean corpuscular hemoglobin concentration, indicating the average concentration of hemoglobin in red blood cells.
- Hematocrit (%): The proportion of blood volume that is occupied by red blood cells.
- Age (years): The age of the patient.
- Monocytes (%): The percentage of monocytes in the blood sample.
- Reticulocyte Count (%): The percentage of young red blood cells in the blood.
- Eosinophils (%): The percentage of eosinophils in the blood.
- C3 (mg/dL): Complement protein C3, part of the immune response.
- Basophils (%): The percentage of basophils in the blood.
- Lymphocytes (%): The percentage of lymphocytes in the blood.
- C4 (mg/dL): Complement protein C4, also part of the immune system.
- MPV (fL): Mean platelet volume, indicating the average size of platelets.
- Diagnosis Graves' Disease: A medical condition affecting the thyroid, either "Yes" or "No".

### Model Performance:
This model was trained using a dataset containing medical features such as WBC Count, MCH, Hemoglobin, and more. The trained model was evaluated on the following metrics:
- Accuracy: 0.85
- F1-Score: 0.88
- Precision: 0.86
- Recall: 0.89
These performance metrics are indicative of the model's effectiveness in predicting sickness duration based on the provided features.

### Security and Authentication:
For this deployment, there are no authentication measures enabled.

### Troubleshooting:

1. Issue: "ModuleNotFoundError" when running the app
   - Ensure all dependencies are installed by running:
     ```bash
     pip install -r requirements.txt
     ```
2. Issue: Model file not found 
   - Ensure that the model file (`random_forest_model.pkl`) is located in the same directory as the `app.py` file.

3. Issue: Incorrect input format 
   - Make sure all numerical inputs are valid and within the specified ranges.

## Setup Instructions

### 1. Requirements
- Python 3.7 or higher
- Streamlit
- joblib

### 2. Requirements File (requirements.txt):
Ensure that you include a `requirements.txt` file listing all dependencies for the project, including:
- `streamlit`
- `joblib`
- `scikit-learn`
- `numpy`

### Conclusion:
This project aims to provide a user-friendly interface for making sickness duration predictions based on test results. By deploying the model as a web service, healthcare professionals can easily input medical data and receive predictions for clinical decision-making.