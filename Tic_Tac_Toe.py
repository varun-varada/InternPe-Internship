# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
file_path = r'C:\Users\varun\OneDrive\Desktop\Vs_code\python\diabeties.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Data Preprocessing
# Handle missing values by replacing zeros with NaN
df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)

# Fill missing values with the median of each column
df.fillna(df.median(), inplace=True)

# Exploratory Data Analysis (EDA)
# Plot the distribution of each feature
df.hist(bins=10, figsize=(12, 10))
plt.show()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Feature Selection
X = df.drop('Outcome', axis=1)  # Features
y = df['Outcome']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Building (Decision Tree Classifier)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Display confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

print(classification_report(y_test, y_pred))

# Predicting with new data (example)
new_data = np.array([[2, 120, 70, 20, 85, 30.0, 0.5, 25]]) 
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)
print(f'Prediction for the new data: {"Diabetic" if prediction[0] == 1 else "Non-diabetic"}')

# Predicting with input_data
input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

# Convert input_data to numpy array and reshape for prediction
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

# Standardize the input data using the same scaler
std_data = scaler.transform(input_data_as_numpy_array)

# Make prediction
prediction = model.predict(std_data)

if prediction[0] == 0:
    print('The person is not diabetic.')
else:
    print('The person is diabetic.')
