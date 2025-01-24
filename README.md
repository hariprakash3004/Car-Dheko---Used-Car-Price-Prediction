# Car Dheko - Used Car Price Prediction

## Overview
This project focuses on building a machine learning model to predict used car prices based on various features such as mileage, engine size, transmission type, and more. The model is integrated into a Streamlit app, enabling users to input car details and receive price predictions instantly. The app also provides data insights through visualizations like mileage distribution and correlation heatmaps.

---

## Features
### 1. Data Cleaning & Preprocessing
- **Handling Missing Values and Outliers:** 
  - Imputed missing numerical values using the mean and categorical values with the mode.
  - Outliers were handled using IQR (Interquartile Range) .
- **Encoding Categorical Data:** 
  - Applied One-Hot Encoding for nominal features (e.g., fuel type, body type).
  - Used Label Encoding for ordinal features (e.g., engine type, seating capacity).
- **Scaling Numerical Features:** 
  - Standardized features using Standard Scaling techniques.

### 2. Feature Engineering
- **Feature Extraction:** 
  - Derived useful features like mileage, torque, car dimensions, and engine specifications.
- **Statistical Tests:**
  - **Chi-Square Test:** Analyzed relationships between categorical features and car price.
  - **ANOVA Test:** Compared means of numerical features like mileage against car price.
  - **Correlation Matrix & Heatmap:** Visualized relationships between numerical features like mileage, torque, and price.
  - **Low Variance Threshold:** Removed features with minimal variance to improve efficiency.

### 3. Exploratory Data Analysis (EDA)
- Conducted univariate, bivariate, and multivariate analyses to uncover important data patterns.
- Created plots like scatter plots, histograms, box plots, and heatmaps to visualize trends and relationships.

### 4. Model Training
- Trained multiple regression models:
  - **XGBoost Regressor**
  - **Random Forest Regressor**
  - **Linear Regression**
  - **Decision Tree Regressor**

- **Hyperparameter Tuning:** Performed grid search for optimizing model performance.
- **Cross-Validation:** Ensured robustness and minimized overfitting.

### 5. Evaluation Metrics
Models were evaluated based on:
- **Mean Squared Error (MSE):** Measures the average squared difference between predicted and actual prices.
- **Mean Absolute Error (MAE):** Captures the average absolute difference between predicted and actual prices.
- **R-squared (R²):** Indicates the variance in car price explained by the model.

---

### 6. App Features

**Allows users to input car specifications to predict the price interactively:**
- Body Type: Dropdown menu to select the car's body type (e.g., Convertibles, SUVs).
- Number of Seats: Dropdown menu to specify the seating capacity.
- Model Year: Dropdown menu to choose the car's manufacturing year.
- Kilometers Driven: Numeric input field to enter the total distance the car has traveled.
- Fuel Type: Dropdown menu to select the type of fuel (e.g., Petrol, Diesel, CNG).
- Number of Previous Owners: Dropdown menu to indicate the number of past owners.
- Transmission Type: Dropdown menu to select the car's transmission type (e.g., Automatic, Manual).
- Insurance Status: Dropdown menu to choose the type of insurance (e.g., Comprehensive).
- OEM (Original Equipment Manufacturer): Dropdown menu to select the car brand (e.g., Audi).
- Gear Box: Numeric input to specify the number of gears.
- Mileage (km/l): Numeric input to enter the car's fuel efficiency.
- Drive Type: Dropdown menu to choose the drivetrain (e.g., 4WD).
- City: Dropdown menu to specify the car's location (e.g., Bangalore).
Outputs an estimated car price based on the provided specifications.
Displays a relevant car image based on the selected details, enhancing user engagement.

---
## Installation
Follow these steps to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/car-dheko-price-prediction.git

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

   
### Data Preprocessing

**Missing Value Handling:** 
Missing values were imputed using the mode for categorical variables and mean for numerical ones.

**Encoding Categorical Data:**
One-Hot Encoding for non-ordinal categorical features like fuel type, body type, transmission, etc.
Label Encoding for ordinal categorical features such as engine type, number of cylinders, seating capacity, etc.

**Feature Selection**
Correlation Matrix & Heatmap: The relationships between numerical features like mileage, torque, length, and price were visualized using a correlation matrix to identify strong correlations and multicollinearity.

**Model Training**
Several regression models were trained and tested:

**XGBoost Regressor:** Known for its performance on tabular data, this model was one of the top-performing models for car price prediction.

**Random Forest Regressor:** An ensemble method that combines predictions from multiple decision trees to produce more accurate results.

**Linear Regression:** A basic approach that assumes a linear relationship between features and the target variable.

**Decision Tree Regressor:** A model that splits the data into different branches based on feature values.

**Hyperparameter** tuning was performed for all models to optimize performance, and the models were evaluated using cross-validation to avoid overfitting.

### Evaluation Metrics

The models were compared using the following metrics:

**Mean Squared Error (MSE):** Measures the average squared difference between the predicted and actual prices.
**Mean Absolute Error (MAE):** Captures the average absolute difference between predicted and actual prices.
**R-squared (R²):** Indicates the proportion of the variance in the target variable that is explained by the input features.

### Model Performance

**XGBoost Regressor**
**RMSE:** 434,041.70
**R-squared:** 0.9369

### Streamlit App
The Streamlit app was developed to make the model accessible to users for predicting car prices interactively. The app has the following features:
      - Users can input details like fuel type, transmission, mileage, engine size, and more.
      - Based on the inputs, the model predicts the car price.

   ![Screenshot 2024-11-09 135928](https://github.com/user-attachments/assets/4579cde0-8851-4f67-ae8a-a42a8119bf68)


  ![Screenshot 2024-11-09 140029](https://github.com/user-attachments/assets/b0ef29c2-ff50-49d7-9f18-a618ff2e666e)

### File Descriptions
**app.py:** Contains the Streamlit app logic.
**models/:** Trained models, scalers, and encoders.
**data/:** Raw and processed datasets.
**requirements.txt:** Lists the Python libraries required for the project.
**notebooks/:** Jupyter notebooks used for data exploration and model training.

### Contributors
 **Name:** HARIPRAKASH .N
For queries, email me at your **hariprakash3004@gmail.com**

