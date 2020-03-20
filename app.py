import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
# Ensures that the debug is set to false when deployed but true when open on gitpod
should_debug = False

if path.exists("env.py"):
    import env
    should_debug = True

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'lights-out'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Links the category id field from the categories collection with the category field from the stories collection
@app.route('/get_stories') 
def get_stories():
    all_categories = list(mongo.db.categories.find())
    all_stories = list(mongo.db.stories.find())
    for story in all_stories:
        story["category"] = list(filter(lambda x: story["category"] == x.get(
            '_id'), all_categories))[0].get('category_name')

    return render_template('stories.html', stories=all_stories)

# A lambda was used in order to get the category id associated with each story & display the relevant category name
@app.route('/stories/<stories_id>')
def stories(stories_id):
    all_categories = list(mongo.db.categories.find())
    story = mongo.db.stories.find_one({'_id': ObjectId(stories_id)})
    story["category"] = list(filter(lambda x: story.get(
        "category") == x.get('_id'), all_categories))[0].get('category_name')
    return render_template('selected_story.html', story=story)


@app.route('/add_story')
def add_story():
    return render_template('add_story.html',
                           categories=mongo.db.categories.find())

# The category id is initially displayed but above code ensures the corresponding category name is displayed
@app.route('/insert_story', methods=['POST'])
def insert_story():
    stories = mongo.db.stories
    category = mongo.db.categories.find_one(
        {"category_name": request.form.get('category')})
    stories.insert_one({
        'story_name': request.form.get('story_name'),
        'category': category.get('_id'),
        'submitted_by': request.form.get('submitted_by'),
        'story_text': request.form.get('story_text'),
        'story_image': request.form.get('story_image')
    })
    return redirect(url_for('get_stories'))


@app.route('/edit_stories/<stories_id>')
def edit_stories(stories_id):
    the_story = mongo.db.stories.find_one({"_id": ObjectId(stories_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_story.html', story=the_story,
                           categories=all_categories)


@app.route('/update_stories/<stories_id>', methods=["POST"])
def update_stories(stories_id):
    stories = mongo.db.stories
    category = mongo.db.categories.find_one(
        {"category_name": request.form.get('category')})
    stories.update_one({'_id': ObjectId(stories_id)},
                       {"$set":
                        {
                            'story_name': request.form.get('story_name'),
                            'category': category.get('_id'),
                            'submitted_by': request.form.get('submitted_by'),
                            'story_text': request.form.get('story_text'),
                            'story_image': request.form.get('story_image')
                        }})
    return redirect(url_for('get_stories'))


@app.route('/delete_story/<stories_id>')
def delete_story(stories_id):
    mongo.db.stories.remove({'_id': ObjectId(stories_id)})
    return redirect(url_for('get_stories'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=should_debug)
