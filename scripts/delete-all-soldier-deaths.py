from cmp.models import SoldierDeath

def run():
    SoldierDeaths = SoldierDeath.objects.all()
    SoldierDeaths.delete()