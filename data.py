template_map = {1:"note_page.html", 2:"three-tab.html", 3:"egg-swap.html", 4:"drag-drop.html" }

lessons = {
    "eggs": {
        0: {"title": "EGGS!", "image": "/static/images/eggs_mixing.jpg",},
        1: {"uses": [
            {"text": "Binding", "link": "#"},
            {"text": "Leavening", "link": "#"},
            {"text": "Moisture", "link": None},
            {"text": "Richness", "link": None}]
        },
        2: {"susbtitutes": [
            {"name":"Banana", "best-in": "Brownies, pancakes!", "why": "Adds sweetness + moisture!" },
            {"name":"Flax Seeds", "best-in": "Cookies, muffins!", "why": "Great binder with its gel-like texture!" },
            {"name":"Applesauce", "best-in": "Cakes, muffins!", "why": "Neutral, light texture, and adds moisture!" }]
        },
        3: {"mc-q": {
            "swap": "Egg Swap!", 
            "question": "Quick: You want to make muffins, but the price of a carton of eggs from the store is $9!! What do you do?",
            "answers": ["Pay the $9", "Use Applesauce instead!", "Cry"],
            "correct": "Use Applesauce instead!",
            "explanation": "Easy Swap that saves you money!" }
        },
        4: {"drag-drop": {
            "drags": ["Banana", "Flax Seeds", "Applesauce"],
            "drops": ["Moisture", "Binding", "Leavening"],
            "correct-drops": ["Moisture", "Binding", "Moisture"]}
        }
    },
    "dairy": {
        0: {"title": "DAIRY!", "image": "/static/images/dairy.jpg"},
        1: {"uses": [
                {"text": "Creaminess", "link": None},
                {"text": "Moisture", "link": None},
                {"text": "Flavor", "link": None},
                {"text": "Richness", "link": None} ]
        },
        2: {"susbtitutes": [
            {"name":"Milk -> Non-Dairy Milk", "adds": "Creaminess, moisture", "why": "Plant milks mimic texture and liquid content of dairy" },
            {"name":"Butter -> Coconut Oil, Vegan Butter", "adds": "Richness, fat", "why": "Fats provide tenderness and mouthfeel" },
            {"name":"Buttermilk -> Non-Dairy Milk + Vinegar/Lemon", "adds": "Richness, fat", "why": "Acid reacts with baking soda to create leavening" } ]
        },
        3: {"mc-q": {
            "swap": "Milk Swap!", 
            "question": "Quick: You want to make muffins to bring into class, but you don’t know if there are any allergies! Which Dairy-Free swap is best?",
            "answers": ["Oat Milk", "Soy Milk", "Almond Milk"],
            "correct": "Oat Milk",
            "explanation": "Oat is best! Both Soy and Tree-nuts are very common allergies!" }
        },
        4: {"drag-drop": {
            "drags": ["Non-Dairy Milk", "Coconut Oil", "Vinegar/Lemon"],
            "drops": ["Moisture", "Richness", "Leavening"],
            "correct-drops": ["Moisture", "Richness", "Leavening"]}
        }
    },
    "gluten": {
        0: {"title": "GLUTEN!", "image": "/static/images/flour.jpg"},
        1: {"uses": [
                {"text": "Structure", "link": None},
                {"text": "Elasticity", "link": "#"},
                {"text": "Chewiness", "link": None},
                {"text": "Binding", "link": None} ]
        },
        2: {"susbtitutes": [
            {"name":"Almond Flour", "adds": "Moisture and a slightly nutty flavor", "best-in": "Cookies, muffins, quick breads, tart crusts, and pancakes." },
            {"name":"Oat Flour", "adds": "Mild, slightly sweet flavor and a soft, tender texture", "best-in": "Muffins, soft cookies, and bars." },
            {"name":"Gluten-Free All-Purpose Blend", "adds": "Structure, stability, and a 1:1 swap for regular flour", "best-in": "Breads, muffins, cookies, etc. very versatile!" } ]
        },
        3: {"mc-q": {
            "swap": "Gluten Swap!", 
            "question": "Quick: What is the main benefit of using a gluten-free all-purpose blend?",
            "answers": ["It makes food sweeter!", "It has more gluten!", "It works well as a 1:1 substitute!"],
            "correct": "It works well as a 1:1 substitute!",
            "explanation": "Being a 1:1 swap makes Gluten-Free All-Purpose Flour a super versatile substitute!" }
        },
        4: {"drag-drop": {
            "drags": ["Almond Flour", "Oat Flour", "Gluten-Free All-Purpose Blend"],
            "drops": ["Moisture", "Tenderness", "Structure"],
            "correct-drops": ["Moisture", "Tenderness", "Structure"]}
        }
    }
}

definitions = {
    "binding": {
        "definition": "The process of holding ingredients together to maintain structure and prevent crumbling",
    },
    "leavening": {
        "definition": "The process of incorporating air into a batter or dough to help it rise and become light and fluffy."
    },
    "elasticity": {
        "definition": "missing definition"
    }
}