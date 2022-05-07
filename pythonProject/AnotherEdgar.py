import requests  # web requests
from bs4 import BeautifulSoup  # beautifulsoup
import re  # re module for regex
import pandas as pd

# Get Apple's [AAPL] 2018 Form 10-K
r = requests.get('https://www.sec.gov/Archives/edgar/data/320193/000032019318000145/0000320193-18-000145.txt',
                 headers={'User-Agent': 'Mozilla'})
raw_10k = r.text

# Regex to find <DOCUMENT> tags
doc_start_pattern = re.compile(r'<DOCUMENT>')
doc_end_pattern = re.compile(r'</DOCUMENT>')
# Regex to find <TYPE> tag proceeding any characters, terminating at new line
type_pattern = re.compile(r'<TYPE>[^\n]+')

# Create 3 lists with the span indices for each regex

### There are many <Document> Tags in this text file, each as specific exhibit like 10-K, EX-10.17 etc
### First filter will give us document tag start <end> and document tag end's <start>
### We will use this to later grab content in between these tags
doc_start_is = [x.end() for x in doc_start_pattern.finditer(raw_10k)]
doc_end_is = [x.start() for x in doc_end_pattern.finditer(raw_10k)]

### Type filter is interesting, it looks for <TYPE> with Not flag as new line, ie terminate there, with + sign
### to look for any char afterwards until new line \n. This will give us <TYPE> followed Section Name like '10-K'
### Once we have have this, it returns String Array, below line will with find content after <TYPE> ie, '10-K'
### as section names
doc_types = [x[len('<TYPE>'):] for x in type_pattern.findall(raw_10k)]

document = {}

# Create a loop to go through each section type and save only the 10-K section in the dictionary
for doc_type, doc_start, doc_end in zip(doc_types, doc_start_is, doc_end_is):
    if doc_type == '10-K':
        document[doc_type] = raw_10k[doc_start:doc_end]

# display excerpt the document

# Write the regex
regex = re.compile(r'(>Item(\s|&#160;|&nbsp;)(1A|1B|7A|7|8|9)\.{0,1})|(ITEM\s(1A|1B|7A|7|8|9))')

# Use finditer to match the regex
matches = regex.finditer(document['10-K'])

# Write a for loop to print the matches
for match in matches:
    print(match)

# Matches
matches = regex.finditer(document['10-K'])

# Create the dataframe
test_df = pd.DataFrame([(x.group(), x.start(), x.end()) for x in matches])

test_df.columns = ['item', 'start', 'end']
test_df['item'] = test_df.item.str.lower()

# Get rid of unnesesary charcters from the dataframe
test_df.replace('&#160;', ' ', regex=True, inplace=True)
test_df.replace('&nbsp;', ' ', regex=True, inplace=True)
test_df.replace(' ', '', regex=True, inplace=True)
test_df.replace('\.', '', regex=True, inplace=True)
test_df.replace('>', '', regex=True, inplace=True)

# display the dataframe
test_df.head()

# Drop duplicates
pos_dat = test_df.sort_values('start', ascending=True).drop_duplicates(subset=['item'], keep='last')

# Set item as the dataframe index
pos_dat.set_index('item', inplace=True)

# display the dataframe
#pos_dat

# Get Item 1a
item_1a_raw = document['10-K'][pos_dat['start'].loc['item1a']:pos_dat['start'].loc['item1b']]

# Get Item 7
item_7_raw = document['10-K'][pos_dat['start'].loc['item7']:pos_dat['start'].loc['item7a']]

# Get Item 7a
item_7a_raw = document['10-K'][pos_dat['start'].loc['item7a']:pos_dat['start'].loc['item8']]

# Get Item 8, !Need to find a way to grab the section. Below only grabs text '>Item 8.'
item_8_raw = document['10-K'][pos_dat['start'].loc['item8']:pos_dat['start'].loc['item9']]

### First convert the raw text we have to exrtacted to BeautifulSoup object
item_8_content = BeautifulSoup(item_8_raw, 'lxml')

### Apply prettify to organize code into tree structure
#print(item_1a_content.prettify()[0:1000])

# Use get_text to pull out just text without tags and style info
print(item_8_content.get_text("\n\n")[0:1500])