
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import Country
    
    #ref_data_url = "https://raw.githubusercontent.com/mledoze/countries/master/dist/countries.csv"
    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/country.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(r.status)
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    #reader.fieldnames = [field.replace('.', '_') for field in reader.fieldnames]
    
    print(reader.fieldnames)
    for row in reader:
        print(row['Name'])
        try:
            Country.objects.create(
                id = row['id'],
                name = row['Name'],
                alpha2 = row['Alpha2'],
                alpha3 = row['Alpha3'],
                country_number = row['CountryNumber'],
                flag = ""
        )
        except Exception as e:
            print("Error with: " + row['Name'])
            raise e

