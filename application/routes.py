from flask import render_template
from application import app
from application.models import Posts

@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
	return render_template('home.html', title='Home', posts=postData)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/books')
def books():
	return render_template('books.html', title='Books')

@app.route('/reviews')
def reviews():
	return render_template('reviews.html', title='Reviews')

@app.route('/login')
def login():
	return render_template('login.html', title='Login')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')

dummyData = [
	{
		"name": {"first":"Chester", "last":"Gardner"},
		"title":"First Post",
		"content":"This is some dummy data for Flask lectures"
	},
	{
		"name": {"first":"Chris", "last":"Perrins"},
		"title":"Second Post",
		"content":"This is even more dummy data for Flask lectures"
	}
]
