from flask import Flask, jsonify, request
import json
app=Flask(__name__)

languages=[{'name': 'Japanese', 'traits':'easy'}, {'name': 'Chinese','traits':'difficult'}]
lang=[]
@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnall():
	print languages[0]
	return jsonify ({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	
	for elem in languages:
		if elem['name']==name or elem['traits']==name:
			lang.append(elem)

	return jsonify ({'languages': lang[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	data=request.data
	data=json.loads(data)
	languages.append(data)
	return jsonify ({'languages': languages})



if __name__== '__main__':
	app.run(debug=True, port=8080)
