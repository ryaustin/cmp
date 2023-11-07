
def run():

    import urllib3
    import csv
    from cmp.models import Cemetery
    
    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/cemetery.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(r.status)
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    reader.fieldnames = [field.replace('.', '_') for field in reader.fieldnames]
    
    # add a country model for each row in the csv file
    for row in reader:
        print(row['id'])
        if row['latitude'] == '':
            row['latitude'] = 0 
        if row['longitude'] == '':
            row['longitude'] = 0
        if int(row['id']) == 948:
            print(row)
            continue
        if int(row['id']) == 991:
            print(row)
            continue
        if int(row['id']) == 1007:
            print(row)
            continue
        if int(row['id']) == 1043:
            print(row)
            continue
        if int(row['id']) == 1051:
            print(row)
            continue
        if int(row['id']) == 1068:
            print(row)
            continue
        try:
            Cemetery.objects.create(
                id=row['id'],
                name=row['name'],
                country_id=row['ccn3'],
                latitude=row['latitude'],
                longitude=row['longitude']
        )
        except Exception as e:
            print("Error with: " + row['name'])
            raise e
