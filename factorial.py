"""
This is a Flask application that calculates the factorial of a number. 
The app has been seeded with various bugs, and thus it's an ideal test exercise for interviewing QA engineers. 
"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calculate_factorial(n):
    "Calculate the factorial of a number"
    if n==0:
        return 1
    else:
        return n*calculate_factorial(n-1)

@app.route("/", methods=['GET', 'POST'])
@app.route("/factorial", methods=['GET', 'POST'])
def factorial():
    "Endpoint for calculating the factorial of a number"
    if request.method == 'GET':
        #return the form
        return render_template('factorial.html')
    if request.method == 'POST':
        #return the answer
        number = int(request.form.get('number'))
        result = calculate_factorial(number)
        api_response = {"answer": result}
        return jsonify(api_response)

@app.route("/terms")
def terms_and_conditions():
    "Return Terms and Conditions statement"
    return "This is the Terms and Conditions page. Stay tuned!"

@app.route("/privacy")
def privacy():
    "Return Privacy statement"
    return "This is the Privacy page. Stay tuned!"

@app.route("/scrt")
def scrt():
    "Return Secret page"
    return "Congratulations! You've found the secret page. Here's a link to the source code: https://github.com/mjparker/factorial-test-app Go find some more bugs :)"
    

#---START OF SCRIPT
if __name__ == '__main__':
    app.run(debug= True)