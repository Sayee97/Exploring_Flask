from flask import Flask,request
from flask_restful import Api,reqparse
from flask_jwt import JWT,jwt_required,timedelta
from security import authenticate, identity
from resources.user import UserRegister
from db import db
from resources.item import Item,ItemList
from resources.store import Store,StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='jose'
api=Api(app)

@app.before_first_request
def create_tables():
	db.create_all()


# app.config['JWT_AUTH_URL_RULE'] = '/login' 
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
jwt = JWT(app, authenticate, identity)


#jwt=JWT(app,authenticate,identity) #/auth

#SAme as @route ==this add_resource 2nd parameter
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__=='__main__':
	db.init_app(app)
	app.run(port=5000,debug=True)