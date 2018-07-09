import os
from flask import Flask

redis_hostname = os.environ.get('redis_hostname', 'redis')
test_env = os.environ.get('test_env', 'none')

app = Flask(__name__)


@app.route('/')
def index():
    return "Index page"


@app.errorhandler(404)
def page_not_found(e):
    return "Page not found"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
