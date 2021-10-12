import re

#When we wish to find if the pattern is prenset in the String or not.

patterns =["term1","term2"]

text ="We are supposed to find the term1, but the other one is absent"

for pattern in patterns:
    print("I am seraching for the pattern: ",pattern)

    if re.search(pattern,text): #We need to pass the re.search(pattern_to_be_searched,string_to_be_searched_in)
        print("Match!")
    else:
        print("No Matches Found!")
    

# re can also be used to find where the matching of the pattern start
text1 ="We are supposed to find the term1, but the other one is absent"
match = re.search('term2',text1)
if match:
    start_point = print(match.start())
else:
    print("Value not found")

#re can be used to split the text.

email ="nimritee97@gmail.com"
split_term ="@"

print(re.split(split_term,email))

# re can be used to findall the matches in the string 

string1="We are supposed to find all the matches of find in the finding string"
print(len(re.findall("find ",string1)))