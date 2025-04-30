from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Enkel liste for å lagre oppgaver i minnet
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form['task']
    if task_text:
        tasks.append({'text': task_text, 'done': False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
