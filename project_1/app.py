import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from flask import Flask,render_template,request
import requests


engine = create_engine('postgresql://postgres:arpit@localhost/project1')
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)


@app.route("/")
def index():
	users = db.execute("SELECT * from users").fetchall()
	return render_template("login_page.html",users = users)

@app.route("/register")
def registration():
	return render_template("registration.html")

@app.route("/user",methods = ["POST"])
def successful():
	name = request.form.get("name")
	print(name)
	password = request.form.get("password")
	print(password)
	user = db.execute("SELECT * FROM users WHERE user_id = :name",{"name":name})
	name = name.capitalize() 
	if user.rowcount == 0:
		return render_template("error.html",message = "No such ID exist!")
	if user.fetchone().password!= password:
		return render_template("error.html",message = "Wrong ID or Password")
		
	return render_template("search.html",run_it = 0,name = name)
	

@app.route("/saved",methods = ["POST"])
def saveit():
	name = request.form.get("name")
	password = request.form.get("password")
	print(name,password)
	db.execute("INSERT INTO users (user_id, password) VALUES (:user_id,:password)",{"user_id":name,"password":password})
	db.commit()
	# db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",{"name": name, "flight_id": flight_id})
	return render_template("success.html",message = "saved successfully")



@app.route("/search/<string:user_id>",methods=["POST","GET"])
def search(user_id):
	print(user_id)
	if request.method == "POST":
		isbn = request.form.get("isbn")
		author = request.form.get("author")
		if author == "":
			print("author is none")
		print(author)
		title = request.form.get("title")
		if title =="":
			print("title is None")
		print(title)
		isbn = '%' + isbn + '%'
		title = '%' + title + '%'
		author = '%' + author + '%'
		books = db.execute("SELECT * FROM books WHERE isbn like :isbn AND title like :title AND author like :author",{"isbn":isbn,"title":title,"author":author}).fetchall()
		book_found = 1
		if db.execute("SELECT * FROM books WHERE isbn like :isbn AND title like :title AND author like :author",{"isbn":isbn,"title":title,"author":author}).rowcount == 0:
			book_found =0
		
		return render_template("search.html",books =books,run_it = 1,name = user_id,book_found=book_found)

@app.route("/search/<string:user_id>/<string:isbn>")
def book(isbn,user_id):
	book = db.execute("SELECT * FROM books WHERE isbn = :isbn",{"isbn":isbn}).fetchone()
	if book is None:
		return render_template("success.html",message ="No book is there !!")

	res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "gt77o8xriOCaqk0SrGcA", "isbns": isbn}).json()
	print(res)
	if db.execute("SELECT * FROM reviews WHERE isbn = :isbn AND user_id = :user_id",{"isbn":isbn,"user_id":user_id}).rowcount == 0:
		return render_template("book.html",book = book,user_id = user_id,review = 1,average_rating = res['books'][0]['average_rating'],reviews_count=res['books'][0]['reviews_count'])
	else:
		print("already reviewed")
		review = db.execute("SELECT * FROM reviews WHERE isbn = :isbn AND user_id = :user_id",{"isbn":isbn,"user_id":user_id}).fetchone()
		return render_template("book.html",book = book,review_user = review,user_id = user_id,review = 0,average_rating = res['books'][0]['average_rating'],reviews_count=res['books'][0]['reviews_count'])
@app.route("/submitted/<string:user_id>/<string:isbn>",methods = ["POST"])
def submit(user_id,isbn):
	rating = request.form.get("rating")
	comment = request.form.get("review")
	print(rating,comment)
	db.execute("INSERT INTO reviews (user_id,isbn,rating,comment) VALUES (:user_id,:isbn,:rating,:comment)",{"user_id":user_id,"isbn":isbn,"rating":rating,"comment":comment})
	db.commit()
	return render_template("success.html")
app.run(debug = True)


