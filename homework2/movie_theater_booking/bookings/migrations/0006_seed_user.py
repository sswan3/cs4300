from django.db import migrations
#from django.contrib.auth.models import User

def add_user(apps, schema_editor):
    user = apps.get_model("auth", "User")
    user.objects.create_user(username = "demo", password = "123")

class Migration(migrations.Migration):
    dependencies = [
        ('bookings', '0005_seed_movies'),
    ]

    operations = [
         migrations.RunPython(add_user),
    ]
