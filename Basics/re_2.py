import re

def multi_pattern(pattern, phrase):

    for pat in pattern:
        print("I am looking for the pattern: ",pat)
        print(re.findall(pat,phrase))
        print('\n')

phrase = "sdsd...sssddd...sdddsddd...dsds...dsssss...sddddd"

pattern =['sd*']
multi_pattern(pattern,phrase)
#output
#['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 'sddddd']

pattern =['sd+']
multi_pattern(pattern,phrase)
#output
#['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddddd']

pattern =['sd?']
multi_pattern(pattern,phrase)
#Output
#['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 'sd']

pattern =['sd{3}']
multi_pattern(pattern,phrase)
#Output
#['sddd', 'sddd', 'sddd', 'sddd']

pattern =['sd{1,3}']
multi_pattern(pattern,phrase)
#Output
#['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddd']


pattern =['s[sd]+']
multi_pattern(pattern,phrase)
#Output
#['sdsd', 'sssddd', 'sdddsddd', 'sds', 'sssss', 'sddddd'] 
# #Basically even after getting that 1 s or d, we can look for other s or d


#Exclusion

phrase_1 = "This is a statement! With a lot of punctuations. We need to remove it?"

pattern = ['[^!.?]+'] #Plus because we looking for one or more instances of it.
multi_pattern(pattern,phrase_1)
#Output
#['This is a statement', ' With a lot of punctuations', ' We need to remove it']


pattern = ['[a-z]+']
multi_pattern(pattern,phrase_1)
#Output
#['his', 'is', 'a', 'statement', 'ith', 'a', 'lot', 'of', 'punctuations', 'e', 'need', 'to', 'remove', 'it']

pattern = ['[A-Z]+']
multi_pattern(pattern,phrase_1)
#Output
#['T', 'W', 'W']

statement = "all the digits like 6783 3883 3 will be given as output #maths"
pattern = [r'\d+']
multi_pattern(pattern,statement)
#Output
#['6783', '3883', '3']

pattern = [r'\D+']
multi_pattern(pattern,statement)
#Output
#['all the digits like ', ' ', ' ', ' will be given as output #maths']

pattern = [r'\s+']
multi_pattern(pattern,statement)
#Output
#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


pattern = [r'\S+']
multi_pattern(pattern,statement)
#Output
#['all', 'the', 'digits', 'like', '6783', '3883', '3', 'will', 'be', 'given', 'as', 'output', '#maths']

pattern = [r'\w+']
multi_pattern(pattern,statement)
#Output
#['all', 'the', 'digits', 'like', '6783', '3883', '3', 'will', 'be', 'given', 'as', 'output', 'maths']

pattern = [r'\W+']
multi_pattern(pattern,statement)
#Output
#[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']