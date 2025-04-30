from flask import Flask, render_template, request, redirect, url_for
from collections import defaultdict

app = Flask(__name__)

# Hver oppgave har tekst, status og kategori
tasks = []

@app.route('/')
def index():
    categorized_tasks = defaultdict(list)
    for i, task in enumerate(tasks):
        task_with_id = task.copy()
        task_with_id['id'] = i
        categorized_tasks[task['category']].append(task_with_id)
    return render_template('index.html', categorized_tasks=categorized_tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form['task']
    category = request.form['category'] or "Uten kategori"
    if task_text:
        tasks.append({'text': task_text, 'done': False, 'category': category})
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/snake')
def snake():
    return render_template('snake.html')



if __name__ == '__main__':
    app.run(debug=True)
