from django.db import migrations

def migrate_address_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    NewAddress = apps.get_model('letting', 'Address')

    for old_address in OldAddress.objects.all():
        new_address = NewAddress(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        new_address.save()

def migrate_letting_data(apps, schema_editor):
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('letting', 'Letting')
    NewAddress = apps.get_model('letting', 'Address')

    for old_letting in OldLetting.objects.all():
        new_letting = NewLetting(
            id=old_letting.id,
            title=old_letting.title,
            address=NewAddress.objects.get(id=old_letting.address.id)
        )
        new_letting.save()

class Migration(migrations.Migration):

    dependencies = [
        ('letting', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_address_data),
        migrations.RunPython(migrate_letting_data),
    ]
