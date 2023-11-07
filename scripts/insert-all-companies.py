
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import Company
    
    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/company.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(r.status)
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    
    print(reader.fieldnames)
    for row in reader:
        print(row['name'])
        try:
            Company.objects.create(
                name = row['name']
        )
        except Exception as e:
            print("Error with: " + row['name'])
            raise e

