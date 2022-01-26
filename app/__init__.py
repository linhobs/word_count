from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)


redis_instance = redis.Redis()
queue = Queue(connection=redis_instance)

from app import views, tasks