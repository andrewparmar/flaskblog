from flask import request, json
from flask_restful import Resource, Api
from flaskblog.database import posts

class PostSimple(Resource):
	
	def get(self):
		return posts

	def post(self):
		some_json = request.get_json()
		print(json.dumps(some_json, indent=4))
		posts.append(dict(some_json))
		return some_json

	def put(self):
		some_json = request.get_json()
		return some_json
