#The Great Number Game
from flask import Flask, render_template, session, request, redirect
import random
app = Flask (__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['random_number'] = random.randrange(0, 101)
    print (session['random_number'])
    return render_template('index.html')

@app.route('/guess', methods=['Get','Post'])
def guessed_number():
    guess=int(request.form['number'])
    if guess > session['random_number']:
        color = "red"
        message = "TOO HIGH !!!"
    elif guess < session['random_number']:
        color = "red"
        message = "TOO LOW !!!"
    elif guess == session['random_number']:
        color = "green"
        message = str(session['random_number']) + " WAS THE NUMBER !!!"
    return render_template('index.html', message=message, color=color)

app.run(debug=True)