from flask import Flask
    

app = Flask(__name__)

@app.route("/") # / means that we what to see the homepage
def hello_world():
    return "<h1 style='background:blue'>Hello, World!</h1>" \
           "<p>This is the text</p>" \
           "<img src='https://i.pinimg.com/originals/9a/3c/3f/9a3c3fb5f73822af8514df07f6676392.gif'></img>"

@app.route('/greet/<name>')
def hello_user(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)