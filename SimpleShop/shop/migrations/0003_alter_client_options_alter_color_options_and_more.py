# Generated by Django 4.1.6 on 2023-02-14 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_client_alter_stuff_phone_alter_supplier_supp_phone"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "مشتری", "verbose_name_plural": "مشتریان"},
        ),
        migrations.AlterModelOptions(
            name="color",
            options={"verbose_name": "رنگ", "verbose_name_plural": "رنگ ها"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "محصولات", "verbose_name_plural": "محصولات"},
        ),
        migrations.AlterModelOptions(
            name="size",
            options={"verbose_name": "اندازه", "verbose_name_plural": "اندازه ها"},
        ),
        migrations.AlterModelOptions(
            name="stuff",
            options={"verbose_name": "پرسنل", "verbose_name_plural": "پرسنل"},
        ),
        migrations.AlterModelOptions(
            name="supplier",
            options={
                "verbose_name": "تامین کننده",
                "verbose_name_plural": "تامین کنندگان",
            },
        ),
    ]
