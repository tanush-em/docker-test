from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    count = cache.incr('hits')
    return f"<h1>Hello! This page has been visited {count} times.</h1>"
