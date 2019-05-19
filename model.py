from pymongo import MongoClient
from bson.objectid import ObjectId

client= MongoClient()
db = client['mini_amazon']

def check_user(username):

	query = {"username":username}
	results = db['users'].find(query)


	if results.count()>0:
		return True
	return False

def create_user(user_info):
	db['users'].insert_one(user_info)

def log_user(username):
	query={"username":username}
	results=db['users'].find_one(query)
	print(results)
	return results


def check_product(product_name):
	query={"name":product_name}
	results=db['products'].find(query)
	if results.count()>0:
		return True
	else:
		return False
	


def create_product(product_info):
	db['products'].insert_one(product_info)

def buyer_products():

	results=db['products'].find({})
	return results

def seller_products(username):
	query ={"seller_name":username}
	results =db['products'].find(query)

	return results


def update_cart(username,product_id):
	db['users'].update({"username":username},{"$addToSet":{"cart":{"$each":[product_id]}}})
	db['users'].update({"username":username},)

def remove_from_cart(username,product_id):
	db['users'].update({"username":username},{"$pull":{"cart":product_id}})


def cart_page(username):

	query={"username":username}
	results= db['users'].find_one(query)
	product_ids=results['cart']
	products=[]
	for product_id in product_ids:
		query={"_id":ObjectId(product_id)}
		results= db['products'].find_one(query)
		products.append(results)

	return products