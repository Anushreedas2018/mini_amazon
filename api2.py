from flask import Flask,render_template,request,url_for
from funcs import weather_api

app=Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")


@app.route('/weater',methods=['POST'])
def weather_quote():
	city=request.form['city']
	weather=weather_api(city)
	return render_template('weather.html',city=city,weather=weather)

if __name__=='__main__':

	app.run(debug=True)
