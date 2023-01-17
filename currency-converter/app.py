# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request,json
import requests

# creating a Flask app
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home(): 
	return jsonify({'message': "please use /currency-converter?currency=<currency>&amount=<amount>"})


@app.route('/currency-converter', methods = ['GET'])
def convert_currency():
    currency = request.args.get('currency')
    amount = request.args.get('amount') 


    # calling currency-rate API
    url = f"http://127.0.0.1:5000/currency-rate?currency={currency}"
    response = requests.request("GET", url)
    rate = int(json.loads(response.text)['value'])


    return jsonify({'amount':(amount*rate)})
    
    

# driver function
if __name__ == '__main__':
	app.run(debug = True, port=5001)
