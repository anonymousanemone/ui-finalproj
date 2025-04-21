from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

# Home route
@app.route('/')
def home():
    # session.clear()
    return render_template('index.html')

@app.route('/three-tab')
def threetab():
    # session.clear()
    return render_template('three-tab.html')
@app.route('/mc-choice')
def mcchoice():
    # session.clear()
    return render_template('mc-choice.html')
@app.route('/drag-drop')
def dragdrop():
    # session.clear()
    return render_template('drag-drop.html')

# Start learning process
# @app.route('/start')
# def start():
#     session['learning_progress'] = {}
#     session['quiz_answers'] = {}
#     return redirect(url_for('learn', lesson_num=1))

# Learning route
@app.route('/learn/1', methods=['GET', 'POST'])
def learn_1():
    return render_template('learn.html')

@app.route('/learn/2')
def learn_2():
    return render_template('learn_2.html')

@app.route('/learn/eggs')
def learn_eggs():
    return render_template(
        'learn_template.html',
        title="EGGS!",
        uses=[
            {"text": "Binding", "link": "#"},
            {"text": "Leavening", "link": "#"},
            {"text": "Moisture", "link": None},
            {"text": "Richness", "link": None},
        ],
        note="click on the word for a definition!",
        image="/static/images/eggs_mixing.jpg",
        back_link="/learn/2"
    )

@app.route('/learn/dairy')
def learn_dairy():
    return render_template(
        'learn_template.html',
        title="DAIRY!",
        uses=[
            {"text": "Creaminess", "link": "#"},
            {"text": "Moisture", "link": "#"},
            {"text": "Flavor", "link": None},
            {"text": "Richness", "link": None},
        ],
        note="click on the word for a definition!",
        image="/static/images/dairy.jpg",
        back_link="/learn/2"
    )

@app.route('/learn/gluten')
def learn_gluten():
    return render_template(
        'learn_template.html',
        title="GLUTEN!",
        uses=[
            {"text": "Structure", "link": "#"},
            {"text": "Elasticity", "link": "#"},
            {"text": "Chewiness", "link": None},
            {"text": "Binding", "link": None},
        ],
        note="click on the word for a definition!",
        image="/static/images/gluten.jpg",
        back_link="/learn/2"
    )

# Quiz route
@app.route('/quiz/<int:question_num>', methods=['GET', 'POST'])
def quiz(question_num):
    return render_template('quiz.html', question_num=question_num)

if __name__ == '__main__':
    app.run(debug=True)