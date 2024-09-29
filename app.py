from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This list will hold the tasks temporarily
tasks = []

# To track completed tasks
completed_tasks = set()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task:
            tasks.append(new_task)

        return redirect(url_for('index'))

    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks, enumerate=enumerate)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        completed_tasks.add(task_id)  # Add task index to completed_tasks set

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)  # Remove task by index
        # Also remove it from the completed set if marked as complete
        if task_id in completed_tasks:
            completed_tasks.remove(task_id)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
