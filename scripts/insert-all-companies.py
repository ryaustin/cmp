
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import Company

    print()
    title = sys.argv[2]
    print(f"""\033[4;33m{title}\033[0m""")
    print("-" * len(title))
    
    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/company.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(f"""Fetch table response code: {r.status}""")
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    
    print(reader.fieldnames)
    for row in reader:
        #print(row['name'])
        try:
            Company.objects.create(
                name = row['name']
        )
        except Exception as e:
            print(f"""💥row: ({row}) """)
            raise e

