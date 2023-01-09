# Generated by Django 4.1.5 on 2023-01-09 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('featured', models.BooleanField(db_index=True, default=False)),
                ('categorey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LittleLemonDRF.categorey')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=22, max_digits=6)),
                ('delivery_crew', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery_crew', to=settings.AUTH_USER_MODEL)),
                ('order_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonDRF.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='menuitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonDRF.menuitem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonDRF.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unit_price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price_1', to='LittleLemonDRF.menuitem')),
            ],
            options={
                'unique_together': {('order', 'menuitem')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('menuitem', 'user')},
        ),
    ]
