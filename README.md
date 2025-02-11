# Fraud-detection

## Project Overview

This project involves analyzing and preprocessing transaction data, creating new features that highlight fraud patterns, and building machine learning models that can detect fraud in real-time. Once the models are developed, they will be evaluated and fine-tuned for optimal performance, after which they will be deployed for continuous monitoring and improvement.

## Key Tasks

### Task 1 - Data Analysis and Preprocessing

1. **Handle Missing Values:**

   - Impute or drop missing values as appropriate.

2. **Data Cleaning:**

   - Remove duplicates.
   - Correct data types.

3. **Exploratory Data Analysis (EDA):**

   - Perform univariate and bivariate analysis.

4. **Merge Datasets for Geolocation Analysis:**

   - Convert IP addresses to integer format.
   - Merge `Fraud_Data.csv` with `IpAddress_to_Country.csv`.

5. **Feature Engineering:**

   - Calculate transaction frequency and velocity from `Fraud_Data.csv`.
   - Extract time-based features such as `hour_of_day` and `day_of_week`.

6. **Normalization and Scaling:**

   - Normalize and scale the features for model building.

7. **Encode Categorical Features:**
   - Convert categorical variables to numerical format.

### Task 2 - Model Building and Training

1. **Data Preparation:**

   - Separate features and target variables for both datasets (`creditcard.csv` and `Fraud_Data.csv`).
   - Split the data into training and testing sets.

2. **Model Selection:**

   - Train and evaluate multiple models, including:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - Gradient Boosting
     - Multi-Layer Perceptron (MLP)
     - Convolutional Neural Network (CNN)
     - Recurrent Neural Network (RNN)
     - Long Short-Term Memory (LSTM)

3. **Model Training and Evaluation:**
   - Train the models and evaluate their performance using metrics such as precision, recall, F1-score, and accuracy.

### MLOps Steps

1. **Versioning and Experiment Tracking:**
   - Use tools like MLflow to track experiments, log parameters, metrics, and version models.

## Data and Features

### 1. **Fraud_Data.csv** (E-Commerce Transaction Data)

- `user_id`: Unique identifier for the user making the transaction.
- `signup_time`: Timestamp of when the user signed up.
- `purchase_time`: Timestamp of the transaction.
- `purchase_value`: Value of the transaction in dollars.
- `device_id`: Unique identifier for the device used for the transaction.
- `source`: Source through which the user accessed the site (e.g., SEO, Ads).
- `browser`: Browser used for the transaction (e.g., Chrome, Safari).
- `sex`: Gender of the user (M = Male, F = Female).
- `age`: Age of the user.
- `ip_address`: IP address of the user making the transaction.
- `class`: Target variable (1 = Fraud, 0 = Non-Fraud).

### 2. **IpAddress_to_Country.csv** (IP Address to Country Mapping)

- `lower_bound_ip_address`: Lower bound of the IP address range.
- `upper_bound_ip_address`: Upper bound of the IP address range.
- `country`: The country corresponding to the IP address range.

### 3. **creditcard.csv** (Bank Transaction Data)

- `Time`: Elapsed time between this transaction and the first transaction in the dataset.
- `V1 - V28`: Anonymized features representing underlying patterns from PCA transformation.
- `Amount`: Transaction amount in dollars.
- `Class`: Target variable (1 = Fraud, 0 = Non-Fraud).

## Model Deployment and Monitoring

Once the models are trained and evaluated, they will be deployed for real-time fraud detection in e-commerce and banking systems. The deployment process will include setting up an API endpoint for the fraud detection service and monitoring model performance in production. Additionally, continuous learning will be set up to improve the models over time.

## Technologies Used

- **Data Processing:** pandas, numpy
- **Machine Learning Models:** Scikit-learn, TensorFlow/Keras
- **Geolocation Mapping:** IP address conversion
- **Model Tracking:** MLflow
- **Visualization:** Matplotlib, Seaborn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Semir1r/Fraud-detection.gitt
   cd Fraud-detection
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
