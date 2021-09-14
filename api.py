from flask import Flask, jsonify
from flask_restful import Api, Resource
import json

app = Flask(_name_)
api = Api(app)

file = open("data.json")
data = json.load(file)

@app.route('/users', methods=['GET'])
def users():
    return jsonify(data)



class UserAPI (Resource):
	def get(self, id):
		for user in data:
			if user["id"] == id:
				return jsonify(user)
		else:
			return(jsonify({
				"message" : "404: User not found!"
				}))

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')


if _name_ == "_main_":
	app.run(host='0.0.0.0', port=5001)
