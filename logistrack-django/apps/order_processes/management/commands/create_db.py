import MySQLdb
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Creates the database if it does not exist (for local development)"

    def handle(self, *args, **options):
        db_settings = settings.DATABASES['default']
        try:
            conn = MySQLdb.connect(
                host=db_settings['HOST'],
                user=db_settings['USER'],
                passwd=db_settings['PASSWORD'],
                port=int(db_settings['PORT'] or 3306)
            )
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {db_settings['NAME']} "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
            )
            conn.commit()
            cursor.close()
            conn.close()
            self.stdout.write(self.style.SUCCESS(f"Database '{db_settings['NAME']}' created (or already existed)"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating database: {e}"))
