from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    recipe_text = db.Column(db.Text, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Recipe {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        recipe_text = request.form['recipe_text']
        country = request.form['country']
        ingredients = request.form['ingredients']

        new_recipe = Recipe(
            name=name,
            recipe_text=recipe_text,
            country=country,
            ingredients=ingredients
        )

        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_recipe.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        search_type = request.form['search_type']

        if search_type == 'name':
            recipes = Recipe.query.filter(Recipe.name.contains(search_term)).all()
        elif search_type == 'country':
            recipes = Recipe.query.filter(Recipe.country.contains(search_term)).all()
        elif search_type == 'ingredient':
            recipes = Recipe.query.filter(Recipe.ingredients.contains(search_term)).all()
        else:
            recipes = []

        return render_template('search_results.html', recipes=recipes, search_term=search_term)

    return render_template('search.html')
@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#cd "C:\Users\User\Downloads\Telegram Desktop\install-mac-osx\install-mac-osx"






