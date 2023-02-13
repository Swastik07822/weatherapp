from flask import Flask, app, render_template, url_for, request
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from E import get_weather
import asyncio
app = Flask(__name__)

'''@app.route("/")
def home():
    #if request.method == 'POST':
        #place =  request.form.get('City')
        #print(result)
    return render_template('home.html')'''
	#return render_template('home.html')
@app.route('/', methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        city =  request.form['City']
        result = asyncio.run(get_weather(city))
        print(result)
        return render_template('home.html', result= result)
    return render_template('home.html', message = 'Done')
if __name__ == '__main__':
   app.run(debug=True)