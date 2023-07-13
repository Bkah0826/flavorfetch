from recipescraper import scrape_recipe

url1 = 'https://www.madewithlau.com/recipes/scallops-and-asparagus'
url2 = 'https://www.allrecipes.com/how-to-make-chili-oil-recipe-7507407'
url3 = 'https://tasty.co/recipe/creamy-mushroom-toasts'
url4 = 'https://www.epicurious.com/recipes/food/views/ba-syn-sujebi-kimchi-soup'


# title, ingredients, instructions = scrape_recipe(url1)
# print("Title:", title)
# print("Ingredients:", ingredients)
# print("Instructions:", instructions)
# print("Recipe Taken From: ", url1)

# title, ingredients, instructions = scrape_recipe(url2)
# print("Title:", title)
# print("Ingredients:", ingredients)
# print("Instructions:", instructions)
# print("Recipe Taken From: ", url2)

title, ingredients, instructions = scrape_recipe(url3)
print("Title:", title)
print("Ingredients:", ingredients)
print("Instructions:", instructions)
print("Recipe Taken From: ", url3)

# title, ingredients, instructions = scrape_recipe(url4)
# print("Title:", title)
# print("Ingredients:", ingredients)
# print("Instructions:", instructions)
# print("Recipe Taken From: ", url4)