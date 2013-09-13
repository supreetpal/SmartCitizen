from django.core.management.base import BaseCommand, CommandError
from Govt_Data_Link.models import Political_Party

file = "govt_party_data"

columns = ['name','cp','pl_cp','ldr_lok_sabha','ldr_raj_sabha','founded_on','preceded_by','headquaters','newspaper','youth_wing','women_wing','pol_position','colors','eci_status','alliance','seats_lok_sabha','seats_raj_sabha']

class Command(BaseCommand):
  option_list = BaseCommand.option_list
  def handle(self, *args, **options):
    Political_Party.objects.all().delete()
    file_data      = open(file,'r+').read()
    party_data     = eval(file_data)
    for data in party_data:
        create_kwargs = {}
        for cols in range(len(columns)):
            print columns[cols] , data[cols]
            create_kwargs[columns[cols]] = data[cols]
        pol_party = Political_Party(**(create_kwargs))
        pol_party.save()

