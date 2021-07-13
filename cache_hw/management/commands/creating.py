import random
import sys
from datetime import date

from django.core.management.base import BaseCommand

from faker import Faker

from cache_hw.models import Author, Post


fake = Faker()
fake_s = Faker(['en_US', 'ja_JP', 'it_IT'])

rand_books = ['English Lessons * for adults',
              'Recipes for everyone (part *)',
              'How to create c4 at home *',
              'Life Of No-One *',
              'See you on the beach (part *)',
              'Everyone needs a hug *',
              'My mom told me to go outside *...',
              'How to be retard *',
              'Murder in heaven (part *)',
              'Adventures From Kyiv To NY *', ]


class Command(BaseCommand):
    help = 'Creating some authors with those posts :)'

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


