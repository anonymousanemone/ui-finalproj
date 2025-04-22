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
            "template": contents[i]
        })

for i, thing in enumerate(lesson_map):
    print(i, thing)
#     for local_step, data in sorted(steps.items()):
#         global_steps.append({
#             "category": category,
#             "local_step": local_step,
#             "data": data
#         })

# # Add global step numbers
# for i, step in enumerate(global_steps):
#     step["global_step"] = i + START_INDEX

# # Build a lookup table
# step_lookup = {step["global_step"]: step for step in global_steps}
# print(step_lookup)


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
@app.route('/learn/<int:lesson_num>', methods=['GET', 'POST'])
def learn_lesson(lesson_num):
    if lesson_num==1:
        return render_template('learn_1.html')
    elif lesson_num==2:
        return render_template('learn_2.html')
    else:
        return 
    
# def generate_lesson_num():
#     from flask import Flask, render_template, abort
#     global_steps = []
#     START_INDEX = 3

#     # Flatten the structure: [(category, local_step, data)]
#     for category, steps in data.lessons.items():
#         for local_step, data in sorted(steps.items()):
#             global_steps.append({
#                 "category": category,
#                 "local_step": local_step,
#                 "data": data
#             })

#     # Add global step numbers
#     for i, step in enumerate(global_steps):
#         step["global_step"] = i + START_INDEX

#     # Build a lookup table
#     step_lookup = {step["global_step"]: step for step in global_steps}


# @app.route('/learn/<int:step>')
# def learn(step):
#     if step not in step_lookup:
#         abort(404)

#     lesson = step_lookup[step]
#     category = lesson["category"]
#     local_step = lesson["local_step"]
#     data = lesson["data"]

#     # Previous/Next global steps
#     prev_step = step - 1 if (step - 1) in step_lookup else None
#     next_step = step + 1 if (step + 1) in step_lookup else None

#     # Determine which template to use based on local step
#     if local_step == 0:
#         template = 'title.html'
#         context = data
#     elif local_step == 1:
#         template = 'uses.html'
#         context = {'uses': data['uses']}
#     elif local_step == 2:
#         template = 'substitutes.html'
#         context = {'substitutes': data['susbtitutes']}
#     elif local_step == 3:
#         template = 'mcq.html'
#         context = {'mcq': data['mc-q']}
#     elif local_step == 4:
#         template = 'dragdrop.html'
#         context = {'dragdrop': data['drag-drop']}
#     else:
#         abort(404)

#     return render_template(template,
#                            step=step,
#                            category=category,
#                            prev_step=prev_step,
#                            next_step=next_step,
#                            **context)

# Quiz route
@app.route('/quiz/<int:question_num>', methods=['GET', 'POST'])
def quiz(question_num):
    return render_template('quiz.html', question_num=question_num)

if __name__ == '__main__':
    app.run(debug=True)