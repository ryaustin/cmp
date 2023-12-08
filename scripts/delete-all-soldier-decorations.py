from cmp.models import SoldierDecoration

def run():
    SoldierDecorations = SoldierDecoration.objects.all()
    SoldierDecorations.delete()
