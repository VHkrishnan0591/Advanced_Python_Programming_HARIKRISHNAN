# **House Price Prediction Presentation**

## Overview
This folder contains the presentation of the Advanced House Price Prediction presented during the summer semester 2024 for the course of Advanced Programming in THD Cham Campus.

The presemtation covers the prediction of House price prediction using various algorithms done in two of its version 1 and version 2 with version 1 uses Lasso feature selection method and version 2 focusses on Mutual Information theory feature selection.

Now comparing the two version of the problem and inferring the mean square error is less for the version 1 of using lasso feature selection.

---
# **Detailed Description**

## Data:

- The dataset set has 81 columsn and 1460 rows with dependent variable as 'Sale Price' which needs to be predicted.

## Exploratory Data Analysis:
 - Understanding the missing values for categorical and numerical features
 - Relationship between null values and dependent variable 'SalesPrice'
 - Finding the unique values in feature with numerical value
 - Breaking down variables with numerical values as discrete and categorical
 - Finidng the realtionship between discrete features and Sale Price
 - Analyse the continuous values by creating histograms to understand the distribution
 - Finding the correlation between the features
 - Checking for Outliers
 - Finding the number of categorical variable and relation between Sale Price

 ## Feature Engineering
 - Replace missing value with a new label called missing as the missing values are not missing by random manner
 - Replacing the numerical Missing Values using median
 - Handling Date Time Variables
 - In Version 1 we use Log transform and Version 2 we use square root transform
 - Handling Rare Categorical values
 - Encoding for the ordinal categorical feature (Target Guided Encoding)
 - Encoding for the nominal categorical variable (Mean Encoding)
 - Removing the outliers

 ## Feature Selection
 - Lasso feature selection is performed in Version 1 and Mutual Information gain feature selection in Version 2

 ## Model Training
 - Test Train Split is performed
 - Feature Scaling is performed using MInMax Scaler
 - Linear Regression, Polynomial Regression, Support Vector Regression, Decison tree and Randomn Forrest are the algorithm are used and their performance are evaluated

 ## Performance Metrics
 - The model are evaluated using Adjusted R2 and R2 score and Mean square error is also considered
 - Inferring the version 1 and version 2 results the mean square error is less in version 1 and Linear regression and Support vector machine performs well with a less mean error

---
# Installation Instructions

- Install the Anaconda IDE <https://www.anaconda.com/download>

 ---

 # Plugins and Libraies Used
  - Python Version - 3.12.4
  - Anaconda for Windows
  - Jupyter Notebook
  - GitHub for Windows
  - Git for Windows
  - Pandas
  - Numpy
  - seaborn
  - Matploib
  - pylab
  - scklearn
---
# Coding Practises Followed
- The variables are given meaningful names which truly represent the context of the problem
- Clear and explainable comments are added 
- The variable name follow the **Snake Case** naming convention.
- Following is the below code example for the practises followed
---
# Authors
 - [VHkrishnan0591](https://github.com/VHkrishnan0591)