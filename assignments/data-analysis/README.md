# 📘 Assignment: Data Analysis

## 🎯 Objective

Students will learn the basics of data analysis using Python. They will load, explore, and analyze a dataset to extract meaningful insights.

## 📝 Tasks

### 🛠️ Data Loading and Exploration

#### Description
Load a provided CSV dataset and perform basic exploration to understand its structure and contents.

#### Requirements
Completed program should:

- Load the CSV file using Python (pandas library recommended)
- Display the first 5 rows of the dataset
- Show the dataset shape (number of rows and columns)
- Show summary statistics (mean, median, min, max) for all numeric columns
- Display data types for each column

#### Example
```python
import pandas as pd

# Load and explore the data
df = pd.read_csv('data.csv')
print(df.head())
print(df.shape)
print(df.describe())
print(df.dtypes)
```


### 🛠️ Data Visualization and Insights

#### Description
Create visualizations to help understand the data and analyze key findings.

#### Requirements
Completed program should:

- Generate at least two different types of plots (e.g., histogram, scatter plot, bar chart, line plot) using matplotlib or seaborn
- Add appropriate titles and axis labels to each visualization
- Identify and describe at least two insights or trends from the data (in comments or print statements)
- Save each plot as an image file (PNG format)

#### Example
```python
import matplotlib.pyplot as plt

# Create a histogram
plt.hist(df['column_name'], bins=20)
plt.title('Distribution of Column Name')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.show()

# Create a scatter plot
plt.scatter(df['column1'], df['column2'])
plt.title('Relationship between Column1 and Column2')
plt.savefig('scatter.png')
plt.show()
```
