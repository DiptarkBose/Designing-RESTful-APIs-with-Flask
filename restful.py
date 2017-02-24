from flask import Flask, jsonify, request
app=Flask(__name__)

languages=[{'name': 'Japanese', 'traits':'easy'}, {'name': 'Chinese','traits':'difficult'}]
@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnall():
	print languages[0]
	return jsonify ({'languages': languages})


if __name__== '__main__':
	app.run(debug=True, port=8080)