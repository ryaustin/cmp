from cmp.models import Country

def run():
    Countries = Country.objects.all()
    Countries.delete()
