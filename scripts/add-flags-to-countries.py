
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import Country
    
    ref_data_url =  "https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(r.status)
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())

    # create a dictionary from the reader with key ccna2 and value flag
    flags = {row['cca2']: row['flag'] for row in reader}

    print(flags['GB'])

    # for every country in the database, add the flag if the country is in the dictionary
    for country in Country.objects.all():
        if country.Alpha2 in flags:
            country.Flag = flags[country.Alpha2]
            country.save()
            print(f"""{country.name} {country.Alpha2} {country.Flag}""")
        else:
            print(f"""{country.name} {country.Alpha2} no flag""")
    

