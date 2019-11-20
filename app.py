from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from db import User, UserInfo, Pokemon, db
from admin import UserAdmin


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'

@app.route('/')
def index():
    return '1'


# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(Pokemon))
app.run()