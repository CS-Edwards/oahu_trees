__author__ = "Candace Edwards -- CS Edwards"
__maintainer__ = "Candace Edwards"
__email__ = "cedward2@hawaii.edu"


#wikipedia scrape script
import requests
import csv
from bs4 import BeautifulSoup
from utility import *

#genus ='Acrocarpus'
#genus_list = ['Adansonia', 'Agathis', 'Acrocarpus']
bad_status_list = list()
bad_data_list = list()
all_trees = []


path = 'Fall_22\ICS_484\p4\oahu_trees\src\data\genus_list.csv'
file = open(path,"r")
data = list(csv.reader(file,delimiter="\n"))
file.close
#data = pd.read_csv("genus_list", names=['genus'] )
#//print(data.head(10))

print(data[:10])
i = 0


for genus in data:

    #set url
    wiki_url='https://en.wikipedia.org/wiki/' + genus[0]

    response = requests.get(url = wiki_url)
    status = response.status_code
    


    #limit to 5 queries for testing
    #i+=1
    #if (i>5):
        #break
    
    
    if(status!=200):
        bad_status_list.append([status,wiki_url])
        continue

    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(id="firstHeading")
        print(title.string)

        row,label = wikiTableParse(soup)

        if(row!=-1):
            all_trees.append(row)
            print(label.string ,'...appended to data')
        else:
            print('ERROR: in utility.py with tree:' + title.string)        
            bad_data_list.append(title.string)

writeToCSV(all_trees)

##outside loop
print(bad_status_list)
print(bad_data_list)