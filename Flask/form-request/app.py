# --------------------------------------------------- #
# Send a request to a Flask route through a HTML form #
# --------------------------------------------------- #

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # route must be the same as form action
def index():
    
    # Display default content when accessing via get
    if request.method == "GET":
        return render_template("index.html", username="world")
    
    # Customize content based on request
    elif request.method == "POST":
        username = request.form.get("username") # retrieve value using the input's name parameter
        return render_template("index.html", username=username)
    
    return render_template("index.html", username="world")


if __name__ == '__main__':
    app.run(debug=True)