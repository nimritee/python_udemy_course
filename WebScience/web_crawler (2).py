import requests
from bs4 import BeautifulSoup
import pandas as pd
from dateutil.parser import parse

# Creating global to store various link and its modified time 
modified_time =[]
internal_link_count=[]
url_fragment_count=[]
external_link_count=[]
counter = 0

# Function to parse the html file using beautifulsoup
def beautiful_soup(url):
   page_response = requests.get(url)  #Getting raw data from URL
   raw_data = BeautifulSoup(page_response.content, 'html.parser')
   extract_timestamp(raw_data)
   return raw_data

# Function to extract links
def extract_links(raw_data):
  links=[]
  anchor_data = raw_data.find_all('a')   # Extracting out the 'a' tagged elements
  for link in anchor_data:
    if 'href' in link.attrs:
      links.append(str(link.attrs['href']))
  return links

# Function to extract the last time the page was modified 
def extract_timestamp(raw_data):
  #Extracting out the 'li' tagged element w.r.t the id(i.e the timestamp regarding when the article was last modified)
  time_stamp =  raw_data.find('li', id = "footer-info-lastmod")
  if time_stamp == None:
    modified_time.append('None')
  else:
    time_stamp= ''.join(map(str,(time_stamp.string).split()[6:]))
    modified_time.append(parse(time_stamp).strftime('%Y-%m-%d::%H-%M'))

# Fuction for grouping the links into internal, external and the links that reference contents within the same page (url fragments)
def categorize_links(link_bucket):
  internal_links=[]
  url_fragments= []
  external_links= []

  for i in link_bucket:
    if i.startswith('/wiki/'):
      internal_links.append(i)
    elif i.startswith('#'):
      url_fragments.append(i)
    elif i.startswith('https:'):
      external_links.append(i)

  # Keeping a track of count of each link type
  internal_link_count.append(len(internal_links))
  url_fragment_count.append(len(url_fragments))
  external_link_count.append(len(external_links))
  return internal_links

def internal_link(inner_links):
  print(internal_link_count)
  for i in inner_links:
    if len(internal_link_count)< 200:
      new_link = "https://simple.wikipedia.org" + i
      fetched_links = extract_links(beautiful_soup(new_link))
      more_internal_links = categorize_links(fetched_links)
    else:
      break
  if counter < 2:
    more_links = []
    more_links.append(more_internal_links[2])
    crawl = internal_link(more_links)
    counter = global counter + 1 
    

# Scraping the initial link
initial_url = 'https://simple.wikipedia.org/wiki/Climate_change'
link_bucket= extract_links(beautiful_soup(initial_url))
initial_internal_links= categorize_links(link_bucket)
more_links=internal_link(initial_internal_links)


# Web crawling through initial internal links.
# for internal_links in internal_initial_links:
  
#   url1= domain_name + internal_links
#   b= beautiful_soup(url1)
#   #Extracting a single internal link and crawl through that page 
#   if internal_links== internal_initial_links[2]:
#     extract_timestamp(b)
#     y=categorize_links(extract_links(b))
#     ##Iterating through first 150 internal links(estimated out from the above extracted page) one by one and extract the required details
#     for internal_links in y[0:150]:

#       url1= domain_name + internal_links
#       b= beautiful_soup(url1)
#       all_links= extract_links(b)
#       extract_timestamp(b)
#       categorize_links(all_links)  
#   else:
    
#     all_links= extract_links(b)
#     extract_timestamp(b)
#     categorize_links(all_links)

num=[]
for x in range(1,43):
  num.append(x)

#Organizing the collected data into a dataframe
df= {'Pagecount' : num,
                  'INTcount' : internal_link_count,
                  'EXTcount' : external_link_count,
                  'URLfragments' : url_fragment_count,
     'timestamp' : modified_time}
data= pd.DataFrame(df)
print(data)