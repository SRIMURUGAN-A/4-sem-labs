# Import necessary libraries
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator, K2Score, HillClimbSearch
from pgmpy.inference import VariableElimination

# Load the dataset
file_path = 'processed.cleveland.data'  # Replace with your actual file path
column_names = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 
    'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
]
data = pd.read_csv(file_path, names=column_names)

# Preprocess the data
data = data.replace('?', pd.NA).dropna().astype(float)

# Binarize the target variable (presence of heart disease)
data['target'] = (data['target'] > 0).astype(int)

# Create a Bayesian Network
model = BayesianNetwork([
    ('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('sex', 'chol'),
    ('cp', 'target'), ('trestbps', 'target'), ('chol', 'target'), 
    ('fbs', 'target'), ('restecg', 'target'), ('thalach', 'target'),
    ('exang', 'target'), ('oldpeak', 'target'), ('slope', 'target'),
    ('ca', 'target'), ('thal', 'target')
])

# Train the model using Maximum Likelihood Estimation
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Perform inference
inference = VariableElimination(model)

# Example query: Probability of heart disease given certain conditions
query_result = inference.query(variables=['target'], evidence={
    'age': 63, 'sex': 1, 'cp': 3, 'trestbps': 145, 'chol': 233, 
    'fbs': 1, 'restecg': 0, 'thalach': 150, 'exang': 0, 'oldpeak': 2.3, 
    'slope': 0, 'ca': 0, 'thal': 1
})
print(query_result)

# Evaluate the model (you can use cross-validation and other metrics)
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
test_data = test_data.copy()

y_true = test_data['target']
y_pred = []

for _, row in test_data.iterrows():
    evidence = row.drop('target').to_dict()
    result = inference.map_query(variables=['target'], evidence=evidence)
    y_pred.append(result['target'])

accuracy = accuracy_score(y_true, y_pred)
print(f'Accuracy: {accuracy:.2f}')
