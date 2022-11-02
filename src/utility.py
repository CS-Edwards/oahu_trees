__author__ = "Candace Edwards -- CS Edwards"
__maintainer__ = "Candace Edwards"
__email__ = "cedward2@hawaii.edu"

import csv
from bs4 import BeautifulSoup

#wiki_url='https://en.wikipedia.org/wiki/Acacia'
#response = requests.get(url = wiki_url)
#status = response.status_code


#print(status)

#class = "infobox biota"

#soup = BeautifulSoup(response.content, 'html.parser')


def wikiTableParse(soup):
    title = soup.find(id="firstHeading")

    print('Starting wiki-table parse for ...')
    print(title.string)

    search_table=soup.find_all("table",class_="infobox biota")
    #print(len(search_table))
    #print(type(search_table))
    #print(search_table)

    try:
        working_table=search_table[0]
        #print(type(working_table))
    except IndexError:
        print(IndexError)
        return -1,-1 #flag an error



    rows = []
    rows.append([""])
    rows.append(['Title',title.string])

    # Find all `tr` tags
    data_rows = working_table.find_all('tr')

    for row in data_rows:
        value = row.find_all('td')
        beautified_value = [ele.text.strip() for ele in value]
        # Remove data arrays that are empty
        if len(beautified_value) == 0:
            continue
        rows.append(beautified_value)

    #remove last row with spec list
    rows.pop(-1)
    #rows.pop(-1)
    rows.append(['end-tree'])

    #for r in rows:
    #    print(r)
    return rows,title


def writeToCSV(rows):
    with open('Fall_22\ICS_484\p4\oahu_trees\src\data\output.csv', 'w', newline="") as output:
        writer = csv.writer(output)
        writer.writerows(rows)

    print('...csv write complete')

    














