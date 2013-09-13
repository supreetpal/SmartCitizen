from django.core.management.base import BaseCommand, CommandError
from Govt_Data_Link.models import Year_of_Ruling,Political_Party
from datetime import datetime

file = "party_rule_data"


class Command(BaseCommand):
  option_list = BaseCommand.option_list
  def handle(self, *args, **options):
    Year_of_Ruling.objects.all().delete()
    file_data      = open(file,'r+').read()
    party_data     = eval(file_data)
    for data in party_data:
        print data[0]
        party        = Political_Party.objects.get(name = data[0])
        ruling       = Year_of_Ruling()
        ruling.party = party
        ruling.pm    = data[1]
        ruling.took_office = datetime.strptime(data[2],"%d-%m-%Y")
        if data[3]!=None:                                            #None Case for Manmohan Singh
            ruling.left_office = datetime.strptime(data[3],"%d-%m-%Y")
        ruling.save()
