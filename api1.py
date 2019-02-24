from flask import Flask, render_template, request, redirect, url_for, session
from model import check_user,create_user,log_user,check_product,create_product,seller_products,buyer_products,cart_page,update_cart,remove_from_cart
app = Flask(__name__)
app.config['SECRET_KEY']='hello'
login = None
user=None

@app.route("/")
def home():
	#if session.get('username'):
	#	return render_template('home.html',user = session['username'])
	#else:
		return render_template('home.html')
    
    


@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route('/login' ,methods = ['GET','POST'])
def login():
	if request.method=='POST':


		uname = request.form['username']
		password = request.form['password']
		result = log_user(uname)

		if check_user(uname):


			if password ==result['password']:
				session['username']=result['username']
				session['type']=result['c_type']
				return redirect(url_for('welcome'))
			return "enter the correct password"
		return "user doesn't exist"

		#return "login failed"
	#login=False
	return redirect(url_for('home'))
	#return render_template('home.html')
	#return redirect(url_for('home'))

@app.route('/signup',methods=['GET','POST'])
def signup():

	if request.method == 'POST':
		user_info={}

		user_info['username'] = request.form['username']
		user_info['email'] = request.form['email']
		user_info['password']= request.form['password']
		rpassword = request.form['rpassword']
		user_info['c_type'] = request.form['ctype']
		if user_info['c_type']=='buyer':
			user_info['cart']=[]


		if check_user(user_info['username']) is False:
			if rpassword == user_info['password']:
				create_user(user_info)
				return "User id is created."
			else:
				return "password dont match"
		else:
			return "user already exists. Please chose a different username"



	return render_template('signup.html')
	



	
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))

@app.route('/add_products', methods=['GET','POST'])
def add_products():
	if request.method =='POST':
		product_info={}

		product_info['name']= request.form['name']
		product_info['description']=request.form['product']
		product_info['price']=int(request.form['price'])
		product_info['seller_name']=session['username']

		if check_product(product_info['name']):

			return "product already exists"
		create_product(product_info)
		return redirect(url_for('home'))

	return render_template('add_products.html')

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/products')
def products():
	products = buyer_products()
	return render_template('products.html', products=products)

@app.route('/sellerproducts')
def sell_products():

	products=seller_products(session['username'])
	return render_template('products.html',products=products)

@app.route('/add_cart',methods=['POST'])
def add_cart():
	product_id=request.form['product_id']
	update_cart(session['username'],product_id)
	return(redirect(url_for('cart')))

@app.route('/cart')
def cart():
	products= cart_page(session['username'])
	return render_template('cart_page.html',products=products)

@app.route('/remove_cart',methods=['POST'])
def remove_cart():
	product_id=request.form['product_id']
	remove_from_cart(session['username'],product_id)
	return(redirect(url_for('cart')))



		



if __name__ == '__main__':
	app.run(debug="True")