from flask import Flask,jsonify,request,render_template

app = Flask(__name__) #each file unique name
stores=[
	{
		'name':"SayeeBookstore",
		'items':[
				{
				'name':"Alchemist",
				'price':15.99
				}

		]
	}



]


@app.route('/')
def home():
	return render_template('index.html')
#post: receive data
#get:use to send data


#POST store name{name:}

@app.route('/store',methods=['POST'])
def create_store():
	request_data=request.get_json()
	new_store={
	'name':request_data['name'],
	'items':[]

	}
	stores.append(new_store)
	return jsonify(new_store)
#get /store/string name
@app.route('/store/<string:name>')
def get_store(name):
	#iterate over stores
	for store in stores:
		if store['name']==name:
			return jsonify(store)
	return jsonify({'message':'store not found'})
#get /store
@app.route('/store')
def get_stores():
	return jsonify({'stores':stores})
#post store name,price

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
	request_data=request.get_json()
	for store in stores:
		if store['name']==name:
			new_item={
			'name':request_data['name'],
			'price':request_data['price']
			}
		store['items'].append(new_item)
		return jsonify(new_item)
	return jsonify({'message':'store not found'})

#get name
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
	for store in stores:
		if store['name']==name:
			return jsonify({'items':store['items']})
	return jsonify({'message':'store item not found'})
app.run(port=5000)


