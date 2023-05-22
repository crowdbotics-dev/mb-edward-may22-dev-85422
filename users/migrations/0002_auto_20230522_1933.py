# Generated by Django 2.2.28 on 2023-05-22 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlField', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Model5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Model6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='bigIntegerField',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='binaryField',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='booleanField',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dateField',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dateTimeField',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='decimalField',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='durationField',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emailField',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='floatField',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='genericIPAddressField',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='integerField',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='positiveIntegerField',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='positiveSmallIntegerField',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='slugField',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='smallIntegerField',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='textField',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='timeField',
            field=models.TimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='urlField',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='uuiField',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Model3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigIntegerField', models.BigIntegerField()),
                ('many2many', models.ManyToManyField(blank=True, related_name='model3_many2many', to='users.Model6')),
            ],
        ),
        migrations.CreateModel(
            name='Just_one_field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField()),
                ('edward', models.BooleanField(blank=True, null=True)),
                ('many2many', models.ManyToManyField(blank=True, related_name='just_one_field_many2many', to='users.Model4')),
                ('one2one', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='just_one_field_one2one', to='users.Model5')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='foreignKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_foreignKey', to='users.Just_one_field'),
        ),
        migrations.AddField(
            model_name='user',
            name='one2oneField',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_one2oneField', to='users.Model3'),
        ),
    ]
