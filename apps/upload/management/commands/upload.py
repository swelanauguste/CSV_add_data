import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from account.models import Account


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    first_name = row[0]
                    last_name = row[1]
                    location = row[2]
                    age = row[3]
                    self.stdout.write(self.style.SUCCESS(f'{last_name}, {first_name} added'))
                    user = Account.objects.get_or_create(
                        first_name=first_name, last_name=last_name, location=location, age=age)
