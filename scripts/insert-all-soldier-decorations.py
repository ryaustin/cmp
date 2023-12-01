
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import SoldierDecoration
    from cmp.models import Company
    from cmp.models import Country
    from cmp.models import Soldier

    print()
    title = sys.argv[2]
    print(f"""\033[4;33m{title}\033[0m""")
    print("-" * len(title))
    
    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/soldier-decoration.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(f"""Fetch table response code: {r.status}""")
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('ISO-8859-1').splitlines())
    
    for row in reader:
        #print(f"""row: ({row['id']}) cwgc:({row['cwgc_id']})""")
        try:
            company = Company.objects.filter(name=row['company_id']) 
            if company:
                company = company.first()
            else:
                #print(f"""row: ({row['id']}) cwgc:({row['cwgc_id']})""")
                company = Company.objects.filter(name="UNKNOWN").first()
            country = Country.objects.filter(name=row['country_id'])
            if country:
                country = country.first()
            else:
                country = Country.objects.filter(name="UNKNOWN").first()
            gazette_date = row.get('gazetteDate', None)
            if gazette_date == "":
                gazette_date = None
                
            if int(row.get("id")) == 384:
                print(f"""row: {row}""")
                breakpoint()

            SoldierDecoration.objects.create(
                #id,soldier_id,company_id,decoration_id,gazetteIssue,gazettePage,gazetteDate,citation,notes,country_id
                # create the model
                id = int(row['id']),
                #soldier = soldier
                soldier_id = int(row['soldier_id']),
                company_id  = company.id,
                decoration_id = int(row['decoration_id']),
                gazette_issue = row['gazetteIssue'],
                gazette_page = row['gazettePage'],
                gazette_date = gazette_date,
                citation = row['citation'],
                notes = row['notes'],
                country_id = country.id
        )
        except Exception as e:
            print(f"""💥row: {row}""")
            raise e
