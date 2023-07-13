from bs4 import BeautifulSoup
import requests

def scrape_recipe(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the recipe title
    title = soup.find('h1').text if soup.find('h1') else "Title Not Found"
    
    # Find Ingredient List using text or heading 
    ingredient_heading = soup.find('h2', text ="Ingredients") or soup.find('h2', text ="Ingredient") or soup.find('h3', text ="Ingredients") or soup.find('h3', text ="Ingredient") or soup.find('div', text="Ingredient") or soup.find('div', text="Ingredients") or soup.find('p', text="Ingredient") or soup.find('p', text="Ingredients")
    # Extract the ingredient list
    if ingredient_heading:
        ingredients = []
        ingredient_element = ingredient_heading.find_next_sibling()
        while ingredient_element and ingredient_element.name != "h2" and ingredient_element.name != "h3":
            if ingredient_element.name == "ul" or ingredient_element.name != "ol":
                ingredient = ingredient_element.text.strip().replace(',','')
                ingredients.append(ingredient)
            ingredient_element = ingredient_element.find_next_sibling()

     # Add comma to each ingredient
        ingredients_with_comma = ", ".join(ingredients)
    else:
        ingredients_with_comma = "Ingredients Not Found"

    #Find instructions using instructions text or heading
    instructions_heading = soup.find('h2', text ="Instructions") or soup.find('h2', text ="Instruction") or soup.find('h2', text ="Preparations") or soup.find('h2', text ="Preparation") or soup.find('h3', text ="Preparations") or soup.find('h3', text ="Preparation") or soup.find('div', text ="Preparations") or soup.find('div', text ="Preparation") or soup.find('p', text ="Preparations") or soup.find('p', text ="Preparation") or soup.find('h3', text ="Instructions") or soup.find('h3', text ="Instruction") or soup.find('div', text="Instructions") or soup.find('div', text="Instruction") or soup.find('p', text="Instructions") or soup.find('p', text="Instruction")

    # Extract the recipe instructions
    if instructions_heading:
        instructions = []
        instructions_element = instructions_heading.find_next_sibling()
        while instructions_element and instructions_element.name != "h2" and instructions_element.name != "h3":
            if instructions_element.name == "ul" or instructions_element.name != "ol":
                instruction = instructions_element.text.strip().replace(',','')
                instructions.append(instruction)
            instructions_element = instructions_element.find_next_sibling()

    # Add comma to each ingredient
        instructions_with_comma = ", ".join(instructions)
    else:
        instructions_with_comma = "Instructions Not Found"
    return title, ingredients_with_comma, instructions_with_comma
