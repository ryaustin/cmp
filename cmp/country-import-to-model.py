
# read countries.json

import json

from cmp.models import Country

with open('countries.json') as f:
    data = json.load(f) 
    for country in data:
        print(country['name']['common'])