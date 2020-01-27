
# Exploring_Flask
HTTP Verbs: del, put, post, get
Stateless concept
Postman
Postman is a great tool to try RESTful APIs

# /Flask_RESTful_an_Flask_Extension
Add resource
a.	api.add_resource(Item,'/item/string:name')
b.	For URL http://127.0.0.1:5000/item/topaz
Create Item class and inherit Resource class
a. class Item(Resource)
add http verbs inside this item class
Always return a dictionary. FLASKRestful converts into json by internal jsonify()
How to use JWT: https://pythonhosted.org/Flask-JWT/ (JSON Web Token for authorization)
