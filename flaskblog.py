from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "title": "Blog Post 1",
        "author": "Abhilash",
        "content": "This the first blog post",
        "date_posted": "17 May, 2020"
    },
    {
        "title": "Blog Post 2",
        "author": "Abhilash",
        "content": "This the second blog post",
        "date_posted": "18 May, 2020"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts, title = 'Abhilash')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__' :
    app.run(debug=True)
