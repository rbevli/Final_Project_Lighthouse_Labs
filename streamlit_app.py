#import libraries
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV


st.header('Welcome! Are you an interested Buyer/Seller of a Toronto Home?')
img = Image.open("./resources/logo.png")
st.image(img)


#recommender using KNN code block
def recommender(data):
    
    #import 
    df = pd.read_csv("houses_cleaned_baselineKNN_crimedata_foursquare.csv", index_col = 0)
    X = df[['bathrooms', 'parking', 'type','final_price',
        'Neighbourhood','bedroom', 'den', 'sqft']]

    
    X_test = pd.DataFrame(data, columns=['bathrooms', 'parking', 'type', 'final_price', 'Neighbourhood',
       'bedroom', 'den', 'sqft'])
    
    X = X.append(X_test,ignore_index = True)
    
    preprocessor = ColumnTransformer(transformers=[
        ('onehot', OneHotEncoder(), ['type','Neighbourhood']),
        ('scaler', MinMaxScaler(), ['bathrooms', 'parking','final_price',
                                    'bedroom', 'den', 'sqft'])])

    
    X_processed = preprocessor.fit_transform(X)

    # fit nearest neighbours
    nbrs = NearestNeighbors(n_neighbors = 5)
    nbrs.fit(X_processed)

    distances, indices = nbrs.kneighbors(X_processed)
    
    def print_similar(id):
        df_return = pd.DataFrame()
        for id in indices[id][1:]:
            df_return = df_return.append(df.iloc[id])
        return df_return[['final_price','description','full_address','full_link','bedroom','bathrooms','den','sqft','parking','Neighbourhood']]
    
    return print_similar(X.index[-1])


# predictor using regression
def predictor(data):
    
    df = pd.read_csv("houses_cleaned_baselineKNN_crimedata_foursquare.csv", index_col = 0)


    #load model
    file3 = open("best_KNN_test_joblib.pickle",'rb')
    model_joblib = joblib.load(file3)
    

    X = df[['bathrooms', 'parking', 'type',
       'Neighbourhood','bedroom', 'den', 'sqft','mean_district_income',
     'Assault_Rate','Auto_Theft_Rate','Break_andEnter_Rate','Robbery_Rate',
       'Shootings_Rate','Restaurant','Bus_Stops','Parks','Schools',
             'Entertainment_Services','Shopping_Plazas','Hospitals']]
    
    cols = ['mean_district_income','Assault_Rate','Auto_Theft_Rate','Break_andEnter_Rate','Robbery_Rate',
       'Shootings_Rate','Restaurant','Bus_Stops','Parks','Schools',
             'Entertainment_Services','Shopping_Plazas','Hospitals','Neighbourhood']

    x_test = pd.DataFrame(data, columns=['bathrooms', 'parking', 'type', 'Neighbourhood',
       'bedroom', 'den', 'sqft'])

    x_test = pd.merge(x_test, X[cols], on = ['Neighbourhood'], how = 'inner')
    
    return model_joblib.predict(x_test)


def buyer():

    st.header('Buyer House Recommender')
    st.header('Welcome! Please enter your desired home features')

    bathrooms = st.slider('Enter the number of bathrooms you would like:', 1, 1, 20)
    bedroom = st.slider("Number of bedrooms you're looking for:", 1, 1, 20)
    den = st.slider('Enter the number of dens you would like:', 0, 1, 20)
    parking = st.slider('How many number of parking spots would you like?', 0, 1, 20)

    type = st.selectbox(
    "What is the type of house you're looing for?",
    ('Condo Apt',
    'Condo Townhouse',
    'Comm Element Condo',
    'Detached',
    'Semi-Detached',
    'Att/Row/Twnhouse',
    'Co-Op Apt',
    'Co-Ownership Apt',
    'Plex',
    'Link',
    'Store W/Apt/Offc')) 
    Neighbourhood = st.selectbox('Enter the Neighbourhood you would like your house in:',
    ('Agincourt North',
    'Agincourt South-Malvern West',
    'Alderwood',
    'Annex',
    'Banbury-Don Mills',
    'Bathurst Manor',
    'Bay Street Corridor',
    'Bayview Village',
    'Bayview Woods-Steeles',
    'Bedford Park-Nortown',
    'Beechborough-Greenbrook',
    'Bendale',
    'Birchcliffe-Cliffside',
    'Black Creek',
    'Blake-Jones',
    'Briar Hill-Belgravia',
    'Bridle Path-Sunnybrook-York Mills',
    'Broadview North',
    'Brookhaven-Amesbury',
    'Cabbagetown-South St.James Town',
    'Caledonia-Fairbank',
    'Casa Loma',
    'Centennial Scarborough',
    'Church-Yonge Corridor',
    'Clairlea-Birchmount',
    'Clanton Park',
    'Cliffcrest',
    'Corso Italia-Davenport',
    'Danforth',
    'Danforth East York',
    'Don Valley Village',
    'Dorset Park',
    'Dovercourt-Wallace Emerson-Junction',
    'Downsview-Roding-CFB',
    'Dufferin Grove',
    'East End-Danforth',
    'Edenbridge-Humber Valley',
    'Eglinton East',
    'Elms-Old Rexdale',
    'Englemount-Lawrence',
    'Eringate-Centennial-West Deane',
    'Etobicoke West Mall',
    'Flemingdon Park',
    'Forest Hill North',
    'Forest Hill South',
    'Glenfield-Jane Heights',
    'Greenwood-Coxwell',
    'Guildwood',
    'Henry Farm',
    'High Park North',
    'High Park-Swansea',
    'Highland Creek',
    'Hillcrest Village',
    'Humber Heights-Westmount',
    'Humber Summit',
    'Humbermede',
    'Humewood-Cedarvale',
    'Ionview',
    'Islington-City Centre West',
    'Junction Area',
    'Keelesdale-Eglinton West',
    'Kennedy Park',
    'Kensington-Chinatown',
    'Kingsview Village-The Westway',
    'Kingsway South',
    "L'Amoreaux",
    'Lambton Baby Point',
    'Lansing-Westgate',
    'Lawrence Park North',
    'Lawrence Park South',
    'Leaside-Bennington',
    'Little Portugal',
    'Long Branch',
    'Malvern',
    'Maple Leaf',
    'Markland Wood',
    'Milliken',
    'Mimico (includes Humber Bay Shores)',
    'Morningside',
    'Moss Park',
    'Mount Dennis',
    'Mount Olive-Silverstone-Jamestown',
    'Mount Pleasant East',
    'Mount Pleasant West',
    'New Toronto',
    'Newtonbrook East',
    'Newtonbrook West',
    'Niagara',
    'North Riverdale',
    'North St.James Town',
    "O'Connor-Parkview",
    'Oakridge',
    'Oakwood Village',
    'Old East York',
    'Palmerston-Little Italy',
    'Parkwoods-Donalda',
    'Pelmo Park-Humberlea',
    'Playter Estates-Danforth',
    'Pleasant View',
    'Princess-Rosethorn',
    'Regent Park',
    'Rexdale-Kipling',
    'Rockcliffe-Smythe',
    'Roncesvalles',
    'Rosedale-Moore Park',
    'Rouge',
    'Runnymede-Bloor West Village',
    'Rustic',
    'Scarborough Village',
    'South Parkdale',
    'South Riverdale',
    'St.Andrew-Windfields',
    'Steeles',
    'Stonegate-Queensway',
    "Tam O'Shanter-Sullivan",
    'Taylor-Massey',
    'The Beaches',
    'Thistletown-Beaumond Heights',
    'Thorncliffe Park',
    'Trinity-Bellwoods',
    'University',
    'Victoria Village',
    'Waterfront Communities-The Island',
    'West Hill',
    'West Humber-Clairville',
    'Westminster-Branson',
    'Weston',
    'Weston-Pellam Park',
    'Wexford/Maryvale',
    'Willowdale East',
    'Willowdale West',
    'Willowridge-Martingrove-Richview',
    'Woburn',
    'Woodbine Corridor',
    'Woodbine-Lumsden',
    'Wychwood',
    'Yonge-Eglinton',
    'Yonge-St.Clair',
    'York University Heights',
    'Yorkdale-Glen Park'))
    final_price = st.slider("Enter the rough price you're looking for?",300000, 20000, 10000000)   
    sqft = st.slider("What size are you looking for?",400, 100, 10000)
   

    
    if st.button('Get Recommendations!'):

        data = [[bathrooms, parking, type, final_price, Neighbourhood,bedroom, den, sqft]]
        
        returned_df = recommender(data)
        
        st.dataframe(returned_df).style.hide_index()
        # st.write('These are the recomendations: ',value, bedroom)

def seller():
    st.header('Seller Price Predictor')
    st.header('Welcome! Please enter your desired home features')


    """
    Describe your house
    """
    bathrooms = st.slider('Enter the number of bathrooms in your home:', 1, 1, 20)
    bedroom = st.slider("Enter the number of bedrooms in your home:", 1, 1, 20)
    den = st.slider('Enter the number of dens in your home:', 0, 1, 20)
    parking = st.slider('Enter the number of parking spots in your home:', 0, 1, 20)

    type = st.selectbox(
    "What is the type of home you own?",
    ('Condo Apt',
    'Condo Townhouse',
    'Comm Element Condo',
    'Detached',
    'Semi-Detached',
    'Att/Row/Twnhouse',
    'Co-Op Apt',
    'Co-Ownership Apt',
    'Plex',
    'Link',
    'Store W/Apt/Offc')) 
    Neighbourhood = st.selectbox('Enter the Neighbourhood of your home:',
    ('Agincourt North',
    'Agincourt South-Malvern West',
    'Alderwood',
    'Annex',
    'Banbury-Don Mills',
    'Bathurst Manor',
    'Bay Street Corridor',
    'Bayview Village',
    'Bayview Woods-Steeles',
    'Bedford Park-Nortown',
    'Beechborough-Greenbrook',
    'Bendale',
    'Birchcliffe-Cliffside',
    'Black Creek',
    'Blake-Jones',
    'Briar Hill-Belgravia',
    'Bridle Path-Sunnybrook-York Mills',
    'Broadview North',
    'Brookhaven-Amesbury',
    'Cabbagetown-South St.James Town',
    'Caledonia-Fairbank',
    'Casa Loma',
    'Centennial Scarborough',
    'Church-Yonge Corridor',
    'Clairlea-Birchmount',
    'Clanton Park',
    'Cliffcrest',
    'Corso Italia-Davenport',
    'Danforth',
    'Danforth East York',
    'Don Valley Village',
    'Dorset Park',
    'Dovercourt-Wallace Emerson-Junction',
    'Downsview-Roding-CFB',
    'Dufferin Grove',
    'East End-Danforth',
    'Edenbridge-Humber Valley',
    'Eglinton East',
    'Elms-Old Rexdale',
    'Englemount-Lawrence',
    'Eringate-Centennial-West Deane',
    'Etobicoke West Mall',
    'Flemingdon Park',
    'Forest Hill North',
    'Forest Hill South',
    'Glenfield-Jane Heights',
    'Greenwood-Coxwell',
    'Guildwood',
    'Henry Farm',
    'High Park North',
    'High Park-Swansea',
    'Highland Creek',
    'Hillcrest Village',
    'Humber Heights-Westmount',
    'Humber Summit',
    'Humbermede',
    'Humewood-Cedarvale',
    'Ionview',
    'Islington-City Centre West',
    'Junction Area',
    'Keelesdale-Eglinton West',
    'Kennedy Park',
    'Kensington-Chinatown',
    'Kingsview Village-The Westway',
    'Kingsway South',
    "L'Amoreaux",
    'Lambton Baby Point',
    'Lansing-Westgate',
    'Lawrence Park North',
    'Lawrence Park South',
    'Leaside-Bennington',
    'Little Portugal',
    'Long Branch',
    'Malvern',
    'Maple Leaf',
    'Markland Wood',
    'Milliken',
    'Mimico (includes Humber Bay Shores)',
    'Morningside',
    'Moss Park',
    'Mount Dennis',
    'Mount Olive-Silverstone-Jamestown',
    'Mount Pleasant East',
    'Mount Pleasant West',
    'New Toronto',
    'Newtonbrook East',
    'Newtonbrook West',
    'Niagara',
    'North Riverdale',
    'North St.James Town',
    "O'Connor-Parkview",
    'Oakridge',
    'Oakwood Village',
    'Old East York',
    'Palmerston-Little Italy',
    'Parkwoods-Donalda',
    'Pelmo Park-Humberlea',
    'Playter Estates-Danforth',
    'Pleasant View',
    'Princess-Rosethorn',
    'Regent Park',
    'Rexdale-Kipling',
    'Rockcliffe-Smythe',
    'Roncesvalles',
    'Rosedale-Moore Park',
    'Rouge',
    'Runnymede-Bloor West Village',
    'Rustic',
    'Scarborough Village',
    'South Parkdale',
    'South Riverdale',
    'St.Andrew-Windfields',
    'Steeles',
    'Stonegate-Queensway',
    "Tam O'Shanter-Sullivan",
    'Taylor-Massey',
    'The Beaches',
    'Thistletown-Beaumond Heights',
    'Thorncliffe Park',
    'Trinity-Bellwoods',
    'University',
    'Victoria Village',
    'Waterfront Communities-The Island',
    'West Hill',
    'West Humber-Clairville',
    'Westminster-Branson',
    'Weston',
    'Weston-Pellam Park',
    'Wexford/Maryvale',
    'Willowdale East',
    'Willowdale West',
    'Willowridge-Martingrove-Richview',
    'Woburn',
    'Woodbine Corridor',
    'Woodbine-Lumsden',
    'Wychwood',
    'Yonge-Eglinton',
    'Yonge-St.Clair',
    'York University Heights',
    'Yorkdale-Glen Park'))
    sqft = st.slider("Enter the square footage of your home:",400, 100, 10000)
   
    
    if st.button('Get Home Price Prediction!'):
        data = [[bathrooms, parking, type, Neighbourhood,bedroom, den, sqft]]
        
        returned_price = predictor(data)
        
        st.write('Your home is valued at CAD ',returned_price[0])

col1, col2 = st.columns([1,1])

buyer_btn = False
seller_btn = False

st.subheader('Are you a buyer or seller?')
page = st.selectbox('',['Buyer','Seller']) 

if page=='Buyer':
    buyer()
elif page=='Seller':
    seller()
