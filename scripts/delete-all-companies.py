from cmp.models import Company

def run():
    companies = Company.objects.all()
    companies.delete()
