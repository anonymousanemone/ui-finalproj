template_map = {1:"uses.html", 2:"substitutes.html", 3:"swap_mc.html", 4:"drag_drop.html" }

lessons = {
    "eggs": {
        0: {"title": "EGGS", 
            "image": "/static/images/eggs_mixing.jpg",
            "icon": "/static/images/egg.png"},
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
        0: {"title": "DAIRY", 
            "image": "/static/images/dairy.jpg",
            "icon": "/static/images/milk.png"},
        1: {"uses": [
                {"text": "Creaminess", "link": None},
                {"text": "Moisture", "link": None},
                {"text": "Flavor", "link": None},
                {"text": "Richness", "link": None} ]
        },
        2: {"substitutes": [
            {"name":"Milk -> Non-Dairy Milk", "adds": "Creaminess, moisture", "why": "Plant milks mimic texture and liquid content of dairy" , "color": "#f4d03f"},
            {"name":"Butter -> Coconut Oil, Vegan Butter", "adds": "Richness, fat", "why": "Fats provide tenderness and mouthfeel" , "color": "#5dade2"},
            {"name":"Buttermilk -> Non-Dairy Milk + Vinegar or Lemon", "adds": "Richness, fat", "why": "Acid reacts with baking soda to create leavening" , "color": "#a569bd"} ]
        },
        3: {"mc_q": {
            "swap": "Milk Swap!", 
            "question": "Quick: You want to make muffins to bring into class, but you don't know if there are any allergies! Which Dairy-Free swap is best?",
            "answers": ["Oat Milk", "Soy Milk", "Almond Milk"],
            "correct": "Oat Milk",
            "explanation": "Oat is best! Both Soy and Tree-nuts are very common allergies!" }
        },
        4: {"drag_drop": {
            "drags": ["Non-Dairy Milk", "Coconut Oil", "Vinegar or Lemon"],
            "drops": ["Moisture", "Richness", "Leavening"],
            "correct_drops": ["Moisture", "Richness", "Leavening"]}
        }
    },
    "gluten": {
        0: {"title": "GLUTEN",
            "image": "/static/images/flour.jpg",
            "icon": "/static/images/gluten.png"},
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

quiz_questions = [
    {
        "category": "Eggs",
        "question": "What can you use as an egg substitute in baking?",
        "options": ["Banana", "Apple Sauce", "Both A and B", "None of the above"],
        "correct": 2,
        "next": 3,
        "correct_explanation": "Great job! Both bananas and applesauce can be used as egg substitutes. Bananas add moisture and binding, while applesauce provides moisture and helps with leavening.",
        "incorrect_explanation": "Not quite! Both bananas and applesauce can be used as egg substitutes. Bananas add moisture and binding, while applesauce provides moisture and helps with leavening."
    },
    {
        "category": "Dairy",
        "question": "What can you use instead of milk in recipes?",
        "options": ["Almond milk", "Soy milk", "Oat milk", "All of the above"],
        "correct": 3,
        "next": 4,
        "correct_explanation": "Perfect! All of these plant-based milks can be used as dairy substitutes. They each bring their own unique flavors and properties to your baking.",
        "incorrect_explanation": "Actually, all of these plant-based milks can be used as dairy substitutes. Almond milk adds a nutty flavor, soy milk is protein-rich, and oat milk provides a creamy texture."
    },
    {
        "category": "Gluten",
        "question": "What flour can you use instead of wheat flour?",
        "options": ["Almond flour", "Coconut flour", "Rice flour", "All of the above"],
        "correct": 3,
        "next": 5,
        "correct_explanation": "Excellent! All of these flours can be used as gluten-free alternatives. Each has its own unique properties: almond flour adds moisture and protein, coconut flour is high in fiber, and rice flour provides a neutral taste.",
        "incorrect_explanation": "Actually, all of these flours can be used as gluten-free alternatives. Almond flour adds moisture and protein, coconut flour is high in fiber, and rice flour provides a neutral taste."
    },
    {
        "category": "Eggs",
        "question": "Which egg substitute is especially good for cookies and muffins due to its binding power?",
        "options": ["Flax Seeds", "Banana", "Applesauce", "Oat Flour"],
        "correct": 0,
        "next": 6,
        "correct_explanation": "Exactly! Flax seeds form a gel-like texture when mixed with water, making them a great binder.",
        "incorrect_explanation": "Not quite. Flax seeds are especially great at binding in cookies and muffins due to their gel-like texture."
    },
    {
        "category": "Dairy",
        "question": "Why is vinegar or lemon used with non-dairy milk as a buttermilk substitute?",
        "options": ["Adds sweetness", "Reacts with baking soda for leavening", "Thickens the milk", "Makes it creamier"],
        "correct": 1,
        "next": 7,
        "correct_explanation": "Right! The acid from vinegar or lemon reacts with baking soda to create leavening.",
        "incorrect_explanation": "Actually, the acid reacts with baking soda to help baked goods rise – a key trait of buttermilk!"
    },
    {
        "category": "Gluten",
        "question": "What makes Gluten-Free All-Purpose Flour a versatile substitute?",
        "options": ["It's sweeter than other flours", "It has a nutty flavor", "It works as a 1:1 swap", "It’s best for pancakes only"],
        "correct": 2,
        "next": 8,
        "correct_explanation": "Exactly! It’s designed to be a 1:1 substitute for regular flour, making it super flexible.",
        "incorrect_explanation": "Close, but it’s the 1:1 swap ratio that makes it such a versatile gluten-free option."
    },
    {
    "category": "Eggs",
    "question": "Which of the following is NOT a primary use of eggs in baking?",
    "options": ["Binding", "Leavening", "Coloring", "Moisture"],
    "correct": 2,
    "next": 9,
    "correct_explanation": "Correct! 'Coloring' is not one of the four primary uses of eggs listed—those are Binding, Leavening, Moisture, and Richness.",
    "incorrect_explanation": "Not quite. While eggs can influence color, the main uses in baking are Binding, Leavening, Moisture, and Richness."
    },
    {
    "category": "Dairy",
    "question": "Why is coconut oil a good substitute for butter in dairy-free baking?",
    "options": [
        "It has a similar salt content",
        "It helps with leavening",
        "It adds richness and fat",
        "It’s a type of protein"
    ],
    "correct": 2,
    "next": 10,
    "correct_explanation": "Yes! Coconut oil adds richness and fat, which are the main properties butter contributes to baking.",
    "incorrect_explanation": "Not quite. Coconut oil is used as a butter substitute because it adds richness and fat, just like butter."
    },
    {
    "category": "Gluten",
    "question": "What property does oat flour bring to gluten-free baking?",
    "options": [
        "A crunchy texture and nutty flavor",
        "A mild, slightly sweet flavor and soft texture",
        "A strong binding structure",
        "A bitter aftertaste and dryness"
    ],
    "correct": 1,
    "next": 11,
    "correct_explanation": "Exactly! Oat flour adds a mild, sweet flavor and creates a soft, tender texture—great for cookies and muffins.",
    "incorrect_explanation": "Not quite. Oat flour adds a soft, tender texture and a mild, slightly sweet flavor—ideal for gentle bakes."
    }
]

final_question = {
    "title": "Let's Make Cookies!",
    "instruction": "Select the correct items from the cupboard to make the substitutes that allow all guests to enjoy together!",
    "ingredients": [
        {"name": "GF AP Flour", "image": "flour.webp", "correct": True},
        {"name": "Almond Flour", "image": "almond.webp", "correct": False},
        {"name": "Bananas", "image": "banana.webp", "correct": True},
        {"name": "Milk", "image": "milk.png", "correct": False},
        {"name": "Flax Seeds", "image": "seeds.webp", "correct": True},
        {"name": "Oat Milk", "image": "milk.png", "correct": True},
        {"name": "Flour", "image": "gluten.png", "correct": False},
        {"name": "Vegan Butter", "image": "butter.png", "correct": True},
        {"name": "Eggs", "image": "egg.png", "correct": False}
    ],
    "correct_explanation": "Perfect! Using GF AP Flour (gluten-free), Bananas (egg substitute), Flax Seeds (binding), Oat Milk (dairy-free), and Vegan Butter makes cookies everyone can enjoy!",
    "incorrect_explanation": "Not quite! Remember, we need to make cookies that are gluten-free, dairy-free, and egg-free. Try selecting GF AP Flour, Bananas, Flax Seeds, Oat Milk, and Vegan Butter.",
    "background_image": "/static/images/kitchen.gif"
}