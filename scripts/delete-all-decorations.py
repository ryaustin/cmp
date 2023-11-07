from cmp.models import Decoration

def run():
    Ranks = Decoration.objects.all()
    Ranks.delete()
