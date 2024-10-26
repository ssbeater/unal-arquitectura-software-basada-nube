from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/tasks/<taskId>', methods=['PUT'])
def update_task(taskId):
    data = request.json
    task_id = int(taskId)
    name = data.get('name')
    description = data.get('description')

    updated_task = TaskService.update_task(task_id, name, description)

    if updated_task is None:
        return jsonify({'message': 'Task not found'}), 404

    return jsonify({'message': 'Task updated'}), 200

@task_blueprint.route('/')
def index():
    return render_template('index.html')
