from cmp.models import PowCamp

def run():
    all_objects = PowCamp.objects.all()
    all_objects.delete()
