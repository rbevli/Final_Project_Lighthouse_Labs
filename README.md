# Final_Project_Lighthouse_Labs

## Overview

This project looks into developing an app that contains two models.
- Build an efficient and accurate Toronto Home Price Predictor using Regression models.
- Build a Home Recommender System that takes an interested buyer’s preferred house characteristics as inputs and recommends the 5 closest matching homes to the Buyer. 

Through the streamlit app's UI, the user can enter the home's characteristics depending on whether they are an interested buyer or an interested seller to get a recommendation or price prediction.

The app's link: [home.io](https://rbevli-final-project-lighthouse-labs-streamlit-app-bfb9kp.streamlitapp.com/)


## Files

- Clustering_Recommender.ipynb : Contains code for KNN clustering for Recommender System
- PreProcessing_Baseline.ipynb : Data Cleaning and Pre-Processing along with KNN imputer for missing NaN Square Footage Values
- Regression_Predictor.ipynb   : Contains code for Regression Modeling, Toronto Police Crime Data Feature Engineering along with Data Exploration and Visualisation
- Toronto_neighbourhoods_data_mining.ipynb : Contains Code for Foursquare Places API Feature Engineering
- streamlit_app.py : Contains code for Final Model Pipeline which is then deployed on streamlit

## Tech Stack

Python | Regression Models | KNN | Seaborn | Pandas | SciKit-learn | NumPy | XGBoost | Foursquare Places API | GeoPandas | streamlit.io |


## Methodology

![image](https://user-images.githubusercontent.com/97575766/187054025-e3f3f376-702b-4349-8e77-302402511926.png)


## Data Exploration and Feature Engineering

Location of homes for sale in Toronto:
![image](https://user-images.githubusercontent.com/97575766/187054045-563687f9-f81b-41f6-b1d0-b4d91c6f28fe.png)


Toronto Neighbourhoods by Avg Price (CAD) :
1) Forest Hill South                    	        -   2.73 million
2) Rosedale-Moore Park                            -   2.33 million
3) Bridle Path-Sunnybrook-York Mills              -   2.32 million


Toronto Neighbourhoods by Number of Listings :
1) Waterfront Communities - The Island            -  1148   (Avg Price - 732,079 CAD)
2) Niagara  		                                  -  533    (Avg Price - 693,141  CAD)
3) Mimico 		                                    -  523    (Avg Price - 710,459  CAD)

![image](https://user-images.githubusercontent.com/97575766/187054411-b219be67-1b52-440e-aa1f-338ca183b49b.png)


## Feature Engineering & Modeling

![image](https://user-images.githubusercontent.com/97575766/187054439-23addf24-7272-4feb-b61e-c7443e08ffbc.png)


## Results and Demonstration

Regression Model improved in performance after adding Crime Statistics. The model further improved after adding neighbourhood features using the Foursquare Places API. RMSE value decreased as new features were engineered.

Clustering Model successfully recommended  most similar homes. 

Demonstration:

![image](https://user-images.githubusercontent.com/97575766/187054491-7fd1ea3a-0066-47d4-8ae6-4feb7a3d4edc.png)

![image](https://user-images.githubusercontent.com/97575766/187054565-4f3e42a7-0883-4f41-bec7-07ccbed88097.png)

![image](https://user-images.githubusercontent.com/97575766/187054584-983827d0-ad69-402c-80cb-0b5b8d43ba15.png)

![image](https://user-images.githubusercontent.com/97575766/187054599-b9f680c8-48d7-4699-b2f4-efa958b37b97.png)



## Future Goals

- Access to dates of listings so as to engineer socio-economic features such as mortgage rates, home inflation rates.
- Employ the use of Natural Language Processing do analyse the description of homes and extract useful features that are embedded in the textual description. Also employ Natural Language Processing for the recommender system so Buyers can input their preferences through a search engine.
- Remodel Regression and Clustering using Neural Networks so as to improve model performance!



