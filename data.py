template_map = {1:"uses.html", 2:"substitutes.html", 3:"swap_mc.html", 4:"drag_drop.html" }

lessons = {
    "eggs": {
        0: {"title": "EGGS", "image": "/static/images/eggs_mixing.jpg",},
        1: {"uses": [
            {"text": "Binding", "link": "#"},
            {"text": "Leavening", "link": "#"},
            {"text": "Moisture", "link": None},
            {"text": "Richness", "link": None}]
        },
        2: {"substitutes": [
            {"name":"Banana", "best_in": "Brownies, pancakes!", "why": "Adds sweetness + moisture!", "color": "#f4d03f" },
            {"name":"Flax Seeds", "best_in": "Cookies, muffins!", "why": "Great binder with its gel-like texture!", "color": "#5dade2" },
            {"name":"Applesauce", "best_in": "Cakes, muffins!", "why": "Neutral, light texture, and adds moisture!", "color": "#a569bd" }]
        },
        3: {"mc_q": {
            "swap": "Egg Swap!", 
            "question": "Quick: You want to make muffins, but the price of a carton of eggs from the store is $9!! What do you do?",
            "answers": ["Pay the $9", "Use Applesauce instead!", "Cry"],
            "correct": "Use Applesauce instead!",
            "explanation": "Easy Swap that saves you money!" }
        },
        4: {"drag_drop": {
            "drags": ["Banana", "Flax Seeds", "Applesauce"],
            "drops": ["Moisture", "Binding", "Leavening"],
            "correct_drops": ["Moisture", "Binding", "Moisture"]}
        }
    },
    "dairy": {
        0: {"title": "DAIRY", "image": "/static/images/dairy.jpg"},
        1: {"uses": [
                {"text": "Creaminess", "link": None},
                {"text": "Moisture", "link": None},
                {"text": "Flavor", "link": None},
                {"text": "Richness", "link": None} ]
        },
        2: {"substitutes": [
            {"name":"Milk -> Non-Dairy Milk", "adds": "Creaminess, moisture", "why": "Plant milks mimic texture and liquid content of dairy" , "color": "#f4d03f"},
            {"name":"Butter -> Coconut Oil, Vegan Butter", "adds": "Richness, fat", "why": "Fats provide tenderness and mouthfeel" , "color": "#5dade2"},
            {"name":"Buttermilk -> Non-Dairy Milk + Vinegar/Lemon", "adds": "Richness, fat", "why": "Acid reacts with baking soda to create leavening" , "color": "#a569bd"} ]
        },
        3: {"mc_q": {
            "swap": "Milk Swap!", 
            "question": "Quick: You want to make muffins to bring into class, but you don’t know if there are any allergies! Which Dairy-Free swap is best?",
            "answers": ["Oat Milk", "Soy Milk", "Almond Milk"],
            "correct": "Oat Milk",
            "explanation": "Oat is best! Both Soy and Tree-nuts are very common allergies!" }
        },
        4: {"drag_drop": {
            "drags": ["Non-Dairy Milk", "Coconut Oil", "Vinegar/Lemon"],
            "drops": ["Moisture", "Richness", "Leavening"],
            "correct_drops": ["Moisture", "Richness", "Leavening"]}
        }
    },
    "gluten": {
        0: {"title": "GLUTEN", "image": "/static/images/flour.jpg"},
        1: {"uses": [
                {"text": "Structure", "link": None},
                {"text": "Elasticity", "link": "#"},
                {"text": "Chewiness", "link": None},
                {"text": "Binding", "link": None} ]
        },
        2: {"substitutes": [
            {"name":"Almond Flour", "adds": "Moisture and a slightly nutty flavor", "best_in": "Cookies, muffins, quick breads, tart crusts, and pancakes." , "color": "#f4d03f"},
            {"name":"Oat Flour", "adds": "Mild, slightly sweet flavor and a soft, tender texture", "best_in": "Muffins, soft cookies, and bars." , "color": "#5dade2"},
            {"name":"Gluten-Free All-Purpose Blend", "adds": "Structure, stability, and a 1:1 swap for regular flour", "best_in": "Breads, muffins, cookies, etc. very versatile!" , "color": "#a569bd"} ]
        },
        3: {"mc_q": {
            "swap": "Gluten Swap!", 
            "question": "Quick: What is the main benefit of using a gluten-free all-purpose blend?",
            "answers": ["It makes food sweeter!", "It has more gluten!", "It works well as a 1:1 substitute!"],
            "correct": "It works well as a 1:1 substitute!",
            "explanation": "Being a 1:1 swap makes Gluten-Free All-Purpose Flour a super versatile substitute!" }
        },
        4: {"drag_drop": {
            "drags": ["Almond Flour", "Oat Flour", "Gluten-Free All-Purpose Blend"],
            "drops": ["Moisture", "Tenderness", "Structure"],
            "correct_drops": ["Moisture", "Tenderness", "Structure"]}
        }
    }
}

definitions = {
    "Binding": {
        "definition": "The process of holding ingredients together to maintain structure and prevent crumbling",
    },
    "Leavening": {
        "definition": "The process of incorporating air into a batter or dough to help it rise and become light and fluffy."
    },
    "Elasticity": {
        "definition": "missing definition"
    }
}

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