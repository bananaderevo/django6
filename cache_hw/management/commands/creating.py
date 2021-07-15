import random
import sys
from datetime import date

from django.core.management.base import BaseCommand

from faker import Faker

from cache_hw.models import Author, Post, Quotes


fake = Faker()


class Command(BaseCommand):
    help = 'Creating some authors with those posts and quotes :)'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int)

    def handle(self, *args, **options):
        if 0 > options['num']:
            sys.stdout.write('Error, wrong number: number should be more than 0.\n')
        else:
            for i in range(options['num']):
                Author.objects.create(name=fake.name(),
                                      info=fake.text())
                Post.objects.create(text=fake.text(),
                                    author=Author.objects.last())
                Quotes.objects.create(quotes=f'"{fake.text()}"',
                                      author=Author.objects.last())



