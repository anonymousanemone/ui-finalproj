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
@app.route('/learn/<int:lesson_num>', methods=['GET', 'POST'])
def learn(lesson_num):
    return render_template('learn.html', lesson_num=lesson_num)

# Quiz route
@app.route('/quiz/<int:question_num>', methods=['GET', 'POST'])
def quiz(question_num):
    return render_template('quiz.html', question_num=question_num)

if __name__ == '__main__':
    app.run(debug=True)