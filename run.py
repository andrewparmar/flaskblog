from flaskblog import app

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)


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