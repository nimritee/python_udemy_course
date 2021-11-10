import pandas
import numpy as np

def del_duplicate(df):
    delete_df = df.drop_duplicates()
    return delete_df

def fill_values(df):
    df_copy = df.copy() 
    cols = ["Weight (grams)","Radius (cm)"]
    df_copy[cols] = df_copy[cols].replace({'0':np.nan, 0:np.nan})
    df_copy['Weight (grams)'] = df_copy['Weight (grams)'].fillna(df_copy.groupby('Fruit (class)')['Weight (grams)'].transform('mean'))
    df_copy['Radius (cm)'] = df_copy['Radius (cm)'].fillna(df_copy.groupby('Fruit (class)')['Radius (cm)'].transform('mean'))
    return df_copy
  
def transform_nominal(df):
    df_copy = df.copy() 
    df_copy['green']= 0
    df_copy['yellow'] =0
    df_copy['red'] = 0
    for index, row in df_copy.iterrows():
        if row['Colour'] == 'Red':
            df_copy.loc[index,'red']=1
        elif row['Colour'] == 'Green':
            df_copy.loc[index,'green']=1
        else:
            df_copy.loc[index,'yellow']=1
    df_copy = df_copy.drop('Colour', 1)
    return(df_copy)

def normalise_minmax(df):
    df_copy = df.copy() 
    df_copy['Weight (grams)'] = (df_copy['Weight (grams)'] - df_copy['Weight (grams)'].min()) / (df_copy['Weight (grams)'].max() - df_copy['Weight (grams)'].min())    
    df_copy['Radius (cm)'] = (df_copy['Radius (cm)'] - df_copy['Radius (cm)'].min()) / (df_copy['Radius (cm)'].max() - df_copy['Radius (cm)'].min()) 
    return df_copy

df = pandas.read_csv("ML_assignment02_dataset_2021.csv") 

delete_df = del_duplicate(df)
print("The output after deleting duplicate samples: \n",delete_df)
delete_df.to_csv('delete.csv')

fill_df = fill_values(df) 
print("The output after misisng values with mean of their coressponding class: \n",fill_df)
fill_df.to_csv('fill.csv')

transform_df = transform_nominal(df) 
print("The output after transforming nominal attributes into numerical values: \n",transform_df)
transform_df.to_csv('nominal.csv')

minmax_df = normalise_minmax(df) 
print("The output after normalising the values of each numerical attribute with min-max method: \n", minmax_df)
minmax_df.to_csv('minmax.csv')