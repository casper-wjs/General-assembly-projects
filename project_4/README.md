# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) West Nile Virus Prediction across the city of Chicago

## Problem Statement

Due to the recent epidemic of West Nile Virus in the Windy City, the Department of Public Health set up a surveillance and control system to help collect data on mosquito numbers, West Nile Virus appearance, and weather events.

As part of the Disease And Treatment Agency, division of Societal Cures In Epidemiology and New Creative Engineering (DATA-SCIENCE), we have been tasked to assess the viability of the current spray model, as well as to try and predict occurrence of West Nile Virus in Chicago by training classifier models. This will further refine the current pest management model.

<a href = 'https://www.preventivepestcontrol.com/weather-affect-mosquito-activity/'> Mosquitoes enjoy wet and warm climates and are most active in temperatures above 80 degrees</a>. Conversely, when temperatures go below 50 degrees, mosquitoes go dormant.  

Mosquito lifecycles for Culex Pipiens, the most common mosquito caught in Chicago, <a href='https://www.in.gov/health/erc/zoonotic-and-vectorborne-epidemiology-entomology/pests/culex-species-mosquitoes/'>typically range from 2-4 weeks, and even less than a week in the heat of summer</a>.

Our project will seek to:

1. Determine the effectiveness of sprays on the mosquito population
2. Predict the occcurence of West Nile Virus
3. Help provide guidelines by which to apply future sprays
4. Conduct a cost benefit analysis on the use of the pesticides in response to the epidemic

After training on the classifier models, the selection of the best model will be guided by the Precision, Recall, ROC-AUC and PR score on the validation set.

## Contents
* Data import, helper functions, cleaning and imputation of missing values
* EDA: Previewing Data and Highlighting Outliers
* Modelling
* Applying our selected model on the Kaggle test set
* Cost-Benefit Analysis and Conclusion

## Executive Summary
This project aims to find try and predict the presence of West Nile Virus within mosquitoes using various classification models, to assess the viability and effectiveness of the spray model employed in 2011 and 2013, and thereafter conduct a cost-benefit analysis on the use of sprays. 

Initial analysis showed some columns with completely missing, or mostly trace data, such as `water1`, `depth` and `snowfall`. As number of mosquitoes per row were capped at 50, the records were summed up to get the total number of mosquitoes into 1 record. Imputation of missing values were done by adding the mean difference between both stations, to the station with available values.

Presence of West Nile Virus were mostly found in Culex Pipiens and Culex Restuans species. There were notably higher numbers of mosquitoes caught when relating with certain weather phenomena, such as mist, drizzle or rain. Temperature correlating with specific times of the year were also found to promote the number mosquitoes caught. This suggests that the pooling of stagnant water sources after such weather conditions, in addition to temperatures during specific seasons of the year, contributed to increased breeding and growth of mosquitoes. 

The spray data provided, however, did not prove to be very effective as the sprays were always conducted <b>after</b> the mosquitoes were caught. Although the traps are scattered and collected every week only from Monday through Wednesday, sprays, which are only effective on the day sprayed, were mostly conducted on Thursdays. Hence, they did not provide most correlation to the mosquito population post-spray.

A few features were engineered additionally, such as the lag of days, ranking of traps based on mosquitoes caught, to improve predictive power for our classification models. The dataset is severely imbalanced due to only a small set of being present with West Nile Virus. We utilised SMOTE, a statisical technique which helps to increase the number of samples in a balanced way. Ultimately, the logistic regression classification model was found to have the best PR-AUC score, with a kaggle result of 0.71124.

With regards to cost-benefit analysis and conclusions, please refer to their individual sections below.


## Dataset

The dataset, along with description, can be found here: [https://www.kaggle.com/c/predict-west-nile-virus/](https://www.kaggle.com/c/predict-west-nile-virus/).


* [`train.csv`](./assets/train.csv): Training set consists of data from 2007, 2009, 2011, and 2013.
* [`test.csv`](./assets/test.csv): Test set consists of data required to predict results for 2008, 2010, 2012, and 2014.
* [`weather.csv`](./assets/weather.csv): Weather data from 2007 to 2014 of 2 stations
* [`spray.csv`](./assets/spray.csv): GIS data of spraying efforts in 2011 and 2013

### Data Dictionary
You can access the data dictionary, split into markdown format [*here*](https://github.com/kkhalis/project_4/blob/master/DataDictionary.md).

You can also access the detailed description of weather info in the Data Dictionary [*here*](https://github.com/kkhalis/project_4/blob/master/assets/noaa_weather_qclcd_documentation.pdf)

## Project Planning
Project Plan Documentation can be found [*here*](https://docs.google.com/spreadsheets/d/1_o3eWrHmSxif5hHflbAwt84u0uXwgWTV/edit#gid=540275792).

## Cost-Benefit Analysis

In effective pest management, one should consider the use of different spray types and effectiveness, as well as factors influencing the lifecycle of the pest.

When considering only fogging, the typical spray used in residential areas for combating mosquitos, timing of the spray should be strongly considered in reducing a mosquito population due to its time-constrained effectiveness:
1. Timing of rainfall
* Rainfall can have a large impact on the population of mosquitos, with stagnant, trapped water providing fertile breeding ground. In built-up cities such as Chicago, it can be difficult to get rid of all water traps and to completely eliminate sources of stagnant water. Use of fogging 8-10 days after a heavy downpour can be a timely way to eliminate mosquito populations for the day, as they are hatching, and accurately target the spray to its window of maximum effectiveness.

* Spray use should also be avoided when the timing coincides with predictions of rainfall on the day itself. For maximum effectiveness, sprays would have to remain in the air and interact with the mosquito population. Any precipitation during the course of the day would reduce the effectiveness of the spray by taking it out of the air and preventing maximum exposure.

2. Degree Days
* Mosquitos have shown to be most active around a specific temperature band, above 65F, often measured in degree days. When judging appropriate spray effectiveness, degree days can be used to help judge the use and timing of sprays. More days consistently above the 65F band would lead to a faster lifecycle, and a more active population, requiring a more consistent use of spraying. In contrast, we may avoid spraying on cooler days due to the limited effectivness of spraying, particularly when the mosquito population is small. Targeted use specifically in areas that have historically had the West Nile Virus presence can be considered instead.
* In examining our spray data set, sprays have largely been applied in September. This might be one big area of improvement for future spray applications, to shift them towards the summer months, when mosquitos are most active.

3. Wind Speed and Drift
* Wind speed should also be considered on the day of application. Wind speed can cause pesticide drift, removing the pesticide fog from its most effective location. Wind speed of the day should be considered during pesticide application. This is especially important in Chicago, which follows a grid layout, allowing buildings to form wind corridors and exacerbating wind effects.
* Conversely, days with no wind speed can be difficult for spray operators, at speeds below 3km/h, spray can evaporate before arriving at the desired destination of application. A light breeze will provide the operator with the knowledge of the pesticide drift.

4. Sprayer Type
* Sprayer machinery can play an important role in the application of pesticides. A fine nozzle sprayer will help to provide a fine dispersion of the pesticide mist, however, hot days and lower humidity can lead to a faster evaporation of smaller droplets. Conversely, larger particle sizes (>200 microns) may survive the heat and be less affected by wind size, but may not be as effective at delivering the pesticide to pests.

5. Pesticide
* The assumption made is that the spray used is the most commonly use spray for fogging the air and targeting adult mosquitoes. However, standing pesticides can also be used in conjunction with air pesticides, targeting difficult to reach or difficult to clear areas with standing water to eliminate mosquito larvae. This would be a far more long-reaching solution, although constant re-application would be required through each rainfall. Therefore, consideration would have to be given according to the frequency of rainfall and the difficulty of application.

### Model 1

#### Costs

1. Spraying

- [Time of spray](https://www.chicago.gov/city/en/depts/cdph/provdrs/healthy_communities/news/2020/august/city-to-spray-insecticide-thursday-to-kill-mosquitoes.html): Weather permitting, the spraying will begin at dusk on August 13th and continue through the night until approximately 1:00 am, with licensed mosquito abatement technicians in trucks dispensing an ultra-low-volume spray. The material being used to control the adult mosquitoes, Zenivex.


- [Spray rate of Zerivex](https://chicago.cbslocal.com/2017/08/30/spray-mosquitoes-far-south-side-west-nile-prevention/): The chemical used is Zenivex, applied at a rate of 1.5 fluid ounces per acre. That measure is approved by the U.S. EPA to control mosquitoes in outdoor residential and recreational areas.


- [Zerivex cost per acre](https://www.centralmosquitocontrol.com/-/media/files/centralmosquitocontrol-na/us/resources-lit%20files/zenivex%20cost%20comparison%20fact%20sheet.pdf): USD0.67 per acre

- Area of Chicago City: estimated to be 145,300 acres based on Google Search

Based on the above, we assume the cost of spray to be USD 0.67 per acre multiplied by the area of Chicago city, which would be at USD $97,351. This accounts for 1 spraying exercise.

If we assume the most aggressive spray strategy and spray every week during the summer months of July, August and September based on our spray effectiveness analysis, then the total cost can be calculated to be USD 1,168,212.

For this scenario, we would need to set aside a budget of about USD 1.17 million to conduct the spraying exercises on an annual basis.

2. Medical Health Costs

- Patients who were hospitalized with acute flaccid paralysis, a partial- to whole-body paralysis caused by WNV infection, had the largest initial and long-term medical costs ([median USD 25,000 and USD 22,000 respectively](https://www.sciencedaily.com/releases/2014/02/140210184713.htm)).


- Number of [human WNV cases](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7241786/) in Chicago region (refer to Table 2): 24 in 2011 and 66 in 2013


- The [CDC site](https://www.cdc.gov/westnile/index.html) shares that while there are no vaccines to prevent or medications to treat WNV in people, about 1 in 5 people who are infected develop a fever and other symptoms and about 1 out of 150 infected people develop a serious, sometimes fatal, illness.  


#### Benefits

In a maximum benefit scenario, we assume that due to our aggressive spraying policy, no one contracted the virus.

Conversely, in a scenario where the spray had not been used, we will use the following costs:

Medical Health Costs - USD 60

  - Number of [human WNV cases](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7241786/) in Chicago region will be taken as the average of cases from 2007-2014 (same as our dataset), without the years of 2011 and 2013, to determine maximal benefit against a programme with no spraying

  - The [CDC estimates](https://www.sciencedaily.com/releases/2014/02/140210184713.htm):
     - Roughly 4 out of 5 people are asymptomatic
     - 1 in 5 people who are infected develop a fever, with a median medical cost of USD 7,500
     - 1 in 150 infected people develop a serious, sometimes fatal, illness incurring long-term median medical costs of a total of USD 47,000.

The medical costs for symptomatically mild to moderate cases are 60/5 * 7500 = USD 90000.0.
The medical costs for symptomatically severe cases, rounding up, are USD 47000.

The total medical costs are USD 137,000

Productivity Loss

Based on [NCBI(National Centre for Biotechnology Information)'s study in determining productivity loss of an individual](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322011/) , we assume productivity loss to be (referenced from Table 3 in the link):

For the symptomatically mild and moderate cases:
- USD 955 for each individual, for a total of USD 11460


For the hospitalised individual:
- USD 10800, if the individual is under the age of 60

Total productivity loss: USD 22260
The economic loss to WNV can be calculated as USD 159,260.

### Model 2

In our second model, we look to target specific areas of the city, highly affected by the mosquitos, along with the following factors:

- Spray Area: Spray Area imputed from the spray area of the 2011 spray block, an area roughly measuring 12.857 km^2, or 3177 acres.

- Spray Times: Following the EDA done on the weather data set, alongside the features that were deemed to be of the highest importance in the logistic regression, we can see that spraying can be targeted to hit the life cycle of mosquitos immediately after periods that are:
    1. At least 10 days after a light rain or mist event
    2. On days where the degree day value is 7 or higher
    
Assuming this happens 3 times a month (Every 10 days of uninterupted sunshine following a rain event), and only in the months correlated with the highest number of cases (August, September), we can lower spray frequency to 6 times a year.

Further, from our EDA, only 18 of the 64 blocks in the train set had WNV counts above 10 for the last 4 years, more than 2.5 cases per year per block.

Therefore, we would restrict our spraying to only the regions that would benefit the most.

At a rate of:
* 6 sprays a year
* For 18 blocks * 3177 acres * USD 0.67 per acre

The total cost of Model 2 would be USD 229887.72

At USD 230,000, this spray plan is remains higher than the loss estimated of USD 159,260.

## Recommendations

In conclusion, while a model that included indiscriminate spraying through Chicago did not show material benefit when compared to the cost, a model that was calculated based on initial features discovered during EDA and examined after modeling did product a spray plan that was more expensive than the economic loss estimated.

This model was however based on a worst case scenario of 6 sprays. When adjusted by the weather for the year, it will likely reduce the reliance of such a high spray count. Further streamlining of the model could be done by looking at the month of June as a lead up, to help determine the severity of the mosquito population for the year.

That said, the [best and most economical way](https://www.cdc.gov/westnile/prevention/index.html) to prevent West Nile disease or any other mosquito-borne illness is likely education of the populace, to reduce the number of mosquitoes. Precautions recommended by the CDC include:

- When outdoors, apply insect repellent that contains DEET, picaridin, oil of lemon eucalyptus or IR 3535, according to label instructions.
- Wear long-sleeved shirts and long pants when going out
- Make sure doors and windows have tight-fitting screens. Repair or replace screens that have tears or other openings. Try to keep doors and windows shut, especially at night.
- Eliminate sources of water-holding containers that can support mosquito breeding such as tires, buckets, planters, toys, pools, birdbaths, flowerpots, or trash containers
- In communities where there are organized mosquito control programs, contact your municipal government to report areas of stagnant water in roadside ditches, flooded yards and similar locations that may produce mosquitoes.

## Conclusion
Some things to consider in a follow-up model or test sets, would include data on the following:
- Use models with class weights. This will penalise the misclassifications made by the minority class by setting a higher class weight , and at the same time, reducing weight for the majority class. Penalising mistakes will put more emphasis on the misclassifed class.
- Consider other approaches in dealing with imbalanced classification, such as ADASYN
- Collect more data to balance classes within the dataset.


Presentation slides can be found [*here*](https://docs.google.com/presentation/d/1mcq-PWQ7iOgGA75zJQiJCC4yx7CGViAl/edit?usp=sharing).