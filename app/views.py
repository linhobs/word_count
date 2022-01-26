from crypt import methods
from re import I
from app import app
from app.tasks import count_words
from app import queue
from flask import render_template, request
@app.route('/')
def index():
    return "hello world"


@app.route('/add-task', methods = ["GET", "POST"])
def add_task():
    jobs = queue.jobs
    message = None

    if request.args:
        url = request.args.get('url')
        task = queue.enqueue(count_words, url)
        jobs = queue.jobs
        queue_len = len(queue)
        message = f" Task queued at {task.enqueued_at}. {queue_len} jobs queued"
    return render_template('index.html', message=message, jobs=jobs)