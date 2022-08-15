from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from random import randint
from PIL import Image

img = Image.open("./resources/logo.png")

st.image(img)

st.header('Welcome! Are you interested in getting a price prediction for your Toronto home?')


def buyer():

    st.header('Buyer House Recommender')
    bathroom = st.slider('Enter the number of bathrooms you would like:', 1, 1, 20)
    parking = st.slider('How many number of parking spots would you like?', 0, 1, 20)
    type = st.selectbox(
    "What is the type of house you're looing for?",
    ('Villa', 'Condo', 'Appartment', 'Mansion')) 
    district = st.text_input('Enter the city you would like your house in:')

    bedroom = st.slider("Number of bedrooms you're looking for:", 1, 1, 20)
    den = st.slider('Enter the number of dens you would like:', 1, 1, 20)
    size = st.slider("What size are you looking for?",400, 100, 400000)   

    if st.button('Get Recomendations!'):
        value = randint(0, 10)
        st.write('These are the recomendations: ',value, bedroom)

def seller():
    st.header('Seller Price Predictor')

    """
    Describe your house
    """
    bathroom = st.slider('Enter the number of bathrooms:', 1, 1, 20)
    parking = st.slider('How many number of parking spots fo you have?', 0, 1, 20)
    type = st.selectbox(
    "What is the type of your house?",
    ('Villa', 'Condo', 'Appartment', 'Mansion')) 
    district = st.text_input('Enter the city in which you have your house')

    bedroom = st.slider("Number of bedrooms", 1, 1, 20)
    den = st.slider('Enter the number of dens', 1, 1, 20)
    size = st.slider("What's the size?",400, 100, 400000)
    if st.button('Get Recomendations!'):
        value = randint(0, 10)
        st.write('These are the recomendations: ',value, bedroom)

col1, col2 = st.columns([1,1])

buyer_btn = False
seller_btn = False

st.subheader('Are you a buyer or seller?')
page = st.selectbox('',['Buyer','Seller']) 

if page=='Buyer':
    buyer()
elif page=='Seller':
    seller()
