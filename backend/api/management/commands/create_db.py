from django.core.management.base import BaseCommand
from django.conf import settings

import psycopg2
from urllib.parse import urlparse
from decouple import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Command(BaseCommand):
    '''Custom command to create a psql database'''

    def handle(self, *args, **kwargs):
        if getattr(settings, "DEBUG", False):
            # Only run if Debug=True (so it's not run in production environments, as this is only useful for dev)
            print('Creating database...')
            self._create()

    @staticmethod
    def _create():
        r = urlparse(config('DATABASE_URL'))
        DB_NAME = r.path.replace('/', '')
        DB_USER = r.username
        DB_PASSWORD = r.password

        conn = psycopg2.connect(user="postgres",
                                host='localhost')
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # To CREATE DB from python

        cur = conn.cursor()
        cur.execute(f'DROP DATABASE IF EXISTS {DB_NAME};')
        cur.execute(f'CREATE DATABASE {DB_NAME};')
        cur.execute(f'DROP USER IF EXISTS {DB_USER};')
        cur.execute(f"CREATE USER {DB_USER} WITH PASSWORD '{DB_PASSWORD}';")
        cur.execute(f"ALTER ROLE {DB_USER} SET client_encoding TO 'utf8';")
        cur.execute(f"ALTER ROLE {DB_USER} SET default_transaction_isolation TO 'read committed';")
        cur.execute(f"ALTER ROLE {DB_USER} SET timezone TO 'UTC';")
        cur.execute(f'GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};')
        cur.execute(f'ALTER USER {DB_USER} CREATEDB;')
        conn.commit()
        conn.close()
