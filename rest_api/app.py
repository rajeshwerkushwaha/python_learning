from flask import Flask, jsonify

# to initiate Flask app
app = Flask(__name__)

# creating a tasks list which acts as a Database(in rea)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# set the route for default
@app.route('/')
def index():
  return 'Welcome to REST API demo in Python!'


# set the route for getting all the tasks
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


# set the route for specific task based on task id
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


# run the app
if __name__ == '__main__':
    app.run(debug=True)