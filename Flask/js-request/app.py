# --------------------------------------------------------- #
# Send request from JavaScript, passing information as JSON #
# --------------------------------------------------------- #

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Default route, displayed
@app.route('/')
def home():
    return render_template('index.html')

# Route for processing request, never displayed
# This allows to update the default page through Javascript, without refreshing it like in form submissions
@app.route('/process', methods=['GET', 'POST'])
def get_prompt():
    input = request.json.get('number') # retrieve value using key set in JS
    output = 'You entered ' + input
    # print('output.text', output["text"], type(output.text), type(output["text"]))
    return jsonify({'output': output}) # create JSON for the result of the request

if __name__ == '__main__':
    app.run(debug=True)