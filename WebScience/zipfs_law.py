import pandas as pd
import nltk
import matplotlib.pyplot as plt
import re

#Tokenizer to divide a text into a list of sentences
nltk.download('punkt')

#Read the text file
corpus_file= open('Text_3.txt','r')

#Read lines of file seperately 
lines_of_file= corpus_file.readlines()

tokenized_words=[]

#Function to clean and tokenize the text
def tokenized_text(lines_of_files):
  for line in lines_of_files:
    
    #Remove special characters and punctuations from text
    line= re.sub(r'[^\w\s]','',line)
    #Remove extra spaces from text
    formatted_line= re.sub('\s\s+','',line)
    #Remove some unnecessary symbols from text
    pattern= '[' + ''.join(['α','β']) + ']'
    lines_without_symbols= re.sub(pattern,'',formatted_line)
    #Remove numbers from text
    lines_without_numbers= re.sub(r'[0-9]+','',lines_without_symbols)
    #Convert the text into lowercase
    lowercase_lines= re.sub(r'[A-Z]+',lambda x: x.group(0).lower(),lines_without_numbers)
    #Split strings into tokens (nominally words) 
    words= nltk.word_tokenize(lowercase_lines.strip())
    #Storing the tokenized result in a list
    if words== []:
      continue
    else:
      tokenized_words.extend(words)

tokenized_text(lines_of_file)

#Remove all the alphabets present in the list of tokenized words
alphabets=[]
for i in range(98,123):
  alphabets.append(chr(i))
for j in tokenized_words:
  if j in alphabets:
    tokenized_words.remove(j)

#Organise the collected data into a dataframe
data= {'Words': tokenized_words}
df= pd.DataFrame(data)

#Create a dataframe with the frequency count of each word, arranged in a descending order
data1=df['Words'].value_counts().rename_axis('Words').reset_index(name='counts')

#Calculate the rank of the word according to their frequency
data1['rank']= data1['counts'].rank(ascending=False)

#Calculate proportionality constant(K) for each word
data1['K']= data1['counts']*data1['rank']

#Get the endpoints of the frequency and rank data
xs= data1['rank'][0],data1['rank'][data1.shape[0]-1]
ys= data1['counts'][0],data1['counts'][data1.shape[0]-1]

#Plot a log-log(frequency vs rank) plot to visualise the results obtained 
fig= plt.figure()
plt.plot(xs,ys,label="Zipf's Law(expected)")
plt.plot(data1['rank'], data1['counts'], label='corpus')
plt.legend()
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title(" Frequency distribution of words")
plt.xscale('log')
plt.yscale('log')
fig.savefig('frequency_distribution_plot.jpg')
plt.show()

"""#####Since above log-log plot gives us almost straight line, therefore we can say that frequency of the words is inversely proportional to the word rank. So, here we can say that our text is consistent with Zipf's Law."""

#Plot a linear graph (Rank vs K) to check the Zipf's law property
fig1= plt.figure(figsize=(10,4))
plt.plot(data1['rank'], data1['K'], label='corpus')
plt.legend()
plt.xlabel('Rank')
plt.ylabel('Frequency*Rank')
plt.title("Visualising Zipf's Law")
fig1.savefig('Rank vs K_plot.jpg')
plt.show()

"""#####From the above plot, it can be stated that, the Zipf's Law roughly holds for the top ranked words, as we can see a constancy in the value of K in that section. While, for the words with lower rank, K is not constant, and thus these words doesn't follow the law.
So, finally we can state that our text is not completely in-line with the law. Our text is consistent upto a certain extent with the law, when observed minutely.
"""