from flask_admin.contrib.peewee import ModelView
from db import UserInfo


class UserAdmin(ModelView):
    inline_models = (UserInfo,)