from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def submit_info():
    name = request.form['name']
    language = request.form['language']
    location=request.form['location']
    comment=request.form['comment']
    return render_template("results.html", language=language, location=location, name=name, comment=comment)
	 

app.run(debug=True)

