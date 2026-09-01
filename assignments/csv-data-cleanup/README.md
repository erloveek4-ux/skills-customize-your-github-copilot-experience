# 📘 Assignment: CSV Data Cleanup Challenge

## 🎯 Objective

Students will learn how to read CSV data, clean messy values, and create a simple report from real-world spreadsheet data. This assignment introduces practical data handling skills without requiring advanced libraries.

## 📝 Tasks

### 🛠️ Load and Inspect the Dataset

#### Description
Read a CSV file and inspect its structure before making any changes.

#### Requirements
Completed program should:
- Open the provided CSV file using Python
- Read the column names and row count
- Print the first 5 rows of data
- Identify whether any values are missing or contain extra spaces

#### Example
```python
import csv

with open('data.csv', newline='') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

print(reader.fieldnames)
print(len(rows))
print(rows[:2])
```

### 🛠️ Clean the Data

#### Description
Fix common problems in CSV data such as extra whitespace, blank values, and values stored as strings instead of numbers.

#### Requirements
Completed program should:
- Strip leading and trailing spaces from text values
- Convert numeric fields to integers or floats when appropriate
- Replace blank values with a sensible default such as `0` or `"Unknown"`
- Save the cleaned data to a new CSV file named `cleaned_data.csv`

#### Example
```python
for row in rows:
    row['name'] = row['name'].strip()
    row['score'] = int(row['score']) if row['score'] else 0
```

### 🛠️ Create a Summary Report

#### Description
Summarize the cleaned dataset so it is easier to understand at a glance.

#### Requirements
Completed program should:
- Calculate the average score
- Find the highest and lowest scores
- Count how many students are missing a value in a field
- Print a short summary report to the console

#### Example
```python
scores = [int(row['score']) for row in rows]
print(f"Average score: {sum(scores) / len(scores):.2f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
```
