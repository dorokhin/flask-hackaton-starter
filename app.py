import os
from flask import Flask

redis_hostname = os.environ.get('redis_hostname', 'redis')


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def index():
    return "Index page"


@app.route('/env')
def env_get():
    return os.environ.get('APP_SETTINGS', 'None')


@app.errorhandler(404)
def page_not_found(e):
    return "Page not found"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
