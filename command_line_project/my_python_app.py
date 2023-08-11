import random

def my_cool_func():
    return "Hope you enjoy your culinary adventure!"

# Lists of options for cooking and baking categories
cooking_categories = ["British", "French", "Chinese", "Italian", "Japanese", "Thai", "Spanish", "Greek", "Lebanese", "Indian", "Mexican"]
baking_categories = ["bread", "cake", "cookies", "tart", "pastry", "brownies"]

# Dictionary of cooking recipes
cooking_recipes = {
    "British": [
        {
            "name": "Fish and Chips",
            "ingredients": ["white fish fillets", "potatoes", "flour", "beer", "salt", "vegetable oil"],
            "total_time": "45 minutes",
            "instructions": [
                "Peel and cut potatoes into fries for 10 minutes.",
                "Mix flour, beer, and salt to make batter for 5 minutes.",
                "Dip fish in batter and fry until golden for 10 minutes.",
                "Fry the potatoes until crispy for 10 minutes.",
                "Serve with malt vinegar."
            ],
        },
    ],
    "French": [
        {
            "name": "Coq au Vin",
            "ingredients": ["chicken", "red wine", "bacon", "onions",  "mushrooms", "carrots", "thyme", "flour"],
            "total_time": "2 hours",
            "instructions": [
                ("Sear chicken in a pot for 15 minutes."),
                ("Saute bacon, onions, and mushrooms for 15 minutes."),
                ("Add wine, carrots, thyme, and flour for 10 minutes."),
                ("Simmer until chicken is tender for 1.5 hours."),
                ("Serve with crusty bread.")
            ],
        },
    ],
   "Chinese": [
        {
            "name": "Kung Pao Chicken",
            "ingredients": [
                "boneless chicken breast, cut into bite-sized pieces",
                "roasted peanuts",
                "dried red chili peppers",
                "green onions, chopped",
                "ginger, minced",
                "garlic, minced",
                "soy sauce",
                "hoisin sauce",
                "rice vinegar",
                "cornstarch",
                "vegetable oil",
                "sesame oil",
                "salt and pepper"
            ],
            "total_time": "30 minutes",
            "instructions": [
                "In a bowl, mix soy sauce, hoisin sauce, rice vinegar, sesame oil, and cornstarch to make the sauce.",
                "Heat vegetable oil in a wok or pan over medium-high heat.",
                "Add dried red chili peppers and stir-fry for a few seconds.",
                "Add chicken pieces and stir-fry until cooked and slightly browned.",
                "Add ginger and garlic, and stir-fry for another minute.",
                "Pour in the sauce and stir to coat the chicken.",
                "Add roasted peanuts and green onions, and stir-fry for a couple of minutes.",
                "Season with salt and pepper to taste.",
                "Serve hot over steamed rice."
            ],
        },
    ],
    "Italian": [
        {
            "name": "Spaghetti Carbonara",
            "ingredients": [
                "spaghetti",
                "pancetta or guanciale",
                "eggs",
                "pecorino cheese, grated",
                "black pepper",
                "salt",
                "olive oil"
            ],
            "total_time": "20 minutes",
            "instructions": [
                "Cook spaghetti in boiling salted water until al dente.",
                "While pasta cooks, sauté pancetta or guanciale in olive oil until crispy.",
                "In a bowl, whisk eggs, grated pecorino cheese, and black pepper.",
                "When pasta is ready, quickly mix it with the cooked pancetta/guanciale.",
                "Off heat, add the egg mixture to the pasta and toss until creamy.",
                "Season with salt and additional cheese and pepper to taste.",
                "Serve immediately."
            ],
        },
    ],
    "Japanese": [
        {
            "name": "Chicken Teriyaki",
            "ingredients": [
                "boneless chicken thighs",
                "soy sauce",
                "mirin",
                "sugar",
                "vegetable oil",
                "sesame seeds (optional)",
                "green onions, sliced (optional)"
            ],
            "total_time": "30 minutes",
            "instructions": [
                "In a bowl, mix soy sauce, mirin, and sugar to make the teriyaki sauce.",
                "Heat vegetable oil in a skillet over medium-high heat.",
                "Add chicken thighs and cook until browned on both sides.",
                "Pour teriyaki sauce over the chicken and simmer until sauce thickens.",
                "Sprinkle with sesame seeds and green onions if desired.",
                "Serve over steamed rice."
            ],
        },
    ],
    "Thai": [
        {
            "name": "Pad Thai",
            "ingredients": [
                "rice noodles",
                "shrimp (or tofu)",
                "eggs",
                "bean sprouts",
                "green onions, chopped",
                "peanuts, crushed",
                "lime wedges",
                "vegetable oil",
                "fish sauce",
                "tamarind paste",
                "sugar",
                "chili powder",
                "garlic, minced"
            ],
            "total_time": "30 minutes",
            "instructions": [
                "Soak rice noodles in warm water until softened. Drain and set aside.",
                "In a pan, heat vegetable oil and sauté garlic until fragrant.",
                "Add shrimp (or tofu) and cook until pink and cooked through.",
                "Push the shrimp to one side of the pan and crack eggs into the other side. Scramble until cooked.",
                "Add rice noodles and stir-fry to combine.",
                "In a bowl, mix fish sauce, tamarind paste, sugar, and chili powder to make the sauce.",
                "Pour the sauce over the noodles and stir-fry to coat.",
                "Add bean sprouts and green onions, and toss.",
                "Serve hot, garnished with crushed peanuts and lime wedges."
            ],
        },
    ],
    "Spanish": [
        {
            "name": "Paella",
            "ingredients": [
                "chicken pieces",
                "chorizo sausage, sliced",
                "shrimp",
                "mussels",
                "onion, chopped",
                "red bell pepper, diced",
                "green peas",
                "rice",
                "saffron threads",
                "chicken broth",
                "olive oil",
                "garlic, minced",
                "paprika",
                "salt and pepper"
            ],
            "total_time": "1 hour",
            "instructions": [
                "In a paella pan, heat olive oil over medium heat.",
                "Add chicken pieces and chorizo. Cook until browned.",
                "Push the chicken and chorizo to the sides and sauté onion, bell pepper, and garlic.",
                "Add rice and paprika. Stir to coat the rice with the oil and spices.",
                "Stir in saffron threads and chicken broth. Bring to a simmer.",
                "Arrange shrimp, mussels, and peas over the rice.",
                "Cover and cook until the rice is tender and the seafood is cooked.",
                "Season with salt and pepper to taste.",
                "Serve hot with lemon wedges."
            ],
        },
    ],
    "Greek": [
        {
            "name": "Greek Salad",
            "ingredients": [
                "tomatoes, chopped",
                "cucumber, chopped",
                "red onion, thinly sliced",
                "Kalamata olives",
                "feta cheese, crumbled",
                "extra-virgin olive oil",
                "dried oregano",
                "salt and pepper",
                "fresh lemon juice"
            ],
            "total_time": "15 minutes",
            "instructions": [
                "In a large bowl, combine tomatoes, cucumber, and red onion.",
                "Add Kalamata olives and crumbled feta cheese.",
                "Drizzle extra-virgin olive oil over the salad.",
                "Sprinkle with dried oregano, salt, and pepper to taste.",
                "Squeeze fresh lemon juice over the salad.",
                "Toss gently to combine all the ingredients.",
                "Serve immediately as a refreshing salad."
            ],
        },
    ],
    "Lebanese": [
        {
            "name": "Hummus",
            "ingredients": [
                "chickpeas",
                "tahini",
                "garlic, minced",
                "lemon juice",
                "extra-virgin olive oil",
                "ground cumin",
                "salt",
                "paprika",
                "fresh parsley, chopped (for garnish)",
                "pita bread (for serving)"
            ],
            "total_time": "15 minutes",
            "instructions": [
                "In a food processor, blend chickpeas, tahini, garlic, lemon juice, olive oil, cumin, and salt until smooth.",
                "If the mixture is too thick, add a little water or more lemon juice.",
                "Taste and adjust seasoning if needed.",
                "Transfer to a serving bowl and drizzle with extra olive oil.",
                "Sprinkle paprika and chopped parsley on top for garnish.",
                "Serve with warm pita bread."
            ],
        },
    ],
    "Indian": [
        {
            "name": "Chicken Curry",
            "ingredients": [
                "chicken pieces",
                "onion, chopped",
                "tomatoes, chopped",
                "ginger-garlic paste",
                "yogurt",
                "ground turmeric",
                "ground cumin",
                "ground coriander",
                "garam masala",
                "chili powder",
                "vegetable oil",
                "fresh cilantro, chopped (for garnish)",
                "salt"
            ],
            "total_time": "45 minutes",
            "instructions": [
                "Heat vegetable oil in a pan and sauté chopped onion until golden.",
                "Add ginger-garlic paste and sauté for another minute.",
                "Stir in ground turmeric, ground cumin, ground coriander, chili powder, and garam masala.",
                "Add chicken pieces and cook until browned.",
                "Stir in chopped tomatoes and cook until they soften.",
                "Add yogurt and simmer until the chicken is cooked through.",
                "Season with salt and adjust spices to taste.",
                "Garnish with chopped fresh cilantro.",
                "Serve hot with rice or naan bread."
            ],
        },
    ],
    "Mexican": [
        {
            "name": "Chicken Tacos",
            "ingredients": [
                "boneless chicken thighs",
                "taco seasoning",
                "flour or corn tortillas",
                "shredded lettuce",
                "diced tomatoes",
                "shredded cheddar cheese",
                "sour cream",
                "salsa",
                "fresh cilantro, chopped (for garnish)",
                "lime wedges"
            ],
            "total_time": "25 minutes",
            "instructions": [
                "Season chicken thighs with taco seasoning.",
                "Heat a skillet over medium heat and cook chicken until fully cooked and slightly charred.",
                "Warm tortillas in a dry skillet or microwave.",
                "Assemble tacos: Place shredded lettuce on each tortilla, top with diced tomatoes and cooked chicken.",
                "Sprinkle shredded cheese over the filling.",
                "Add a dollop of sour cream and salsa on top.",
                "Garnish with chopped fresh cilantro and serve with lime wedges.",
                "Enjoy your flavorful chicken tacos!"
            ],
        },
    ],
}

# Dictionary of baking recipes
baking_recipes = {
    "Bread": [
        {
            "name": "Classic Homemade Bread",
            "ingredients": [
                "4 cups all-purpose flour",
                "1 packet active dry yeast",
                "1 1/2 cups warm water",
                "2 tablespoons sugar",
                "2 teaspoons salt",
                "2 tablespoons olive oil",
            ],
            "total_time": "3 hours",
            "instructions": [
                "In a bowl, dissolve sugar in warm water. Sprinkle yeast over the water and let it stand for about 10 minutes until foamy.",
                "Add flour, salt, and olive oil to the yeast mixture. Mix to form a dough.",
                "Knead the dough on a floured surface for about 10 minutes until smooth and elastic.",
                "Place the dough in a greased bowl, cover with a damp cloth, and let it rise in a warm place for about 1.5 to 2 hours, or until doubled in size.",
                "Punch down the dough and shape it into a loaf. Place in a greased loaf pan.",
                "Cover and let it rise for another 30 minutes.",
                "Preheat the oven to 375°F (190°C).",
                "Bake the bread for about 25-30 minutes, or until the top is golden brown and sounds hollow when tapped.",
                "Remove from the oven and let it cool on a wire rack before slicing.",
            ],
        },
    ],
    "Cake": [
        {
            "name": "Classic Chocolate Cake",
            "ingredients": [
                "2 cups all-purpose flour",
                "1 3/4 cups granulated sugar",
                "3/4 cup unsweetened cocoa powder",
                "1 1/2 teaspoons baking powder",
                "1 1/2 teaspoons baking soda",
                "1 teaspoon salt",
                "2 large eggs",
                "1 cup milk",
                "1/2 cup vegetable oil",
                "2 teaspoons vanilla extract",
                "1 cup boiling water",
            ],
            "total_time": "1 hour",
            "instructions": [
                "Preheat the oven to 175°C. Grease and flour two 9-inch round cake pans.",
                "In a large bowl, whisk together flour, sugar, cocoa powder, baking powder, baking soda, and salt.",
                "Add eggs, milk, oil, and vanilla extract. Beat on medium speed for 2 minutes.",
                "Stir in boiling water until the batter is smooth. The batter will be thin.",
                "Pour the batter evenly into the prepared pans.",
                "Bake for 30 to 35 minutes, or until a toothpick inserted into the center comes out clean.",
                "Remove from the oven and let the cakes cool in the pans for 10 minutes. Then, transfer to wire racks to cool completely.",
                "Once cooled, frost and decorate the cake as desired.",
                "Slice and serve the delicious chocolate cake!",
            ],
        },
    ],
    "Cookies": [
        {
            "name": "Chocolate Chip Cookies",
            "ingredients": [
                "1 cup butter, softened",
                "3/4 cup granulated sugar",
                "3/4 cup brown sugar, packed",
                "1 teaspoon vanilla extract",
                "2 large eggs",
                "2 1/4 cups all-purpose flour",
                "1 teaspoon baking soda",
                "1/2 teaspoon salt",
                "2 cups chocolate chips",
            ],
            "total_time": "25 minutes",
            "instructions": [
                "Preheat the oven to 190°C.",
                "In a large bowl, beat together softened butter, granulated sugar, brown sugar, and vanilla extract until creamy.",
                "Add eggs, one at a time, beating well after each addition.",
                "In a separate bowl, combine flour, baking soda, and salt. Gradually add to the butter mixture, beating until well blended.",
                "Stir in chocolate chips.",
                "Drop rounded tablespoons of dough onto ungreased baking sheets.",
                "Bake for 9 to 11 minutes, or until golden brown.",
                "Remove from the oven and let the cookies cool on the baking sheets for a few minutes, then transfer to wire racks to cool completely.",
                "Enjoy your homemade chocolate chip cookies!",
            ],
        },
    ],
    "Tart": [
        {
            "name": "Raspberry Almond Tart",
            "ingredients": [
                "1 sheet frozen puff pastry, thawed",
                "1 cup almond flour",
                "1/2 cup granulated sugar",
                "1/4 teaspoon salt",
                "2 large eggs",
                "1/4 cup unsalted butter, melted",
                "1 teaspoon almond extract",
                "1 cup fresh raspberries",
                "Powdered sugar, for dusting",
            ],
            "total_time": "1 hour",
            "instructions": [
                "Preheat the oven to 190°C.",
                "Roll out the thawed puff pastry and fit it into a tart pan. Trim any excess pastry.",
                "In a bowl, whisk together almond flour, granulated sugar, and salt.",
                "Add eggs, melted butter, and almond extract. Mix until well combined.",
                "Spread the almond mixture evenly over the puff pastry.",
                "Arrange fresh raspberries on top of the almond mixture.",
                "Bake for 25 to 30 minutes, or until the tart is golden brown and the filling is set.",
                "Remove from the oven and let the tart cool on a wire rack.",
                "Once cooled, dust with powdered sugar before serving.",
                "Slice and enjoy your delightful raspberry almond tart!",
            ],
        },
    ],
    "Pastry": [
        {
            "name": "Spinach and Feta Pastry",
            "ingredients": [
                "1 sheet frozen puff pastry, thawed",
                "2 cups fresh spinach, chopped",
                "1/2 cup feta cheese, crumbled",
                "1/4 cup grated Parmesan cheese",
                "1/4 cup chopped fresh dill",
                "1/4 teaspoon salt",
                "1/4 teaspoon black pepper",
                "1 large egg, beaten (for egg wash)",
            ],
            "total_time": "40 minutes",
            "instructions": [
                "Preheat the oven to 200°C.",
                "In a bowl, combine chopped spinach, feta cheese, Parmesan cheese, chopped dill, salt, and black pepper.",
                "Roll out the thawed puff pastry and cut into squares or rectangles.",
                "Place a spoonful of the spinach and cheese mixture onto each pastry square.",
                "Fold the pastry over the filling to create a triangle or rectangle shape. Press the edges to seal.",
                "Brush the tops of the pastries with beaten egg for a golden finish.",
                "Place the pastries on a baking sheet and bake for 20 to 25 minutes, or until they are puffed and golden brown.",
                "Remove from the oven and let the pastries cool on a wire rack.",
                "Serve the delicious spinach and feta pastries as an appetizer or snack.",
            ],
        },
    ],
    "Brownies": [
        {
            "name": "Fudgy Chocolate Brownies",
            "ingredients": [
                "1/2 cup unsalted butter",
                "1 cup granulated sugar",
                "2 large eggs",
                "1 teaspoon vanilla extract",
                "1/3 cup unsweetened cocoa powder",
                "1/2 cup all-purpose flour",
                "1/4 teaspoon salt",
                "1/4 teaspoon baking powder",
                "1/2 cup chocolate chips or chunks",
            ],
            "total_time": "30 minutes",
            "instructions": [
                "Preheat the oven to 175°C. Grease and line an 8x8-inch baking pan with parchment paper.",
                "In a microwave-safe bowl, melt the butter in 20-second intervals until fully melted.",
                "Stir in granulated sugar until well combined.",
                "Add eggs one at a time, mixing well after each addition. Stir in vanilla extract.",
                "In a separate bowl, whisk together cocoa powder, flour, salt, and baking powder.",
                "Gradually add the dry ingredients to the wet ingredients, mixing until just combined.",
                "Fold in chocolate chips or chunks.",
                "Pour the batter into the prepared baking pan and spread evenly.",
                "Bake for 20 to 25 minutes, or until a toothpick inserted into the centre comes out with a few moist crumbs.",
                "Remove from the oven and let the brownies cool in the pan.",
                "Once cooled, lift the brownies out of the pan using the parchment paper, then slice and enjoy!",
            ],
        },
    ],
}

# Combine both cooking and baking recipes into a single dictionary
recipes = {
    "Cooking": cooking_recipes,
    "Baking": baking_recipes,
}

# Function to fetch and display the recipe from a category
def get_recipe(category, category_type):
    if category_type in recipes:
        for available_category in recipes[category_type]:
            if available_category.lower() == category.lower():
                recipe = recipes[category_type][available_category][0]
                print(f"Recipe: {recipe['name']}")
                print("Ingredients:", ', '.join(recipe['ingredients']))
                print("Total Time:", recipe['total_time'])
                print("Instructions:")
                for step, instruction in enumerate(recipe['instructions'], start=1):
                    print(f"{step}. {instruction}")
                return
        print("Category not found.")
    else:
        print("Invalid category type.")

# Function to recommend a recipe based on user's choice
def recommend_recipe():
    print("Welcome to the Recipe Recommender!")
    mood = input("Are you in the mood to cook or bake today? ")

    if mood.lower() == "cook":
        print("Great! What type of cuisine are you interested in?")
        print("Options: British, French, Chinese, Italian, Japanese, Thai, Spanish, Greek, Lebanese, Indian, or Random")
        category = input("Enter your choice: ")
        if category.lower() == "random":
            random_category = random.choice(list(recipes["Cooking"].keys()))
            get_recipe(random_category, "Cooking")
        else:
            get_recipe(category, "Cooking")

    elif mood.lower() == "bake":
        print("Great! What type of baking are you interested in?")
        print("Options: Bread, Cake, Cookies, Tart, Pastry, Brownies, or Random")
        category = input("Enter your choice: ")
        if category.lower() == "random":
            random_category = random.choice(list(recipes["Baking"].keys()))
            get_recipe(random_category, "Baking")
        else:
            get_recipe(category, "Baking")

    else:
        print("Invalid input. Please choose 'cook' or 'bake'.")

    print(my_cool_func())

# Main loop
while True:
    recommend_recipe()
    play_again = input("Do you want to find another recipe? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thank you for using the Recipe Recommendation App!")
