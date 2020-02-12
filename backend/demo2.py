from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", avatar = "https://avatar.csdn.net/F/4/9/2_zhao4zhong1.jpg")

@app.route("/<is_login>/")
def login(is_login):
	if is_login == "1":
		userinfo = {
			"username" : "muhaha",
			"age" : "23"
		}
		return render_template("login.html", user = userinfo)
	else:
		return render_template("login.html")

@app.route("/main/")
def main():
	books = [
		{
			"name" : "Harry Potter",
			"author" : "J.K Rollin",
			"price" : "109"
		},
		{
			"name" : "Great Expectation",
			"author" : "Dickons",
			"price" : "50"
		}
	]
	return render_template("main.html", books = books)


if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)
	