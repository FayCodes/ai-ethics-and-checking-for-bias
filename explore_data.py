import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('compas-scores-two-years.csv')

print("=== COMPAS Dataset Exploration ===")
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

print("\n=== Race Column Analysis ===")
print("Unique values in 'race' column:")
print(df['race'].value_counts())
print(f"\nData type: {df['race'].dtype}")

print("\n=== Sex Column Analysis ===")
print("Unique values in 'sex' column:")
print(df['sex'].value_counts())
print(f"\nData type: {df['sex'].dtype}")

print("\n=== Two Year Recidivism Analysis ===")
print("Unique values in 'two_year_recid' column:")
print(df['two_year_recid'].value_counts())
print(f"\nData type: {df['two_year_recid'].dtype}")

print("\n=== Sample of key columns ===")
key_columns = ['race', 'sex', 'age', 'priors_count', 'decile_score', 'two_year_recid']
print(df[key_columns].head(10)) 