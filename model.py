# -*- coding: utf-8 -*-

from peewee import *
import datetime
import settings

if settings.DBENGINE.lower() == 'mysql':
    database = MySQLDatabase(
        settings.DBNAME,
        host=settings.DBHOST,
        port=settings.DBPORT,
        user=settings.DBUSER,
        passwd=settings.DBPASSWORD,
        charset='utf8',
        use_unicode=True,
    )

elif settings.DBENGINE.lower() == 'sqlite3':
    database = SqliteDatabase(settings.DBNAME)

elif settings.DBENGINE.lower() == 'postgresql':
    database = PostgresqlDatabase(
        settings.DBNAME,
        user=settings.DBUSER,
        password=settings.DBPASSWORD,
        host=settings.DBHOST,
        charset='utf8',
        use_unicode=True,
    )

else:
    raise AttributeError("Please setup datatbase at settings.py")


class BaseModel(Model):
    class Meta:
        database = database


class Community(BaseModel):
    id = BigIntegerField(primary_key=True)
    title = CharField()
    link = CharField(unique=True)
    district = CharField()
    busicircle = CharField()
    tagList = CharField()
    onsale = CharField()
    onrent = CharField(null=True)
    builtyear = CharField(null=True)
    builttype = CharField(null=True)
    wuyecost = CharField(null=True)
    servcomp = CharField(null=True)
    builtcomp = CharField(null=True)
    buildingnum = CharField(null=True)
    housenum = CharField(null=True)
    price = CharField(null=True)
    followers = IntegerField(null=True)
    dealin90 = IntegerField(null=True)
    validdate = DateTimeField(default=datetime.datetime.now)


class Houseinfo(BaseModel):
    houseID = CharField(primary_key=True)
    title = CharField()
    link = CharField()
    community = CharField()
    years = CharField()
    housetype = CharField()
    square = CharField()
    direction = CharField()
    floor = CharField()
    taxtype = CharField()
    totalPrice = CharField()
    unitPrice = CharField()
    followInfo = CharField()
    decoration = CharField()
    validdate = DateTimeField(default=datetime.datetime.now)


class Hisprice(BaseModel):
    houseID = CharField()
    totalPrice = CharField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        primary_key = CompositeKey('houseID', 'totalPrice')


class Sellinfo(BaseModel):
    houseID = CharField(primary_key=True)
    title = CharField()
    link = CharField()
    community = CharField()
    years = CharField()
    housetype = CharField()
    square = CharField()
    direction = CharField()
    floor = CharField()
    status = CharField()
    source = CharField()
    totalPrice = CharField()
    unitPrice = CharField()
    dealdate = CharField(null=True)
    updatedate = DateTimeField(default=datetime.datetime.now)


class Rentinfo(BaseModel):
    # 由于网页中未找到房子id,故不用该项:utf-8
    # houseID = CharField(primary_key=True)
    title = CharField()
    link = CharField()
    region = CharField()
    zone = CharField()
    meters = CharField()
    shitingwei = CharField()
    price = CharField()
    updatedate = DateTimeField(default=datetime.datetime.now)


def database_init():
    database.connect()
    database.create_tables(
        # [Community, Houseinfo, Hisprice, Sellinfo, Rentinfo], safe=True)
        [Community], safe=True)
    database.close()
