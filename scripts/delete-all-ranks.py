from cmp.models import Rank

def run():
    Ranks = Rank.objects.all()
    Ranks.delete()
