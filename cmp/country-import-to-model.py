
# read csv.py
# read csv_file and create a country model for each row in the csv file
# the csv_file has the format "id,name,alpha2,alpha3,country_code"

from cmp.models import Country

csv_file = "/tmp/countries.csv"

with open(csv_file, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        id, name, alpha2, alpha3, old_id, blah = line.split(",")
        c = Country(name=name, alpha2=alpha2, alpha3=alpha3, old_id=old_id)
        print(c)
        c.save()