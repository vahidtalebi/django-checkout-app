# Generated by Django 3.0.3 on 2020-02-06 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fristname', models.CharField(max_length=70)),
                ('lastname', models.CharField(max_length=70)),
                ('national_code', models.IntegerField()),
                ('personnel_code', models.IntegerField()),
                ('fathername', models.CharField(max_length=70)),
                ('mobile_number', models.IntegerField()),
                ('gender', models.BooleanField()),
                ('personnel_image', models.ImageField(upload_to='admin_image')),
                ('access_type_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Access_type')),
            ],
        ),
        migrations.CreateModel(
            name='Driving_fine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Payport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Request_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=70)),
                ('lastname', models.CharField(max_length=70)),
                ('fathername', models.CharField(max_length=50)),
                ('time_of_birth', models.DateTimeField()),
                ('national_code', models.IntegerField()),
                ('mobile_number', models.IntegerField()),
                ('gender', models.BooleanField()),
                ('personal_pic', models.ImageField(upload_to='user_image')),
                ('marital_status', models.CharField(max_length=70)),
                ('std_code', models.IntegerField()),
                ('majar', models.CharField(max_length=120)),
                ('enter_yaer', models.IntegerField()),
                ('field', models.CharField(max_length=120)),
                ('gerayesh', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=1200)),
                ('phone_number', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('finger_print', models.CharField(max_length=1200)),
                ('otp', models.IntegerField()),
                ('state', models.CharField(max_length=120)),
                ('driving_licence_number', models.IntegerField()),
                ('driving_licence_years', models.IntegerField()),
                ('driving_licence_date', models.DateTimeField()),
                ('driving_licence_fr_photo', models.CharField(max_length=1200)),
                ('driving_licence_ba_photo', models.CharField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField()),
                ('request_time', models.DateTimeField()),
                ('request_image', models.CharField(max_length=1000)),
                ('comment', models.CharField(max_length=1200)),
                ('admin_dicision', models.CharField(max_length=1200)),
                ('admin_comment', models.CharField(max_length=1200)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Admins')),
                ('request_type_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Request_type')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_time', models.DateTimeField()),
                ('payment_amount', models.IntegerField()),
                ('payport_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Payport')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('online_time', models.DateTimeField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Admins')),
            ],
        ),
        migrations.CreateModel(
            name='Enter_cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('enter_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField()),
                ('car_tag', models.CharField(max_length=50)),
                ('car_photo', models.CharField(max_length=1200)),
                ('car_color', models.CharField(max_length=50)),
                ('car_type', models.CharField(max_length=50)),
                ('gates_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Gates')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Drivers_fined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_photo', models.ImageField(upload_to='car_image')),
                ('car_tag', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('driving_fine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Driving_fine')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Locations')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khuisf_trafic.Users')),
            ],
        ),
    ]
