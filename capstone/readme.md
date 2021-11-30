# Capstone Project - Predicting HDB Resale Prices in Singapore using Regression Models and Neural Networks

Model deployed on [Heroku](https://hdb-model.herokuapp.com/)

## Executive Summary

### Problem Statement

Due to Covid and the presence of lockdowns which has affected public housing project delays in Singapore, HDB resale prices has been steadily increasing and has become a common discussion topics especially amongst first time young buyers.

I am curious to find out what features influence HDB resale prices and help potential buyers find out if the current asking prices of HDBs are reasonable by using regression models to predict HDB prices.

The increasing cost of living comes to mind for young Singaporeans looking to purchase a home and start a family. This model would serve a guide for them as part of their home purchase decision making process.

Regression models for consideration: Linear, Lasso, Ridge, Random Forest, ExtraTrees, XGBoost, Neural Networks

Success Metrics: Model performance will be guided by RMSE. We will seek to find the best performing model based on the lowest RMSE score.

Data source from [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices)

From the csv files downloaded, we extracted over 200,000 rows of HDB transactions for the 10-year period from Oct 2011 to Oct 2021.

### Data Cleaning

Fortunately, the data downloaded from the government website was very clean and there was not much cleaning to do. The only thing I did was drop columns like 'remaining_lease' which was not very useful as we already have 'lease_commencement_date'. We also made the assumption to only analyze HDB apartment unit types and dropped rows relating to HDB terrace house transactions, albeit it was not many.

### Feature engineering

Feature engineering was an important aspect for this project as we did not have many feature columns from the initial dataset. Considering that this is a real estate prediction project, I wanted to create new features relating to distance of nearby amenities. Therefore, using the OneMap API, I scrapped for geo coordinates of the HDB transactions as well as coordinates of amenities such as MRT stations, schools, mall and CBD. Using a customized function, I calculated the distance of all nearby amenities and added them as additional features.

Other features added included:
- year transacted (this can be pulled from the month column which includes the month and year of transaction date)
- age (calculated by taking current year 2021 minus lease commencement date)
- inflation adjusted resale price (using Singapore's historical inflation data to adjust the prices accordingly to 2021's value)
- price per sqf (taking nominal prices divided by HDB area)
- floor area in sqf (the housing market in Singapore more commonly uses sqf instead of sqm as a comparison metric)
- storey (the initial data provided a floor range for each transaction. We will convert it into numbers by taking the average of the range of numbers

### Exploratory Data Analysis

Histogram and correlation matrices were done to compare the numerical features.

We also create a variety of time series plots to look at:
- overall median HDB resale price
- number of transactions by flat type
- median resale price by flat type
- median floor area sqf by flat type
- price per square foot by town

Additionally, we leveraged the interactive features of Tableau Public to add additional data visualization. The link can be found [here](https://public.tableau.com/app/profile/casper.wong/viz/HDB_16339564614480/HDBResalePriceAnalysis).

### Preprocessing and Modeling

Categorical features were dummified using OneHotEncoder. Additionally, we created a dummified year column to account for inflationary effects and dummified the time (month) column to add in [fixed effects](https://are.berkeley.edu/courses/EEP118/current/handouts/eep118_panel_data_fixed_effects.pdf) to account for unforeseen time based macro factors which influenced HDB prices (for example: unexpected cooling measures in 2013, Covid in 2020).

Our baseline model will use the mean of resale prices in the train set as the predictor of sale prices in the test set.

This resulted in a train RMSE of 144,232 and test RMSE of 142,975 and will be the minimum score to beat.

The following models were trained:
1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. Random Forest Regressor
5. ExtraTrees Regressor
6. XG Boost Regressor
7. Feed forward Neural Network
   - Vanilla model
   - with Batch Normalization
   - with Weight Decay
   - with Dropout

### Model Evaluation

In summary, we note the following:

- Linear regression and Ridge regression performed closely with similar test RMSE
- On the other hand, Lasso regression performed worse compared to the above 2
- Overall, ensemble methods performed better
- Unique to pricing related data, I realize that for tree based models, you would not want to train your trees which are too deep as it will overfit on the training data
- We also note that the runtime for training XG Boost is much faster compared to Random Forest regression
- For tree-based models, note that the more number of trees within the model, the longer the runtime. Therefore we would want to be conscious of the time spent tuning these models.
- When there is too many trees to be run, there is a risk of memory error. Personally, the threshold for my computer was when I was trying to run 400 trees on Gridsearch
- Surprisingly, Neural Networks (NN) were trained much faster than Random Forest and XGBoost, however did not perform as well. This may point to the fact that deep learning may not always be the best choice.
- Every run of NN is subjected to a portion of randomness. These randomness can be due to random initialization of weights and bias or randomness in regularization like dropouts
- Using RMSE as our guiding metric, XG Boost regression is the best model with the lowest test RMSE score

This may be due to the fact that it is a form of gradient boosting whereby the objective is to minimize the loss function of the model by adding weak learners using gradient descent. Gradient descent is an iterative optimization algorithm for finding a local minimum of differentiable function. As weak learners train on the remaining residual errors of a strong learner, it gives more importance and concentration to observations with high errors.

### Feature Importance

Using our best model (XG Boost) to interpret the feature importance:

1. Overall, we had more physical housing features such as flat type and flat model, followed by location based features like the town in which the HDB apartments were found in. Interestingly, a feature like floor area did not make it onto the list.

2. Specifically, flat types like executive, 2-room, 3-room and 5-room were in the top 5 features. Flat types generally would correlate with the area of the apartments and made logical sense to be present in the list.

3. We noticed that towns located in the central part of Singapore made it into the list (with the exception of Woodlands), which plays into the perception that well located real estate would greatly influence its price.

3. Interestingly, proximity to nearest mall was the only distance based feature making into the list, which meant that proximity to malls had a greater influence in price than proximity to schools and mrt stations.

4. age correlates negatively with price and it is unsurprising that it is a top ranking features. Furthermore, considering that HDBs are leasehold in nature, it would be natural that people would want to buy newer flats, thus an important feature

### Conclusion

Singapore's HDB resale market generally goes through several property cycles. Although not collected within the dataset for this project, a quick Google search would show that HDB resale saw a price boom in the 90s as Singapore's economy was developing rapidly. It ended in the late 90s when the Asian Financial Crisis happened. The 2000s saw some price stagnation in the first half of the decade and quickly accelerated in the second half.

The model's predictive capacity is subjected to macro factors and policy changes which sometimes can be unforeseen and cause sharp changes in price trend.
Most recently, the government just announced new policies to curb 'lottery effects' of well placed HDB BTO projects and and make public housing more equitable: Prime Location Public Housing (PLH) model.

Going forward, these PLH projects will be subjected to more stringent measures at the point of resale.
For example: longer minimum occupation period would likely mean that there would less speculation. BTO applicants would likely be people who are more serious about long term house ownership and not using HDB as a stepping stone to cash out and upgrade to private housing

### Next Steps/how we can improve

- Retrain model with a larger dataset (use more historical HDB resale transactions)
- Continue to retune our models' hyperparameters for better results
- As an expansion of the project, I can collect private residential condo transactions and test our models' predictive capability
- We will try to use Flask to deploy our model online to allow users to input some HDB features and see a price estimate as a guide for their HDB home purchase decision (Update: Model is deployed on [Heroku](https://hdb-model.herokuapp.com/))
