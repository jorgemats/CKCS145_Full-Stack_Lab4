from flask import Flask, jsonify, request, json, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'GET':
		data = "hello world"
		return jsonify({'data': data})
		
	if request.method == 'POST':
		data = request.get_json()
		return jsonify(data)

@app.route('/home', methods = ['GET'])
def home2():
	return render_template('test.html') #renders the html form when client url is set to /home
		
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
	return jsonify({'data': num**2})
	
@app.route('/test', methods = ['POST']) #this route uses the html form as an input
def test():
	if request.method == 'POST':
		data_id = request.form.get('Id')
		data_customer = request.form.get('Customer')
		data_quantity = request.form.get('Quantity')
		data_price = request.form.get('Price')
		print('Id: ', data_id)
		print('Customer: ', data_customer)
		print('Quantity: ', data_quantity)
		print('Price: ', data_price)
		return jsonify({'data': 'success'}) #returning a JSON object

@app.route('/test2', methods = ['POST']) #this route accepts the JSON object as input
def test2():
	if request.method == 'POST':
		content = request.json
		print(content)
		print('Id:', content['Id'])
		print('Customer:', content['Customer'])
		print('Quantity:', content['Quantity'])
		print('Price:', content['Price'])
		return jsonify({'data': 'success'}) #returning a JSON object
	
app.run()
