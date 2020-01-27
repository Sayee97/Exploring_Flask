from flask import Flask,request
from flask_restful import Api,reqparse
from flask_jwt import JWT,jwt_required,timedelta
from security import authenticate, identity
from user import UserRegister

from item import Item,ItemList
app=Flask(__name__)
app.secret_key='jose'
api=Api(app)


# app.config['JWT_AUTH_URL_RULE'] = '/login' 
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
jwt = JWT(app, authenticate, identity)


#jwt=JWT(app,authenticate,identity) #/auth

#SAme as @route ==this add_resource 2nd parameter
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
	app.run(port=5000,debug=True)