from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
from datetime import datetime
import data

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

# calculating lesson numbers
START_INDEX = 3
lesson_map = []
category_home = []

for category, contents in data.lessons.items():
    for i in range (1, 5):
        cur_index = len(lesson_map)+START_INDEX
        if i==1:
            category_home.append(cur_index)
            back_index = 2
        else:
            back_index = cur_index-1
        next_index = 2 if i==4 else cur_index+1
        lesson_map.append({
            "category": contents[0],
            "data": contents[i],
            "template": data.template_map[i],
            "back_index": back_index,
            "next_index": next_index
        })

# Home route
@app.route('/')
def home():
    # session.clear()
    return render_template('index.html')

# Learning route
@app.route('/learn/<int:lesson_num>', methods=['GET', 'POST'])
def learn_lesson(lesson_num):
    if lesson_num==1:
        return render_template("learn_1.html")
    elif lesson_num==2:
        return render_template("learn_2.html", homes=category_home)
    else:
        if lesson_num not in range(START_INDEX, START_INDEX+len(lesson_map)):
             return "Lesson not found", 404
        index = lesson_num-START_INDEX
        return render_template(
            lesson_map[index]["template"], 
            general=lesson_map[index]["category"],
            contents=lesson_map[index]["data"],
            back_index=lesson_map[index]["back_index"],
            next_index=lesson_map[index]["next_index"])


# Quiz route
@app.route('/quiz/<int:question_num>', methods=['GET', 'POST'])
def quiz(question_num):
    if question_num == 1:
        return render_template('quiz.html', question_num=question_num)
    elif question_num == 2:
        return render_template('quiz_linear.html', question=data.quiz_questions[0])
    elif question_num == 3:
        return render_template('quiz_linear.html', question=data.quiz_questions[1])
    elif question_num == 4:
        return render_template('quiz_linear.html', question=data.quiz_questions[2])
    elif question_num == 5:
        return render_template('quiz_final.html', question=data.final_question)
    else:
        return "Quiz not found", 404

@app.route('/quiz/results')
def quiz_results():
    return render_template('quiz_results.html')

if __name__ == '__main__':
    app.run(debug=True)