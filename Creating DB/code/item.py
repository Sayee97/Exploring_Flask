from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required

class Item(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('price', type=float, required=True,help="Field Cannot be Blank")

	@classmethod
	def find_by_name(cls,name):
		print(name,"NAME")
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query="SELECT * FROM items WHERE name=?"
		result=cursor.execute(query,(name,))
		row=result.fetchone()
		print(row)
		connection.close()
		if row:
			return {'item':{'name':row[0],'price':row[1]}}


	@jwt_required()
	def get(self,name):
		#print(name)
		item=self.find_by_name(name)
		#print(item)
		if item:
			return item
		return {'message':'Item not found'},404


	def post(self,name):
		if self.find_by_name(name):

			return {'message':"An item with name '{}' already exists".format(name)},400

		data=Item.parser.parse_args()
		item={'name':name,'price':data['price']}
		try:
			self.insert(item)
		except:
			return {"message":"An error occured while inserting an item"},500 #int server error

		return item,201


	@classmethod
	def insert(cls,item):

		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()

		query="INSERT INTO items VALUES (?,?)"
		cursor.execute(query,(item['name'],item['price'],))

		connection.commit()
		connection.close()

	
	def delete(self,name):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()

		query="DELETE FROM items WHERE name = ?"
		cursor.execute(query,(name,))
		connection.commit()
		connection.close()
		return {'message':'Item deleted'}

	
	def put(self,name):
		
		data=Item.parser.parse_args()
		item=self.find_by_name(name)
		updatedItem={'name':name,'price':data['price']}


		if item is None:
			try:
				self.insert(updatedItem)
			except:
				return {"message":"cant insert item"}
		else:
			try:
				self.update(updatedItem)
			except:
				return {"message":"cant be updates"}

		return updatedItem
	@classmethod
	def update(cls,item):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()

		query="UPDATE items  SET price = ? WHERE name=?"
		cursor.execute(query,(item['price'],item['name']))
		connection.commit()
		connection.close()

class ItemList(Resource):
	def get(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()

		query="SELECT * from items"
		result=cursor.execute(query)
		items=[]
		for row in result:
			items.append({'name':row[0],'price':row[1]})
		connection.commit()
		connection.close()

		return {'items':items}