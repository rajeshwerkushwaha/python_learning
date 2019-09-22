from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'd9e4cf2deb535ff245a08a6ae8459863'


posts = [
	{
		'author': 'Rajesh Kumar',
		'title': 'Blog Post 1',
		'content': 'Fist post content',
		'date_posted': 'Sep 21, 2019'
	},
	{
		'author': 'Sheetal Maurya',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'Sep 21, 2019'
	},
	{
		'author': 'Deepak Khatri',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'Sep 21, 2019'
	},
	{
		'author': 'Bindiya Khatri',
		'title': 'Blog Post 4',
		'content': 'Fourth post content',
		'date_posted': 'Sep 21, 2019'
	},
	{
		'author': 'Mukesh Kumar',
		'title': 'Blog Post 5',
		'content': 'Fifth post content',
		'date_posted': 'Sep 21, 2019'
	}
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)



# run the app
if __name__ == '__main__':
    app.run(debug=True)