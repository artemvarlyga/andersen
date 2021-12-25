import sys

from flask import Flask

app = Flask(__name__)

@app.route('/')
def simple_func():
    return 'Hello Andersen!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=sys.argv[1])
