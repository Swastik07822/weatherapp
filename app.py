from flask import Flask, app, render_template, request
from E import get_weather
import asyncio
app = Flask(__name__)

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
