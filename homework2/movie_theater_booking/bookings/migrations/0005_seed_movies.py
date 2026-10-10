from django.db import migrations

def add_movies(apps, schema_editor):
    Movie = apps.get_model("bookings", "Movie")
    Movie.objects.create(title = "Pocohontas", description = "Native American stuff happens", 
    release_date = "2026-11-13", duration = 2)

    Movie.objects.create(title = "Shrek", description = "An ogre falls in love with a princess", 
    release_date = "2026-12-25", duration = 3)
    
    Movie.objects.create(title = "Dora the Explorer", description = "Go on adventures with Dora and Friends and learn spanish along the way!", 
    release_date = "2026-10-14", duration = 1)

    Movie.objects.create(title = "Titanic", description = "a ship is gonna sink from an iceberg", 
    release_date = "2027-11-02", duration = 3)


class Migration(migrations.Migration):
    dependencies = [
        ('bookings', '0004_seed_seats'),
    ]
    operations = [
         migrations.RunPython(add_movies),
    ]
