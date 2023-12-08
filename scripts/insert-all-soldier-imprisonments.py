
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import SoldierImprisonment

    print()
    title = sys.argv[2]
    print(f"""\033[4;33m{title}\033[0m""")
    print("-" * len(title))
    
    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/soldier-imprisonment.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(f"""Fetch table response code: {r.status}""")
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    # breakpoint()
    # id,soldier_id,company_id,powNumber,powCamp_id,dateFrom,dateTo,notes
    for row in reader:
        #print(f"""SoldierImprisonment: {row['id']} {row['soldier_id']} """)
        try:
            SoldierImprisonment.objects.create(
                id = row['id'],
                soldier_id = row['soldier_id'],
                legacy_company = row['company_id'],
                pow_number = row['powNumber'],
                pow_camp_id = row['powCamp_id'],
                legacy_date_from = row['dateFrom'],
                legacy_date_to = row['dateTo'],
                notes = row['notes']
        )
        except Exception as e:
            print(f"""💥row: ({row}) """)
            raise e
