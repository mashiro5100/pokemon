import peewee
from playhouse.dataset import MySQLDatabase


db = MySQLDatabase('pokemon', user='root', password='1198',  host='127.0.0.1', port=3307)


class BaseModel(peewee.Model):
    id = peewee.AutoField()

    class Meta:
        database = db


class Pokemon(BaseModel):

    name = peewee.CharField(max_length=128)

    class Meta:
        table_name = 'pokemon'


class User(BaseModel):
    username = peewee.CharField(max_length=80)
    email = peewee.CharField(max_length=120)

    class Meta:
        table_name = 'user'

    def __unicode__(self):
        return self.username


class UserInfo(BaseModel):
    key = peewee.CharField(max_length=64)
    value = peewee.CharField(max_length=64)

    user = peewee.ForeignKeyField(User)

    class Meta:
        table_name = 'user_info'

    def __unicode__(self):
        return '%s - %s' % (self.key, self.value)
