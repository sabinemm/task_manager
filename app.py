import os
import ssl
import pymongo
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config['MONGO_URI'] = os.getenv(
    'MONGO_URI', 'mongodb+srv://sabine:r00t@myfirstcluster-y6w96.mongodb.net/task_manager')
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html', categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")), debug=True)
