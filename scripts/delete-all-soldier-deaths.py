from cmp.models import SoldierDeath

def run():
    soldierDeaths = SoldierDeath.objects.all()
    soldierDeaths.delete()
