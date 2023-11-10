from cmp.models import SoldierImprisonment

def run():
    Imprisonments = SoldierImprisonment.objects.all()
    Imprisonments.delete()
