from cmp.models import Soldier

def run():
    Ranks = Soldier.objects.all()
    Ranks.delete()
