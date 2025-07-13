from flask import Flask, jsonify, request
# create an app
app = Flask(__name__)

# define the route
@app.route("/")
def home():
    return "🚀 Hello, Flask! Welcome to your first route."
@app.route("/about")
def about():
    return "This is a Flask App."
@app.route("/greet/<name>")
def greet(name):
    # return f"Hello, {name.capitalize()}!"
    return jsonify({"name": name, "status":"active"})
@app.route("/search")
def search():
    term = request.args.get('term', 'ras')
    limit = request.args.get('limit',10)
    return f"searching for '{term}' limit '{limit}'"
@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    return jsonify({
        "message":f"receive data for {name} and {age}",
        "status":"Success"
    })


# run the app
if __name__== "__main__":
    app.run(debug=True)



