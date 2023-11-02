
def run():

    import urllib3
    import csv
    from cmp.models import Country
    
    ref_data_url = "https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(r.status)
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    reader.fieldnames = [field.replace('.', '_') for field in reader.fieldnames]
    
    # add a country model for each row in the csv file
    for row in reader:
        print(row['name_common'])
        if row['name_common'] == 'Kosovo':
            row['ccn3'] = '999'
            row['independent'] = False
        try:
            Country.objects.create(
                name_common=row['name_common'],
                name_official=row['name_official'],
                tld=row['tld'],
                cca2=row['cca2'],
                ccn3=row['ccn3'],
                cca3=row['cca3'],
                cioc=row['cioc'],
                independent=row['independent'],
                status=row['status'],
                unMember=row['unMember'],
                currencies=row['currencies'],
                idd_root=row['idd_root'],
                idd_suffixes=row['idd_suffixes'],
                capital=row['capital'],
                alt_spellings=row['altSpellings'],
                region=row['region'],
                subregion=row['subregion'],
                languages=row['languages'],
                latlng=row['latlng'],
                landlocked=row['landlocked'],
                borders=row['borders'],
                area=row['area'],
                flag=row['flag'],
                callingCodes=row['callingCodes']
        )
        except Exception as e:
            print("Error with: " + row['name_common'])
            raise e


        


        



