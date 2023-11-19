
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import Cemetery

    print()
    title = sys.argv[2]
    print(f"""\033[4;33m{title}\033[0m""")
    print("-" * len(title))

    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/cemetery.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(f"""Fetch table response code: {r.status}""")
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    reader.fieldnames = [field.replace('.', '_') for field in reader.fieldnames]
    
    # add a country model for each row in the csv file
    for row in reader:
        if row['latitude'] == '':
            row['latitude'] = 0 
        if row['longitude'] == '':
            row['longitude'] = 0
        try:
            Cemetery.objects.create(
                id=row['id'],
                name=row['name'],
                country_id=row['ccn3'],
                latitude=row['latitude'],
                longitude=row['longitude']
        )
        except Exception as e:
            print(f"""💥row: ({row}) """)
            raise e
