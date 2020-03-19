import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'lights-out'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/get_stories')
def get_stories():
    return render_template('stories.html', stories=mongo.db.stories.find())


@app.route('/stories/<stories_id>')
def stories(stories_id):
    stories = mongo.db.stories.find_one({'_id': ObjectId(stories_id)})
    return render_template('selected_story.html', story=stories)


@app.route('/add_story')
def add_story():
    return render_template('add_story.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_story', methods=['POST'])
def insert_story():
    stories = mongo.db.stories
    stories.insert_one(request.form.to_dict())
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
    print(request.form.get("category"))
    stories.update_one({'_id': ObjectId(stories_id)},
                       {"$set":
                        {
                            'story_name': request.form.get('story_name'),
                            'category': request.form.get('category'),
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
            debug=True)
