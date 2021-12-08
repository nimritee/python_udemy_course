import pandas
from collections import defaultdict


# Function to delete duplicate rows from a dataframe
def del_duplicate(dataframe):
    return dataframe.drop_duplicates()


#Function will identify and return all missing value index and its class
def identify_missing_values(dataframe,attribute):
    missing_array = defaultdict(list) # Creating a dictionary, with list as its value
    radius_index = dataframe.index[dataframe[attribute] == 0].tolist()
    for indexes in radius_index:
        if missing_array[dataframe['Fruit (class)'][indexes]]:
            missing_array[dataframe['Fruit (class)'][indexes]].append(indexes)
        else:
            missing_array[dataframe['Fruit (class)'][indexes]] = [indexes]
    return missing_array


# Function will find the mean of the missing value using mean of its class
def generate_mean(dataframe,missing_data,attribute):
    final_data ={}
    for fruit_class,indexes in missing_data.items():
        index_data = dict(map(reversed, enumerate(indexes))) # Create a dictionary with keys of all list values
        #Find the mean of the attribute for a particular class, removing all the NaN and the missing index
        mean = dataframe[attribute].where(dataframe['Fruit (class)'] == fruit_class).dropna().drop(indexes).mean() 
        index_data = dict.fromkeys(indexes,mean) # Update all the keys, with the mean value
        final_data = final_data | index_data # Merge the final_data dictionary with index_data dictionary
    return final_data


# Update the dataframe with the given values
def substitute_values(dataframe,data_values,attribute):
    for key,value in data_values.items():
        dataframe.loc[key,attribute]=value
    return dataframe


# Function to fill missing values (fields that have 0) with the mean of the corresponding class of the attribute
def fill_values(og_dataframe):
    dataframe = og_dataframe.copy() # Making a copy of the dataframe passed
    attributeArray = ['Radius (cm)','Weight (grams)']
    for attribute in attributeArray:
        missing_data = identify_missing_values(dataframe,attribute) #To identify all the missing values for the particular attribute
        generated_data = generate_mean(dataframe,missing_data,attribute) #Find the mean of the missing values of the same class
        dataframe = substitute_values(dataframe,generated_data,attribute) #Update the dataframe values, with the values found
    return dataframe


# Function to transform the Colour column into green,yellow and red, by adding 1 if its True for that row and the rest 0
def transform_nominal(og_dataframe):
    dataframe = og_dataframe.copy() # Making a copy of the dataframe passed
    attribute_values = og_dataframe['Colour'].unique() # Getting unique values from the Column
    for column in attribute_values: # Creating Columns of all the unique value
        dataframe[column] = 0 
    for index, row in dataframe.iterrows():
        dataframe.loc[[index],[row['Colour']]]=1
    dataframe = dataframe.drop('Colour',axis=1) #To drop the Colour column
    return(dataframe)


# Function to normalise the values of each numerical attribute with min-max method
def normalise_minmax(og_dataframe):
    dataframe = og_dataframe.copy() # Making a copy of the dataframe passed
    numerical_attribute = ['Radius (cm)','Weight (grams)']
    for column in numerical_attribute: # apply normalization techniques
        dataframe[column] = (dataframe[column] - dataframe[column].min()) / (dataframe[column].max() - dataframe[column].min())    
    return dataframe


dataframe = pandas.read_csv("ML_assignment02_dataset_2021.csv") #Load the given dataset using pandas

noDuplicateSample = del_duplicate(dataframe) #To delete duplicate samples
print("Dataframe after deleting duplicate sample: \n\n {} \n".format(noDuplicateSample))
noDuplicateSample.to_csv('no_duplicate.csv')

fillValues = fill_values(dataframe) #To fill missing values
print("Dataframe after filling missing values (fields that have 0) with the mean of the corresponding class: \n\n{} \n ".format(fillValues))
fillValues.to_csv('no_missing_value.csv')

transformData = transform_nominal(dataframe) # To transform nominal attributes into numerical values
print("Dataframe after transforming nominal attributes into numerical values: \n\n {} \n".format(transformData))
transformData.to_csv('nominal_transformation.csv')

minMaxData = normalise_minmax(dataframe) # To normalise the values of each numerical attribute with min-max method
print("Dataframe after normalising the values of each numerical attribute with min-max method: \n\n {} \n".format(minMaxData))
minMaxData.to_csv('normalise_minmax.csv')