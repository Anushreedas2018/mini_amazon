from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

login = None
user=None

@app.route("/")
def home():
    return render_template('home.html',user=user,login=login)
    


@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route('/login' ,methods = ['GET','POST'])
def login():
	if request.method=='POST':
  	
		vishak = {'uname':'vishak','password':'12345'}

		uname = request.form['username']
		password = request.form['password']

		if vishak['uname']==uname and vishak['password']==password:
			#return "login successful.welcome"
			login=True
			user={'uname':'vishak','password':'12345'}
			return redirect(url_for('home'))
		#return "login failed"
	login=False
	return redirect(url_for('home'))
	return render_template('home.html')
	#return redirect(url_for('home'))



app.run(debug="True")