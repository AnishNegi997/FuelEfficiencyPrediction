from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np  # For logarithmic transformation

# Initialize Flask app
app = Flask(__name__)

# Load the pipeline
pipeline = joblib.load('randomforest_pipeline.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    fuelCost = float(request.form['fuelCost'])
    CO2 = float(request.form['CO2_log'])
    cylinders = float(request.form['cylinders'])
    displ = float(request.form['displ'])
    year = int(request.form['year'])
    fuelType = request.form['fuelType']
    VClass = request.form['VClass']
    make = request.form['make']
    
    # Apply logarithmic transformation to the relevant features
    # To handle cases where the value might be zero or negative (which would cause an error in log)
    # We can add a small constant to avoid log(0), if your data doesn't allow 0s. Alternatively, you can drop such values.
    log_fuelCost = np.log(fuelCost + 1)  # Log transformation with a small constant to avoid log(0)
    log_CO2 = np.log(CO2 + 1)  # Same for CO2
    log_displ = np.log(displ + 1)  # Same for displacement
    log_cylinders = np.log(cylinders + 1)  # Same for cylinders

    # Prepare the transformed input data
    input_data = {
        'fuelCost': log_fuelCost,
        'CO2_log': log_CO2,
        'cylinders': log_cylinders,
        'displ': log_displ,
        'year': year,
        'fuelType': fuelType,
        'VClass': VClass,
        'make': make
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Make prediction
    prediction = pipeline.predict(input_df)[0]

    # Return result
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
