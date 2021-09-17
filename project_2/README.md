# Project 2 - Ames Housing Data and Kaggle Challenge

## Executive Summary

### Problem Statement

As data analysts at a property agency in Ames, Iowa, I are tasked with conducting statistical analysis of housing transactions in Ames to identify prominent house features which affect house prices.

I will create a regression model based on the Ames Housing Dataset. This model will predict the price of a house at sale based on the dataset which I retrieved from Kaggle.

The Ames Housing Dataset is an exceptionally detailed and robust dataset with over 70 columns of different features relating to houses and I will identify which features will best predict housing prices in Ames.

Kaggle has provided us with 2 datasets: a train.csv to train our model with and a test.csv which I will fit our model into and make housing price predictions.

Our understanding of the prominent features and price predictions will be crucial to provide advice to potential home sellers who might be considering to sell their house in Ames and would want to know what future price estimates may be so that they can adjust their ask price appropriately and market their homes effectively.

### Data Cleaning

The training dataset contains over 2000 rows and 81 columns and I needed to ensure that I had a good look at it to understand the features.
The first step was to read through the data dictionary provided on the Ames Housing data to have a sense of the types of variables within the data e.g. numerical (discrete or continuous) and categorical (nominal or ordinal) features.

After reading in the train dataset, I looked to identify the missing values. I dropped the features which had a high percentage of missing values (over one third or 33%). Although there was no missing values in the neighborhood column, a comparison with the data dictionary from Kaggle showed that there 6 rows which had neighborhoods not present in the dictionary and proceeded to drop these rows.

I then created a summary of the remaining missing values by feature and went through each feature to explore the rationale of why those null values were present. Usually, features of the same sub category like masonry veneer type and masonry veneer area would be have some form of relationship, for example if veneer area was 0 in one of the rows, I can safely assume that the veneer type of the same row would be non existent (None).

By the use of the function: value_counts(), I would also check if the null values could have been missing because they were misidentified as None or NA.

As a result of the above assumptions and thought process, I can fill these null values with 'None' or zeros.

Lot frontage feature was a column that required more thought. Based on data dictionary definition, lot frontage meant the linear feet of street connected to the property. Upon further reading, it is the horizontal distance between the sides of lot line and it shouldn't be zero. In this case, the null values were imputed with the median value.

Once the training set was cleaned with all null values accounted for, the same methodology was applied to the test set. The only difference was that I could not drop any rows for the test set as part of the Kaggle submission requirement. An example of a feature that we could not drop was the rows with incorrect data from the neighborhood column. There were 5 rows labelled 'greens' neighborhood, in this case, they were replaced with 2 (which is the median ordinal ranking) for this neighborhood feature.

## Exploratory Data Analysis

3 correlation matrix for the discrete, continuous and ordinal (converted in numerical based on ordinal ranking) variables were conducted. From here, I filtered out multi-collinearity of the features to each other and considered dropping one of them since they were correlated to each other. This was also a form of feature selection. Nominal features were more tricky and I firstly identified relationships between the categories of each features in terms of their frequency and whether there were distinctive variability of saleprice for each of the category within the feature. This also allowed us to narrow down the choice of nominal features which would be more useful as a predictor of saleprice. Finally, I utilized OneHotEncoder from sklearn's preprocessing module to create dummies for the selected nominal features.

### Preprocessing and Modeling

Of the remaining features, I did a feature engineering to aggregate all the baths together into one feature. Subsequently, train_test_split was done to the training set to split it into a smaller training set and a validation set. Since we are predicting the saleprice in our test set and the saleprice column is non-existent, having a validation set gives our model the opportunity to occasionally *see* the data but never learn from it.

Since Kaggle explicitly stated that root mean square error will be used for grading, I made sure that my models were evaluated using RMSE for the training and validation sets.

3 models were used:
1. Linear regression
2. Lasso regression
3. Ridge regression

For all 3 models, cross validation was done to ensure a more conservative average of our R-square scores. The optimal alphas for both Lasso and Ridge were used when running the models which penalizes the coefficients of features which are not very useful. This allows the model to be more optimized for better saleprice prediction.


### Model Evaluation

In summary, all 3 models performed relatively similarly but the Lasso regression performed the best with the lowest RMSE on the validation set.

- RMSE for Lasso Regression on validation set: 31,916
- RMSE for Ridge Regression on validation set: 32,142
- RMSE for Linear Regression on validation set: 32,260


### Takeaways and Recommendations

Based on the Lasso coefficients, these are the top 10 features identified to be most useful. They have the strong coefficient positive score:

1. Overall quality
2. Above ground living area
3. Neighborhood
4. Kitchen quality
5. 1st floor square feet
6. Masonry veneer aggregate
7. Basement exposure
8. Basement finish square feet type 1
9. Garage area
10. Fireplaces

The bottom 5 features which were zero-ed out by Lasso were:
1. Year built
2. Basement condition
3. Electrical
4. 2nd floor square feet
5. Garage condition

For potential home sellers looking to put up their homes for sale, I would recommend:

1. Taking note of which neighborhood their homes are located in
2. Consider increasing livable space especially first floor and garage area within their homes by engaging some remodelling works
3. Consider increasing the number of rooms (excluding bathrooms) by converting excess space within the house into an additional study room or guest bedroom. This can potentially increase its valuation  
