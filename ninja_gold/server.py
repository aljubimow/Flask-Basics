from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'gold_count' not in session:
        session['gold_count']=0
    if 'activity' not in session:
        session['activity']=[]
    return render_template("index.html")

@app.route('/process_money',methods=['POST'])
def process_money():
    if request.form['location']==farm:
        print (request.form['location'])
        gold_earned=random.randint(10,21)
        session['gold_count']=session['gold_count'] + gold_earned
        newstr='Earned {} golds from the {}.'.format(gold_earned,request.form['location'])
        session['activity'].append(newstr)
   
    elif request.form['location']==cave:
        print (request.form['location'])
        gold_earned=random.randint(5,11)
        session['gold_count']=session['gold_count'] + gold_earned
        newstr='Earned {} golds from the {}.'.format(gold_earned,request.form['location'])
        session['activity'].append(newstr)    

    elif request.form['location']==house:
            print (request.form['location'])
            gold_earned=random.randint(2,6)
            session['gold_count']=session['gold_count'] + gold_earned
            newstr='Earned {} golds from the {}.'.format(gold_earned,request.form['location'])
            session['activity'].append(newstr)

    elif request.form['location']==casino:
            print (request.form['location'])
            gold_earned=random.randint(-50,50)
            session['gold_count']=session['gold_count'] + gold_earned
            if gold_earned >= 0:
                newstr='Earned {} golds from the {}.'.format(gold_earned,request.form['location'])
            else:
                newstr='Lost {} golds from the {}.'.format(gold_earned,request.form['location']) 
            session['activity'].append(newstr)
    
    return redirect('/')

app.run(debug=True)
