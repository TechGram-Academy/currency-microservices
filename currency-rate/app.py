# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

currency_to_inr = {
	'usd': 81,
	'pound': 100,
	'taka': 0.8,
	'cad': 60
}

@app.route('/', methods = ['GET'])
def home():
	return jsonify({'message': "please use /currency-rate?currency=<currency>"})


@app.route('/currency-rate', methods = ['GET'])
def currency_rate():
	currency = request.args.get('currency')

	value = currency_to_inr[currency]
	return jsonify({'value': value})



# driver function
if __name__ == '__main__':
	app.run(debug = True)
