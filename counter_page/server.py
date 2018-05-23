# Counter of Visitors
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
        #set session counter to zero
    session["count"] +=1
    #adds 1 when refreshed
    return render_template('index.html')
    
@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    #adds 2 when button is clicked
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)