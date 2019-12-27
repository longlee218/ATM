# Generated by Django 3.0 on 2019-12-27 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ATM',
            fields=[
                ('atm_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('atm_balance', models.BigIntegerField()),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'Deactive')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('bank_name', models.TextField()),
                ('bank_headquarters', models.TextField()),
                ('bank_phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_address', models.TextField()),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Long.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('province_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('province_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoryMoney',
            fields=[
                ('history_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('history_time', models.DateTimeField()),
                ('money', models.BigIntegerField()),
                ('atm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Long.ATM')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=32)),
                ('emp_password', models.CharField(max_length=50)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Long.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='province_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Long.Province'),
        ),
        migrations.AddField(
            model_name='bank',
            name='branches',
            field=models.ManyToManyField(through='Long.Branch', to='Long.Province'),
        ),
        migrations.AddField(
            model_name='atm',
            name='employee_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Long.Employee'),
        ),
    ]
