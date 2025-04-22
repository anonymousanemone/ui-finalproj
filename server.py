from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
from datetime import datetime
import data

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

# Global lesson steps (flattened)
lesson_map = []
START_INDEX = 3


for category, contents in data.lessons.items():
    for i in range (1, 5):
        # contents[i].append(contents[0].items())
        # print(contents[0], contents[i])
        lesson_map.append({
            "category": contents[0],
            "data": contents[i],
            "template": data.template_map[i]
        })

for i, thing in enumerate(lesson_map):
    print(i, thing)


# Home route
@app.route('/')
def home():
    # session.clear()
    return render_template('index.html')

@app.route('/mc-choice')
def mcchoice():
    # session.clear()
    return render_template('mc-choice.html')
@app.route('/drag-drop')
def dragdrop():
    # session.clear()
    return render_template('drag-drop.html')
@app.route('/learn/7')
def egg_swap():
    return render_template('egg-swap.html')

# Start learning process
# @app.route('/start')
# def start():
#     session['learning_progress'] = {}
#     session['quiz_answers'] = {}
#     return redirect(url_for('learn', lesson_num=1))

# Learning route
@app.route('/learn/<int:lesson_num>', methods=['GET', 'POST'])
def learn_lesson(lesson_num):
    lessons = {
        3: {
            "title": "EGGS!",
            "uses": [
                {"text": "Binding", "link": "/learn/4"},
                {"text": "Leavening", "link": "/learn/5"},
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
        5: {
            "title": "Leavening",
            "note": "Definition: The process of incorporating air into a batter or dough to help it rise and become light and fluffy.",
            "image": "/static/images/eggs_mixing.jpg",
            "back_link": "/learn/3",
            "next_link": "/learn/6"
        },
        6: {
            "title": "Egg Substitutes Overview",
            "substitutes": [
                {
                    "name": "Banana",
                    "works_best": "Brownies, pancakes!",
                    "why_it_works": "Adds sweetness + moisture",
                    "color": "#f4d03f" 
                },
                {
                    "name": "Flax Seeds",
                    "works_best": "Cookies, muffins!",
                    "why_it_works": "Great binder with its gel-like texture!",
                    "color": "#5dade2"  
                },
                {
                    "name": "Applesauce",
                    "works_best": "Cakes, muffins!",
                    "why_it_works": "Neutral, light texture, and adds moisture!",
                    "color": "#a569bd"  
                }
            ],
            "back_link": "/learn/5",
            "next_link": "/learn/7"
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
        16: {
            "title": "Dairy Substitutes Overview",
            "substitutes": [
                {
                    "name": "Milk -> Non-Dairy Milk",
                    "adds": "Creaminess, Moisture!",
                    "why_it_works": "Plant milks mimic texture and liquid content of dairy",
                    "color": "#f4d03f" 
                },
                {
                    "name": "Flax Seeds",
                    "adds": "Richness, fat",
                    "why_it_works": "Fats provide tenderness and mouthfeel",
                    "color": "#5dade2"  
                },
                {
                    "name": "Applesauce",
                    "adds": "Acidity, rise!",
                    "why_it_works": "Acid reacts with baking soda to create leavening",
                    "color": "#a569bd"  
                }
            ],
            "back_link": "/learn/15",
            "next_link": "/learn/17"
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
        lesson = lessons[lesson_num]

        # Render `substitutes.html` if the lesson has substitutes
        if "substitutes" in lesson:
            return render_template(
                'substitutes.html',
                title=lesson["title"],
                substitutes=lesson["substitutes"],
                back_link=lesson.get("back_link"),
                next_link=lesson.get("next_link")
            )

        # Render `learn_template.html` for other lessons
        return render_template(
            'learn_template.html',
            title=lesson["title"],
            uses=lesson.get("uses", []),  # Default to an empty list if `uses` is not present
            note=lesson.get("note", ""),
            image=lesson.get("image", ""),
            back_link=lesson.get("back_link"),
            next_link=lesson.get("next_link")
        )

    # Handle invalid lesson numbers
    return "Lesson not found", 404

# Quiz route
@app.route('/quiz/<int:question_num>', methods=['GET', 'POST'])
def quiz(question_num):
    return render_template('quiz.html', question_num=question_num)

if __name__ == '__main__':
    app.run(debug=True)