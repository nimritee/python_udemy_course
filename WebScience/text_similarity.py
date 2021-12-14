import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')
import re
from collections import Counter
import numpy as np
from numpy.linalg import norm


frequency_list= []

# Function to clean and tokenize the data
def data_cleaning(lines_of_files):
    line= ""
    for l in lines_of_files:
        l = l.rstrip("\n")
        line = line + " " +l

    line= re.sub(r'[^\w\s]','',line) # Remove special characters and punctuations from text
    formatted_line= re.sub('\s\s+',' ',line) # Remove extra spaces from text
    pattern= '[' + ''.join(['α','β']) + ']' # Remove some unnecessary symbols from text
    lines_without_symbols= re.sub(pattern,'',formatted_line)
    lines_without_numbers= re.sub(r'[0-9]+','',lines_without_symbols) # Remove numbers from text
    cleaned_data= re.sub(r'[A-Z]+',lambda x: x.group(0).lower(),lines_without_numbers)
    return cleaned_data

def perform_tokenize_data(data):
    tokenized_words =[]
    text_document ={}

    for doc,words in data.items():
        words= nltk.word_tokenize(words) # Split strings into tokens (nominally words) 
        if words== []:
            continue
        else:
            tokenized_words.extend(words)
            text_document[doc] = tokenized_words
            tokenized_words =[]
    return text_document

def data_preprocessing():
    text_document ={}
    document_list = ["Text_0.txt","Text_1.txt","Text_2.txt"]
    for item in document_list:
        with open(item) as file: 
            file_data = file.readlines()
        
        text_document[item] = data_cleaning(file_data)
    return text_document

# Function to get unique words from the pair of docs
def get_unique_words(doc1,doc2):
  for i in tokenize_data.values():
     frequency_list.append(Counter(i))
  
  words_doc1 = set(doc1) 
  words_doc2 = set(doc2)
  union_data=  words_doc1.union(words_doc2)
  return union_data
  
#Function to calculate cosine similarity between two documents
def cosine_similarity(doc1,doc2,doc1_index,doc2_index):
  vector1= [] 
  vector2= []
  data= get_unique_words(doc1,doc2)
  for i in list(data):
    vector1.append(frequency_list[doc1_index][i])
    vector2.append(frequency_list[doc2_index][i])
  
  calculated_cosine_similarity= np.dot(vector1,vector2)/(norm(vector1)*norm(vector2))  
  return calculated_cosine_similarity

# Function to calculate the Jaccard Score
def jaccard_score(doc1,doc2):

    # Find the unique words in a document
    words_doc1 = set(doc1) 
    words_doc2 = set(doc2)

    # Compute the intersection of words list of doc1 & doc2
    intersection_data= words_doc1.intersection(words_doc2)

    # Compute the union of words list of doc1 & doc2
    union_data = words_doc1.union(words_doc2)

    # Jaccard Score  = Length of intersection set / Length of union set
    return float(len(intersection_data)) / len(union_data)

# Function to calculate Euclidean Distance between two documents
def euclidean_distance(doc1,doc2,doc1_index,doc2_index):
  vector_euclid1= []
  vector_euclid2= []
  data= get_unique_words(doc1,doc2)
  for i in list(data):
    vector_euclid1.append(frequency_list[doc1_index][i])
    vector_euclid2.append(frequency_list[doc2_index][i])
  
  calculated_euclid_distance= norm(np.array(vector_euclid1)- np.array(vector_euclid2))  
  return calculated_euclid_distance


data= data_preprocessing()
document_pairs = ['Text_0.txt,Text_1.txt','Text_0.txt,Text_2.txt','Text_1.txt,Text_2.txt']
document_indexes= {'Text_0.txt':0, 'Text_1.txt':1, 'Text_2.txt':2}
tokenize_data = perform_tokenize_data(data)

for pairs in document_pairs:
    doc1,doc2=pairs.split(",")

    # Calculating the Jaccard Score 
    calculated_jaccard_score = jaccard_score(tokenize_data[doc1],tokenize_data[doc2])
    print("\nThe Jaccard Similarity Score between {} and {} is:{} \n".format(doc1,doc2,calculated_jaccard_score))

    # Calculating the Cosine Similarity 
    calculated_cosine_similarity = cosine_similarity(tokenize_data[doc1],tokenize_data[doc2],document_indexes[doc1],document_indexes[doc2])
    print("The Cosine Similarity Score between {} and {} is:{} \n".format(doc1,doc2,calculated_cosine_similarity))

    # Calculating the Euclidean Distance 
    calculated_euclidean_distance = euclidean_distance(tokenize_data[doc1],tokenize_data[doc2],document_indexes[doc1],document_indexes[doc2])
    print("The Euclidean distance Score between {} and {} is:{} \n".format(doc1,doc2,calculated_euclidean_distance))