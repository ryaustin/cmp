
def run():

    import sys
    import urllib3
    import csv
    from cmp.models import Soldier
    
    ref_data_url = "https://raw.githubusercontent.com/gm3dmo/old-cmp/main/data/soldier.csv"
    http = urllib3.PoolManager()
    r = http.request('GET', ref_data_url)
    print(r.status)
    # load the response into a csv dictionary reader
    reader = csv.DictReader(r.data.decode('utf-8').splitlines())
    # breakpoint()
    print(reader) 
    # print(reader.fieldnames)
    for row in reader:
        # id,surname,initials,army_number,rank_id,notes
        print(f"""{row['id']} {row['surname']}""")
        try:
            Soldier.objects.create(
                id = row['id'],
                surname = row['surname'],
                initials = row['initials'],
                army_number = row['army_number'],
                rank_id = row['rank_id'],
                notes = row['notes']
        )
        except Exception as e:
            print("Error with: " + row['surname'])

            raise e
