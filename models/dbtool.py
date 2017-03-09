from peewee import *

db = SqliteDatabase('mdmpy.db')


class Torrents(Model):
    title = CharField()

    class Meta:
        database = db


class Music(Model):
    title = CharField()
    artist = CharField()
    album = CharField(null=True)
    ext_id = CharField(unique=True)
    downloaded = BooleanField(default=False)
    local_path = CharField(null=True)
    torrent = ForeignKeyField(Torrents, null=True)
    allow_youtube = BooleanField(default=False)
    quality = CharField()

    class Meta:
        database = db


class Games(Model):
    title = CharField()
    ext_id = CharField(unique=True)
    downloaded = BooleanField(default=False)
    local_path = CharField()
    torrent = ForeignKeyField(Torrents)

    class Meta:
        database = db


class Books(Model):
    title = CharField()
    ext_id = CharField(unique=True)
    downloaded = BooleanField(default=False)
    local_path = CharField()
    torrent = ForeignKeyField(Torrents)

    class Meta:
        database = db


class Settings(Model):
    key = CharField(unique=True)
    value = CharField()

    class Meta:
        database = db


class Indexers(Model):
    url = CharField(unique=True)
    type = CharField(default="torznab")
    api_key = CharField(null=True)

    class Meta:
        database = db


def initializeDatabase():
    db.connect()
    if not Music.table_exists():
        db.create_tables([Music, Games, Books, Settings, Torrents, Indexers])

