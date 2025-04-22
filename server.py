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
@app.route('/egg-swap')
def egg_swap():
    return render_template('egg-swap.html')

# Start learning process
# @app.route('/start')
# def start():
#     session['learning_progress'] = {}
#     session['quiz_answers'] = {}
#     return redirect(url_for('learn', lesson_num=1))

# Learning route
@app.route('/learn/1', methods=['GET', 'POST'])
def learn_1():
    # Render the specific template for /learn/1
    return render_template('learn.html')

@app.route('/learn/2', methods=['GET', 'POST'])
def learn_2():
    # Render the specific template for /learn/2
    return render_template('learn_2.html')

@app.route('/learn/<int:lesson_num>', methods=['GET', 'POST'])
def learn_lesson(lesson_num):
    lessons = {
        3: {
            "title": "EGGS!",
            "uses": [
                {"text": "Binding", "link": "#"},
                {"text": "Leavening", "link": "#"},
                {"text": "Moisture", "link": None},
                {"text": "Richness", "link": None},
            ],
            "note": "click on the word for a definition!",
            "image": "/static/images/eggs_mixing.jpg",
            "back_link": "/learn/2",
            "next_link": "/learn/4"
        },
        4: {
            "title": "Binding",
            "note": "Definition: The process of holding ingredients together to maintain structure and prevent crumbling",
            "image": "/static/images/eggs_mixing.jpg",
            "back_link": "/learn/3",
            "next_link": "/learn/5"
        },
        15: {
            "title": "DAIRY!",
            "uses": [
                {"text": "Creaminess", "link": None},
                {"text": "Moisture", "link": None},
                {"text": "Flavor", "link": None},
                {"text": "Richness", "link": None},
            ],
            "note": "click on the word for a definition!",
            "image": "/static/images/dairy.jpg",
            "back_link": "/learn/2",
            "next_link": "/learn/16"
        },
        21: {
            "title": "GLUTEN!",
            "uses": [
                {"text": "Structure", "link": None},
                {"text": "Elasticity", "link": "#"},
                {"text": "Chewiness", "link": None},
                {"text": "Binding", "link": None},
            ],
            "note": "click on the word for a definition!",
            "image": "/static/images/flour.jpg",
            "back_link": "/learn/2",
            "next_link": "/learn/22"
        }
    }

    # Check if the lesson exists
    if lesson_num in lessons:
        return render_template(
            'learn_template.html',
            title=lessons[lesson_num]["title"],
            uses=lessons[lesson_num]["uses"],
            note=lessons[lesson_num]["note"],
            image=lessons[lesson_num]["image"],
            back_link=lessons[lesson_num]["back_link"]
        )
    else:
        # Handle invalid lesson numbers
        return "Lesson not found", 404

# Quiz route
@app.route('/quiz/<int:question_num>', methods=['GET', 'POST'])
def quiz(question_num):
    return render_template('quiz.html', question_num=question_num)

if __name__ == '__main__':
    app.run(debug=True)