from flask import Flask, url_for, redirect
		
app = Flask(__name__)

# @app.route("/")
# def index():
# 	print(url_for("my_list"))
# 	print(url_for("article", id = "abc"))
# 	return "Hello, Flask!"

@app.route("/")
def index():
	# using reverse url method to get website address
	# or we can redirect("/login/")
	login_url = url_for('login')
	return redirect(login_url)
	return "This is main page"

@app.route("/login/")
def login():
	return "This is login page"

@app.route("/comment/<is_login>/")
def comment(is_login):
	if is_login == "1":
		return "This is comment page"
	else :
		return redirect(url_for('login')) 

# @app.route("/list/")
# def my_list():
# 	return "list"

# @app.route("/article/<id>")
# def article(id):
# 	return "The request parameter: %s" %id

if __name__ == "__main__":
	app.run(debug = True)
