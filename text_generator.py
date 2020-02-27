import numpy as np
import sys
import pandas as pd
from jinja2 import Template
import json

#open metadata and get all the parameters
with open('metadata.json') as json_file:
    data = json.load(json_file)
    dataset = data['Data-Path']
    year = data['Year']
    subject = data['Subject']
    source = data['Source']
    given_title = data['Title']


#get data from spreadsheet
finaldata = pd.read_csv(dataset)

#sort into columns
fips_code = finaldata['FIPS'].tolist()
county = finaldata['COUNTY'].tolist()
county_number= finaldata['COUNTY-NUMBER'].tolist()


#variables
# cn = county number
# hl = higher/lower
# sa = state average
# r = rank by state
# p = percentile national


#to calculate with codeeee
state_average=
higher/lower =
rank =
percentile =



def localized_Text(fips):

    f = int(fips)
    i = fips_code.index(f)


    t = Template("The {{y}} {{s}} in {{c}}, (which is the closest county in your area that collects such data), was {{cn}}, which is {{hl}} than the state average of {{sa}}, according to {{src}}. Within the state, {{c}} has the {{r}} highest {{s}}, and it is on the {{p}} percentile in the country.")

    ti= Template(given_title)
    generated_title = ti.render(c = county[i])




#define var to plug into template

    generated_text = t.render( y = year, s = subject, c = county[i], cn = county_number[i], hl = "blah", sa = "blah", src = source, c = county[i], r = "blah", s = subject,  p = "blah")

    jsonobject = {
    "Text": str(generated_text),
    "Title": str(generated_title),
    "County" : str(county[i])
    }

    textjson = json.loads(jsonobject)

    workfile = str(fips) + ".json"
    f = open(workfile, 'w')
    f.write(textjson)


#create file for every fips code
for num in fips_code:
    if math.isnan(num):
        pass
    else:
        c = int(num)
        localized_Text(c)
        print("done")
