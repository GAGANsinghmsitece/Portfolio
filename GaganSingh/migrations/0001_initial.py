# Generated by Django 2.1.3 on 2019-02-25 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationGagan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(blank=True, max_length=500)),
                ('joiningperiod', models.CharField(blank=True, max_length=150)),
                ('course', models.CharField(blank=True, max_length=500)),
                ('date', models.DateTimeField(blank=True)),
                ('score', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileGagan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Gagan Singh', max_length=100)),
                ('Image', models.ImageField(upload_to='profilepic')),
                ('Bio', models.CharField(max_length=10000, null=True)),
                ('currently', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projectimage')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsGagan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('desc', models.CharField(blank=True, max_length=1000)),
                ('profilegagan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaganSingh.ProfileGagan')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='technical_stack')),
                ('desc', models.CharField(blank=True, max_length=1000)),
                ('profilegagan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaganSingh.ProfileGagan')),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateof', models.DateTimeField(blank=True)),
                ('heading', models.CharField(blank=True, max_length=200)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('profilegagan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaganSingh.ProfileGagan')),
            ],
        ),
        migrations.AddField(
            model_name='projectpara',
            name='projectsgagan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaganSingh.ProjectsGagan'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='projectsgagan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaganSingh.ProjectsGagan'),
        ),
        migrations.AddField(
            model_name='hobbies',
            name='profilegagan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaganSingh.ProfileGagan'),
        ),
        migrations.AddField(
            model_name='educationgagan',
            name='profilegagan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaganSingh.ProfileGagan'),
        ),
    ]
