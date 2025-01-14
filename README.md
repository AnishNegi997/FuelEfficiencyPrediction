# Fuel Efficiency Prediction 🚗

## 📝 Project Overview
This project predicts the fuel efficiency of vehicles based on various features such as fuelType, cylinders, fuelCost and more. It leverages machine learning algorithms to provide accurate and reliable predictions, aiding in better decision-making for vehicle manufacturers and consumers.

## 🌟 Features
- Predicts fuel efficiency using machine learning models.
- Supports multiple algorithms: Random Forest, Linear Regression, and KNN.
- Includes data preprocessing and feature engineering for optimal model performance.
- Exploratory Data Analysis (EDA) for insights into the dataset.

## 🛠️ Tech Stack
- Programming Language: Python
- Web Framework: Flask
- Machine Learning: scikit-learn, pandas, numpy
- Data Visualization: matplotlib, seaborn

## ⚙️ Setup Instructions
### Clone the repository:
```bash
git clone https://github.com/your-username/fuel-efficiency-prediction.git
cd fuel-efficiency-prediction
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the application:
```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000`.

## 🗃️ Dataset
The dataset used for this project contains information about vehicle characteristics and their fuel efficiency. Key attributes include:

- fuelCost
- engine Size
- Miles per gallon (MPG)

**Source:** https://www.fueleconomy.gov/feg/download.shtml

## 🔍 Exploratory Data Analysis
In this section, we perform various steps of Exploratory Data Analysis (EDA) to better understand the relationships between features and gain insights into the dataset.

1. Correlation Analysis:
We calculated the correlation matrix using the .corr() method to identify the relationships between numeric features.
Insight: We observed a negative correlation between engine size and MPG (miles per gallon), indicating that as engine size increases, fuel efficiency tends to decrease.

3. Correlation Heatmap:
A heatmap was generated to visualize the correlation between features.
Insight: The heatmap clearly showed important relationships, such as the negative correlation between engine size and MPG and the positive correlation between co2 and engine size.

5. Distribution of MPG Values:
The distribution of the target variable MPG was plotted using a histogram.
Insight: The distribution of MPG was right-skewed, suggesting that most vehicles in the dataset have lower fuel efficiency.

7. Scatter Plots for Feature Relationships:
Engine Size vs. co2
MPG vs. Engine Size
Insight: The scatter plots confirmed that larger engines are associated with lower fuel efficiency.

9. Handling Missing Data:
We checked for missing values in the dataset.
Action: Missing values were either imputed or rows with too many missing values were removed.

11. Feature Engineering:
Feature Selection: Unnecessary columns were dropped as they didn't contribute to predicting fuel efficiency.
Log Transformation: A log transformation was applied to the engineSize feature to improve its distribution.

13. Outlier Detection:
Box plots were used to detect outliers in features like co2 and fuelCost.
Action: Outliers were detected and handled to ensure they didn’t skew the model.

15. Pairplot of Features:
A pairplot was used to visualize relationships between key features such as fuelCost, co2, and MPG.

## 🧠 Model Details
- **Random Forest**: High accuracy, good for handling non-linear relationships.
- **Linear Regression**: Simple, interpretable model for linear relationships.
- **KNN**: Effective for small datasets with clear patterns.

## 🚀 Results
- **Model accuracy**: R²: 0.9998, Mean Absolute Error (MAE): 0.0039

## 🎯 Future Scope
- Extend the project to predict other vehicle parameters.
- Integrate real-time data from APIs.
- Deploy the app on a cloud platform like AWS or Heroku.

## 🛠️ Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact
Feel free to reach out via Email or connect on LinkedIn.
