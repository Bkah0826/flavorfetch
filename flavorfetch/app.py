from flask import Flask, render_template, request
from recipescraper import scrape_recipe

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve the URL entered by the user
        url = request.form['url']
        # Call the recipe scraping function
        title, ingredients, instructions = scrape_recipe(url)
        # Render the result template with the extracted data
        return render_template('result.html', title=title, ingredients=ingredients, instructions=instructions)
    # Render the home template for GET requests
    return render_template('home.html')

if __name__ == '__main__':
    app.run()