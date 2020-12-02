# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:21:27 2020

@author: maria
"""
import pandas as pd

def data_processing(df):
    '''
    This function takes in the pandas dataframe and does processing,
    and returns the processed dataframe.
    '''
        # drop duplicated rows
    df.drop_duplicates(('description', 'title'), inplace=True)
    # drop rows with missing prices
    df[pd.notnull(df.price)]
    
    # Imputing missing values
    for col in ('region_2', 'designation', 'taster_twitter_handle', 'taster_name', 'region_1'):
        df[col]=df[col].fillna('Unknown')
        
    #Inputting the missing province with the mode
    df['province'] = df['province'].fillna(df['province'].mode())
    # Inputing missing price with the mean
    df['price'] = df['price'].fillna(df['price'].mean())
    
    return df