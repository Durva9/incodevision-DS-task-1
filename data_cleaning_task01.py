# ==========================================
# Task 01: Data Cleaning and Preprocessing
# ==========================================

import pandas as pd
import numpy as np

# ------------------------------------------
# Step 1: Load the Dataset
# ------------------------------------------
df = pd.read_csv("task01_raw_employee_data.csv")

print("Original Dataset:")
print(df)
print("\nDataset Info:")
print(df.info())

# ------------------------------------------
# Step 2: Identify Missing Values
# ------------------------------------------
print("\nMissing Values Count:")
print(df.isnull().sum())

# ------------------------------------------
# Step 3: Handle Missing Values
# ------------------------------------------

# Fill missing Age with median (ignore non-numeric values)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"].fillna(df["Age"].median(), inplace=True)

# Fill missing Salary with mean
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Fill missing Name with 'Unknown'
df["Name"].fillna("Unknown", inplace=True)
df["Name"].replace("", "Unknown", inplace=True)

# ------------------------------------------
# Step 4: Remove Duplicate Records
# ------------------------------------------
df.drop_duplicates(inplace=True)

# ------------------------------------------
# Step 5: Fix Inconsistent Text Data
# ------------------------------------------

# Standardize Name formatting
df["Name"] = df["Name"].str.title()

# Standardize Department names
df["Department"] = df["Department"].str.upper()

# ------------------------------------------
# Step 6: Fix Date Format
# ------------------------------------------
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"], errors="coerce")

# ------------------------------------------
# Step 7: Fix Data Types
# ------------------------------------------
df["Age"] = df["Age"].astype(int)
df["Salary"] = df["Salary"].astype(float)

# ------------------------------------------
# Step 8: Final Clean Dataset
# ------------------------------------------
print("\nCleaned Dataset:")
print(df)

print("\nCleaned Dataset Info:")
print(df.info())

# ------------------------------------------
# Step 9: Save Cleaned Dataset
# ------------------------------------------
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nCleaned data saved as 'cleaned_employee_data.csv'")
