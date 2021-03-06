# Generated by Django 2.1.2 on 2018-11-15 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolioHistory',
            fields=[
                ('rebalanceID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioID',
            fields=[
                ('portfolioID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioWeights',
            fields=[
                ('weightID', models.AutoField(primary_key=True, serialize=False)),
                ('portfolioID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.PortfolioID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField(max_length=100)),
                ('lastName', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='stockHistory',
            fields=[
                ('eventID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='stockID',
            fields=[
                ('tickerID', models.AutoField(primary_key=True, serialize=False)),
                ('companyName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('surveyID', models.AutoField(primary_key=True, serialize=False)),
                ('question1', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Dummy',
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='tickerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.stockID'),
        ),
        migrations.AddField(
            model_name='portfolioweights',
            name='tickerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.stockID'),
        ),
        migrations.AddField(
            model_name='portfolioid',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Profile'),
        ),
        migrations.AddField(
            model_name='portfoliohistory',
            name='portfolioID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.PortfolioID'),
        ),
        migrations.AddField(
            model_name='portfoliohistory',
            name='tickerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.stockID'),
        ),
    ]
