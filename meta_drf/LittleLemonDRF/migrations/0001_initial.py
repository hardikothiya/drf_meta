# Generated by Django 4.1.5 on 2023-01-11 09:56

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
                ('total_items', models.IntegerField(default=2)),
                ('total_cost', models.FloatField(default=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart_user', to=settings.AUTH_USER_MODEL)),
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
                ('categorey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='LittleLemonDRF.categorey')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=22, max_digits=6)),
                ('is_delivered', models.BooleanField(default=False)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='LittleLemonDRF.cart')),
                ('delivery_crew', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_crew', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField()),
                ('price', models.FloatField(default=1)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartitem_set', to='LittleLemonDRF.cart')),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonDRF.menuitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'menuitem')},
            },
        ),
    ]
