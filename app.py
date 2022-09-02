from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    #return 'Hello, World!'

@app.route("/about")
def about():
    return render_template('about.html')
# @app.route('/products')
# def products():
#     return 'this is product page'

if __name__ == "__main__":
    app.run(debug=True)