# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# Flask Setup
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('form.html')

@app.route('/', methods=['POST', 'GET'])
def address():
    error = None
    if request.method == 'POST':
        if valid_address(request.form['userAddress']:
            return (request.form['userAddress'])
        else:
            error = 'Address Not Found'
    # the code below is executed if the request method
    # was GET or the address was invalid
    return render_template('form.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)
