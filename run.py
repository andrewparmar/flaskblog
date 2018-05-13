from flaskblog import app

if __name__ == "__main__":
	app.run(debug=True)


########################################################################
# Unused Routes
########################################################################

# @app.route('/api/v1/posts', methods=['GET', 'POST'])
# def posts_get():
# 	if request.method == 'POST':
# 		some_json = request.get_json()
# 		print(json.dumps(some_json, indent=4))
# 		posts.append(dict(some_json))
# 		return jsonify(some_json), 201
# 	return jsonify(posts), 201