from cmp.models import Cemetery

def run():
    Cemeteries = Cemetery.objects.all()
    Cemeteries.delete()
